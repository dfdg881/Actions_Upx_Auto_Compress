#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, struct, select, argparse, time, random, ipaddress, ssl, threading, logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

CF_CIDRS = [
    "103.21.244.0/22","103.22.200.0/22","103.31.4.0/22","104.16.0.0/13","104.24.0.0/14",
    "108.162.192.0/18","131.0.72.0/22","141.101.64.0/18","162.158.0.0/15","172.64.0.0/13",
    "173.245.48.0/20","188.114.96.0/20","190.93.240.0/20","197.234.240.0/22","198.41.128.0/17"
]

def rand_ip_from_cidr(cidr:str)->str:
    n=ipaddress.ip_network(cidr)
    if n.version!=4: return str(list(n.hosts())[0])
    cnt=n.num_addresses
    if cnt<=2: return str(n.network_address)
    return str(n.network_address + random.randint(1, cnt-2))

def rand_ip_from_cidrs(cidrs, k):
    seen=set(); out=[]
    while len(out)<k and len(seen)<k*10:
        ip=rand_ip_from_cidr(random.choice(cidrs))
        if ip not in seen: seen.add(ip); out.append(ip)
    return out

def test_cf_ip(ip, timeout=2.0, port=443):
    try:
        t=time.perf_counter()
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(timeout); s.connect((ip,port))
        ctx=ssl.create_default_context(); ss=ctx.wrap_socket(s, server_hostname="cloudflare.com")
        ss.sendall(b"GET / HTTP/1.1\r\nHost: cloudflare.com\r\nConnection: close\r\n\r\n")
        r=ss.recv(1_024); ss.close(); s.close()
        return (time.perf_counter()-t) if (r and r.startswith(b"HTTP/")) else None
    except Exception as e:
        log.debug("CF test %s fail: %s", ip, e); return None

def select_best_cf_ip(count=10, timeout=2.0):
    log.info("Cloudflare IP 优选中，测试 %d 个 IP...", count)
    ips=rand_ip_from_cidrs(CF_CIDRS, count); res=[]
    for i,ip in enumerate(ips,1):
        log.info("[%d/%d] 测试 %s:443 ...", i, len(ips), ip)
        lat=test_cf_ip(ip, timeout)
        if lat is not None: res.append((ip,lat)); log.info("  ✓ %s - %.2fms", ip, lat*1000)
        else: log.info("  ✗ %s - 失败", ip)
    if not res: log.warning("全部失败"); return None
    res.sort(key=lambda x:x[1]); best=res[0]; log.info("最佳: %s (%.2fms)", best[0], best[1]*1000)
    return best[0]

def is_client_hello(d:bytes):
    return len(d)>6 and d[0]==0x16 and d[5]==0x01 and 0x0301<= struct.unpack(">H", d[1:3])[0] <=0x0304

def find_sni_mid(d:bytes):
    try:
        if not is_client_hello(d) or len(d)<43: return None
        p=5+4+2+32  # rec hdr(5) already before; + hs header(4) + ver(2) + rnd(32)
        if p>=len(d): return None
        sid_len=d[p]; p+=1+sid_len
        cs_len=struct.unpack(">H", d[p:p+2])[0]; p+=2+cs_len
        cm_len=d[p]; p+=1+cm_len
        ext_len=struct.unpack(">H", d[p:p+2])[0]; p+=2
        end=p+ext_len
        while p+4<=end:
            et,el=struct.unpack(">HH", d[p:p+4]); p+=4
            if et==0:  # SNI
                if p+5>len(d): return None
                hn_len=struct.unpack(">H", d[p+3:p+5])[0]
                hs=p+5; he=hs+hn_len
                if he>len(d): return None
                return hs + hn_len//2
            p+=el
        return None
    except Exception as e:
        log.debug("parse CH fail: %s", e); return None

def split_tls_records(d:bytes):
    mid=find_sni_mid(d)
    if mid is None: return [d]
    hdr=d[:3]; pay=d[5:]; sp=mid-5
    p1,p2=pay[:sp], pay[sp:]
    r1=hdr+struct.pack(">H",len(p1))+p1
    r2=hdr+struct.pack(">H",len(p2))+p2
    log.info("TLS Record 分片: %d + %d 字节", len(r1), len(r2))
    return [r1,r2]

