# Detailed Tutorial

## 1. Fork the Repository
Open the project repository page and click the `Fork` button in the upper right - hand corner of the page. This will copy the code of the original repository to your own GitHub account.
![fork](./images/fork-btn.png 'fork')

On the pop - up confirmation page, select the location where you want to copy the repository, usually your own account. After confirming that the information is correct, click the `Crrate Fork` button to complete the copying.

![fork2](./images/fork-detail.png 'fork2')

## 2. Open Actions
Go to the repository page after you forked it.
In the navigation bar of the repository page, find and click the `Actions` tab.
![Actions Entry](./images/actions-btn.png 'Actions Entry')

2. Enable the Actions workflow:

![Enable Actions Workflow](./images/actions-enable.png 'Enable Actions Workflow')

## 3. Run
### (1) Select the Workflow
### Download and Compress Alist with UPX
Download the latest Arm64 version of [Alist](https://github.com/AlistGo/alist) software and compress it using the UPX tool.
### Download and Compress AdGuardHome with UPX
Download the latest Arm64 version of [AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) software and compress it using the UPX tool.
### Custom File Download and Compress with UPX
Customize the URL of the file to be downloaded. Download the file according to the file URL provided by the user and compress it using the UPX tool.
Select the corresponding workflow branch according to your needs.
![Select Workflow Branch](./images/choose.png 'Select Workflow Branch')

### (2) Trigger the Workflow
On the Actions page, find the name of the workflow you want to run (e.g., Download and Compress AdGuardHome with UPX). 

### Fill in the Input Parameters
#### Download and Compress AdGuardHome with UPX | Download and Compress Alist with UPX
`upx_args`: Used to specify the compression parameters of UPX, with the default being --best. If you need to modify the parameters, for example, use the --ultra-brute compression mode, you can set `upx_args` to --ultra-brute when triggering the workflow.
#### Custom File Download and Compress with UPX
The following parameters need to be filled in:
`file_url`: The direct download URL of the file.
`file_name`: The name of the downloaded file, with the default being example.
`save_path`: The save path of the file, with the default being the current working directory.
`upx_args`: You can modify the compression parameters of UPX as needed, with the default being --best.

Click on the workflow and then click the `Run workflow` button next to it.
![run workflow](./images/run.png 'run workflow')

According to the [GitHub Documentation](https://docs.github.com/en/actions), workflows can be triggered by various events. In addition to the manually triggered workflow_dispatch, they can also be triggered by events such as push and pull_request.


## 4. Download the File Compressed by UPX
When the workflow runs successfully, find the record of the workflow you just ran on the Actions page and click to enter the details page of this record.
On the details page, find the "Artifacts" section and click on the name of the file to download the compressed file.
![download artifacts](./images/download.png 'run workflow')