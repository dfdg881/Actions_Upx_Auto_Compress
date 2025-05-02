<div align="center">
  <h1 align="center">Actions_Upx_Auto_Compress</h1>
</div>

<div align="center">A project that automatically downloads the latest version of specified software and compresses it using the UPX tool, which can reduce manual operations and improve efficiency.</div>
<br>
<p align="center">
  <!-- You can add some status icons for the project here, such as version, download volume, etc. Since there is no specific information, it is not added for now. -->
</p>

English | [Chinese](./README.md)

### Project Navigation
- [Features](#Features)
- [Workflow Instructions](#Workflow-Instructions)
- [Quick Start](#Quick-Start)
- [License](#License)

> [!IMPORTANT]
> 1. Operate using GitHub Actions.
> 2. Ensure that the downloaded software and the UPX tool are compatible with the operating environment.

## Features

- ✅ Automation: Automates software downloading, compression, and artifact uploading, reducing the complexity of manual operations.
- ✅ Flexibility: Users can customize the compression parameters of UPX as needed and can also customize the files to be downloaded in `upx.yml`.
- ✅ Version Management: Ensures that the latest version of the software is used for compression each time the workflow runs by obtaining the latest version information of the software.

## Workflow Instructions

### 1. alist.yml
- **Function**: This workflow is mainly used to download the latest version of [alist](https://github.com/AlistGo/alist) and compress it using UPX.
- **Usage Method**: It can be manually triggered (`workflow_dispatch`), and the compression parameters of UPX (`upx_args`) can be specified during triggering. The default parameter is `--best`.
- **Key Steps**: 
    - Check out the repository code.
    - Install the `jq` tool for parsing JSON data.
    - Obtain the latest version information and download link of Alist.
    - Obtain the latest version information and download link of UPX.
    - Download and extract Alist.
    - Download and set up UPX.
    - Compress the Alist executable file using UPX.
    - Verify the existence of the compressed file.
    - Upload the compressed Alist as an artifact.

### 2. update.yml
- **Function**: This workflow is used to download the latest version of AdGuardHome (an ad blocker) and compress it using UPX.
- **Usage Method**: It can also be manually triggered, and the compression parameters of UPX can be specified. The default parameter is `--best`.
- **Key Steps**: 
    - Check out the repository code.
    - Install the `jq` tool.
    - Obtain the latest version information and download link of AdGuardHome.
    - Obtain the latest version information and download link of UPX.
    - Download and extract AdGuardHome.
    - Download and set up UPX.
    - Compress the AdGuardHome executable file using UPX.
    - Upload the compressed AdGuardHome as an artifact.

### 3. upx.yml
- **Function**: This workflow allows users to customize the URL, file name, save path, and UPX compression parameters of the file to be downloaded, and then download the file and compress it using UPX.
- **Usage Method**: When manually triggering, the URL of the file (`file_url`) needs to be specified. You can optionally specify the file name (`file_name`), save path (`save_path`), and UPX compression parameters (`upx_args`). The default file name is `example`, the default save path is `./`, and the default compression parameter is `--best`.
- **Key Steps**: 
    - Check out the repository code.
    - Set up the working directory.
    - Obtain the latest version information and download link of UPX.
    - Install the `jq` tool.
    - Download the specified file.
    - Download and set up UPX.
    - Compress the downloaded file using UPX.
    - Upload the compressed file as an artifact.

## Quick Start

### Workflow
Fork this project, go to the Actions page of the GitHub repository, enable the corresponding workflow, and set the parameters as needed.

## License

[MIT](./LICENSE) License &copy; 2025 - PRESENT [dfdg881](https://github.com/dfdg881)