class DNSMini:
    def __init__(self): self.map={}
    def set(self, host, ip): self.map[host]=ip; log.info("解析覆盖: %s -> %s", host, ip)
    def resolve(self, host): return self.map.get(host, host)

def send_reply_ok(csock, rep=0x00):
    csock.sendall(b"\x05"+bytes([rep])+b"\x00\x01"+socket.inet_aton("0.0.0.0")+struct.pack(">H",0))

def socks5_handshake(csock):
    try:
        d=csock.recv(257)
        if len(d)<2 or d[0]!=5: return False
        csock.sendall(b"\x05\x00"); return True
    except: return False

def socks5_request(csock):
    try:
        d=csock.recv(4)
        if len(d)!=4 or d[0]!=5 or d[1]!=1: return None
        atyp=d[3]
        if atyp==1:
            dst=socket.inet_ntoa(csock.recv(4))
        elif atyp==3:
            l=csock.recv(1)[0]; dst=csock.recv(l).decode()
        else: return None
        port=struct.unpack(">H", csock.recv(2))[0]
        return dst,port
    except: return None

def pipe(csock, tsock, tport):
    first=True; is_https=(tport==443)
    csock.setblocking(False); tsock.setblocking(False)
    try:
        while True:
            r,_,e=select.select([csock,tsock],[],[csock,tsock],1.0)
            if e: break
            if csock in r:
                data=csock.recv(8192)
                if not data: break
                if first and is_https and is_client_hello(data):
                    first=False
                    for rec in split_tls_records(data): tsock.sendall(rec)
                else: tsock.sendall(data)
            if tsock in r:
                data=tsock.recv(8192)
                if not data: break
                csock.sendall(data)
    except Exception as ex:
        log.debug("pipe err: %s", ex)
    finally:
        tsock.close()

def handle_client(csock, dns):
    try:
        if not socks5_handshake(csock): return
        req=socks5_request(csock)
        if not req: return
        host,port=req
        dst=dns.resolve(host)
        log.info("CONNECT %s:%d%s", host, port, f" 解析到:{dst}" if dst!=host else "")
        ts=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            ts.connect((dst,port)); send_reply_ok(csock,0x00)
        except Exception as e:
            log.error("连接失败: %s", e); send_reply_ok(csock,0x05); ts.close(); return
        pipe(csock, ts, port)
    finally:
        csock.close()

def main():
    p=argparse.ArgumentParser(description="精简版 SOCKS5 + TLS ClientHello 分片 + 可选 Cloudflare IP 优选")
    p.add_argument("--host", default="127.0.0.1"); p.add_argument("--port", type=int, default=9178)
    p.add_argument("--no-cf-select", action="store_true"); p.add_argument("--cf-test-count", type=int, default=10)
    p.add_argument("--cf-timeout", type=float, default=2.0); p.add_argument("--debug", action="store_true")
    a=p.parse_args()
    if a.debug: logging.getLogger().setLevel(logging.DEBUG)
    dns=DNSMini()
    if not a.no_cf_select:
        log.info("="*60); log.info("启用 Cloudflare IP 优选"); log.info("="*60)
        best=select_best_cf_ip(a.cf_test_count, a.cf_timeout)
        if best: 
            dns.set("linux.do", best)
            dns.set("connect.linux.do", best)
            dns.set("webmail.linux.do", best)
            dns.set("lottery.linux.do", best)
            dns.set("cdk.linux.do", best)
            dns.set("rate.linux.do", best)
            dns.set("nav.linux.do", best)
        log.info("="*60)
    srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1); srv.bind((a.host,a.port)); srv.listen(128)
    log.info("SOCKS5 监听 %s:%d；分片模式: TCP_NODELAY", a.host, a.port)
    try:
        while True:
            c,addr=srv.accept(); log.info("来自 %s 的连接", addr)
            threading.Thread(target=handle_client, args=(c,dns), daemon=True).start()
    except KeyboardInterrupt:
        pass
    finally:
        srv.close()

if __name__=="__main__": main()