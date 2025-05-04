# Detailed Tutorial

## 1. Fork the Project
Open the project repository page and click the "Fork" button in the upper right corner of the page. This will copy the code of the original repository to your own GitHub account.
On the pop - up confirmation page, select the location where you want to copy the repository, usually your own account. After confirming that the information is correct, click the "Fork" button to complete the copy.

## 2. Open Actions
Enter the page of the repository you forked.
In the navigation bar of the repository page, find and click the "Actions" tab. If this is the first time you open the Actions page of this repository, you may see a prompt informing you that you need to enable the workflow. Follow the prompt and click the corresponding button to enable the workflow.
Supplementary information on workflow triggering methods
According to the [GitHub Docs](https://docs.github.com/en/actions), workflows can be triggered by various events. In addition to the manually triggered workflow_dispatch, they can also be triggered by events such as push and pull_request.

## 3. Run
### (1) Select a Workflow
### Download and Compress Alist with UPX
Download the latest Arm64 version of [Alist](https://github.com/AlistGo/alist) software and compress it using the UPX tool.
### Download and Compress AdGuardHome with UPX
Download the latest Arm64 version of [AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) software and compress it using the UPX tool.
### Custom File Download and Compress with UPX
Customize the URL of the file to be downloaded. Download the file according to the file URL provided by the user and compress it using the UPX tool.

Select the corresponding workflow file according to your needs.

### (2) Trigger the Workflow

On the Actions page, find the name of the workflow you want to run (e.g., Download and Compress AdGuardHome with UPX). Click on the workflow and then click the "Run workflow" button next to it.

### (3) Fill in the Input Parameters
### Download and Compress AdGuardHome with UPX | Download and Compress Alist with UPX
You can pass in the upx_args parameter to specify the compression parameters of UPX, with the default being --best. If you need to modify this parameter, for example, to use the --ultra - brute compression mode, you can set upx_args to --ultra - brute when triggering the workflow. After filling in, click "Run workflow" to confirm triggering the workflow.
### Custom File Download and Compress with UPX
The following parameters need to be filled in:
file_url: You must fill in a valid file download URL. According to the GitHub Documentation, when filling in the URL, ensure that the URL is accessible and has the corresponding download permissions.
file_name: You can fill in the name of the downloaded file as needed. If not filled in, the default is example.
save_path: You can specify the save path of the file. If not filled in, the default is the current working directory. When specifying the save path, ensure that the path has write permissions.
upx_args: You can modify the compression parameters of UPX as needed, with the default being --best. After filling in, click "Run workflow" to confirm triggering the workflow.

## 4. Download the File Compressed by UPX
When the workflow runs successfully, find the record of the workflow you just ran on the Actions page and click to enter the details page of this record.
On the details page, find the "Artifacts" section and click the name of the file to download the compressed file.