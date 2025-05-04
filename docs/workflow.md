# 详细教程

## 一、Fork 项目
打开项目仓库页面，在页面右上角点击`Fork`按钮。这会将原仓库的代码复制到您自己的 GitHub 账户下。
![fork](./images/fork-btn.png 'fork')

在弹出的确认页面中，选择将仓库复制到您希望的位置，通常是您自己的账户。确认信息无误后，点击`Crate Fork`按钮完成复制。
![fork2](./images/fork-detail.png 'fork2')

## 二、打开 Action
进入您 Fork 后的仓库页面。
在仓库页面的导航栏中，找到并点击`Actions`选项卡。
![Actions入口](./images/actions-btn.png 'Actions入口')

2. 开启 Actions 工作流：

![开启Actions工作流](./images/actions-enable.png '开启Actions工作流')

## 三、运行
### （一）选择工作流
### Download and Compress Alist with UPX
下载最新Arm64版本的[Alist](https://github.com/AlistGo/alist) 软件，并使用 UPX 工具对其进行压缩
### Download and Compress AdGuardHome with UPX
下载最新Arm64版本的[AdGuardHome](https://github.com/AdguardTeam/AdGuardHome)软件，并使用 UPX 工具对其进行压缩
### Custom File Download and Compress with UPX
自定义下载文件的 URL，根据用户提供的文件 URL 下载文件，并使用 UPX 工具对其进行压缩
根据您的需求，选择相应的工作流分支。
![选择工作流分支](./images/choose.png '选择工作流分支')

### （二）触发工作流

在 Actions 页面中，找到您想要运行的工作流名称（如 `Download and Compress AdGuardHome with UPX`），点击该工作流后点击旁边的`Run workflow`按钮
![run workflow](./images/run.png 'run workflow')

#### 可填写参数
##### Download and Compress AdGuardHome with UPX | Download and Compress Alist with UPX
`upx_args`:用于指定 UPX 的压缩参数，默认为 --best。如需修改参数，例如使用 --ultra-brute 压缩模式，可以在触发工作流时将 `upx_args` 设置为 --ultra-brute。
##### Custom File Download and Compress with UPX
`file_url`：文件下载 URL。(直链)
`file_name`：下载文件的名称，默认为 example。
`save_path`：文件的保存路径，默认为当前工作目录。
`upx_args`：可根据需要修改 UPX 的压缩参数，默认为 --best。
填写完参数后点击旁边绿色的`Run workflow`按钮开始运行
根据 [GitHub 文档](https://docs.github.com/zh/actions)，工作流可以通过多种事件触发，除了手动触发的 workflow_dispatch，还可以通过 push、pull_request 等事件触发。

## 四、下载upx压缩后的文件
当工作流运行成功后，在 Actions 页面中找到刚刚运行的工作流记录，点击进入该记录的详情页面。
在详情页面中，找到“Artifacts”部分，点击文件的名称，即可下载压缩后的文件。
![download artifacts](./images/download.png 'run workflow')

