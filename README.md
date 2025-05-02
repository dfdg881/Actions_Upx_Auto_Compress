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
- [工作流说明]( #工作流说明)
- [快速上手](#快速上手)
- [许可证](#许可证)

> [!IMPORTANT]
> 1. 使用gh action进行操作
> 2. 需要确保下载的软件和UPX工具与运行环境兼容。

## 特点

- ✅ 自动化：实现了软件下载、压缩和工件上传的自动化，减少了人工操作的繁琐。
- ✅ 灵活性：用户可以根据需要自定义UPX的压缩参数，还可以在`upx.yml`中自定义要下载的文件。
- ✅ 版本管理：通过获取软件的最新版本信息，确保每次运行工作流时都使用最新版本的软件进行压缩。

## 工作流说明

### 1. alist.yml
- **功能**：该工作流主要用于下载[alist](https://github.com/AlistGo/alist)的最新版本，并使用UPX进行压缩。
- **使用方法**：可以通过手动触发（`workflow_dispatch`），在触发时可以指定UPX的压缩参数（`upx_args`），默认参数为`--best`。
- **关键步骤**：
    - 检查仓库代码。
    - 安装`jq`工具，用于解析JSON数据。
    - 获取Alist的最新版本信息和下载链接。
    - 获取UPX的最新版本信息和下载链接。
    - 下载并解压Alist。
    - 下载并设置UPX。
    - 使用UPX压缩Alist可执行文件。
    - 验证压缩后的文件是否存在。
    - 上传压缩后的Alist作为工件。

### 2. update.yml
- **功能**：此工作流用于下载AdGuardHome（一款广告拦截器）的最新版本，并使用UPX进行压缩。
- **使用方法**：同样通过手动触发，可指定UPX压缩参数，默认参数为`--best`。
- **关键步骤**：
    - 检查仓库代码。
    - 安装`jq`工具。
    - 获取AdGuardHome的最新版本信息和下载链接。
    - 获取UPX的最新版本信息和下载链接。
    - 下载并解压AdGuardHome。
    - 下载并设置UPX。
    - 使用UPX压缩AdGuardHome可执行文件。
    - 上传压缩后的AdGuardHome作为工件。

### 3. upx.yml
- **功能**：该工作流允许用户自定义要下载的文件的URL、文件名、保存路径和UPX压缩参数，然后下载文件并使用UPX进行压缩。
- **使用方法**：手动触发时，需要指定文件的URL（`file_url`），可以选择指定文件名（`file_name`）、保存路径（`save_path`）和UPX压缩参数（`upx_args`），默认文件名是`example`，默认保存路径是`./`，默认压缩参数是`--best`。
- **关键步骤**：
    - 检查仓库代码。
    - 设置工作目录。
    - 获取UPX的最新版本信息和下载链接。
    - 安装`jq`工具。
    - 下载指定的文件。
    - 下载并设置UPX。
    - 使用UPX压缩下载的文件。
    - 上传压缩后的文件作为工件。

## 快速上手

### 工作流
Fork 本项目并GitHub仓库的Actions页面，开启相应的工作流，并根据需要设置参数

## 许可证

[MIT](./LICENSE) License &copy; 2025 - PRESENT [dfdg881](https://github.com/dfdg881)
