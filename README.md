<div align="center">
  <h1 align="center">Actions_Upx_Auto_Compress</h1>
</div>

<div align="center">一个自动化下载指定软件最新版本并使用UPX工具进行压缩的项目，可减少人工操作，提高效率</div>
<br>
<p align="center">
  <!-- 这里可添加项目的一些状态图标，如版本、下载量等，由于没有具体信息，暂不添加 -->
</p>

[English](./README_en.md) | 中文

### 项目导航
- [特点](#特点)
- [快速上手](#快速上手)
- [许可证](#许可证)

> [!IMPORTANT]
> 1. 使用gh action进行操作
> 2. 需要确保下载的软件和UPX工具与运行环境兼容。

## 特点

- ✅ 自动化：实现了软件下载、压缩和工件上传的自动化，减少了人工操作的繁琐。
- ✅ 灵活性：用户可以根据需要自定义UPX的压缩参数，还可以在`upx.yml`中自定义要下载的文件。
- ✅ 版本管理：通过获取软件的最新版本信息，确保每次运行工作流时都使用最新版本的软件进行压缩。


## 快速上手

### 工作流
Fork 本项目并开启工作流，具体步骤请见[详细教程](./docs/workflow.md)


## 许可证

[MIT](./LICENSE) License &copy; 2025 - PRESENT [dfdg881](https://github.com/dfdg881)
