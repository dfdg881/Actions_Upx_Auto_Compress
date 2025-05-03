# 详细教程

## 一、Fork 项目
打开项目仓库页面，在页面右上角点击“Fork”按钮。这会将原仓库的代码复制到您自己的 GitHub 账户下。
在弹出的确认页面中，选择将仓库复制到您希望的位置，通常是您自己的账户。确认信息无误后，点击“Fork”按钮完成复制。

## 二、打开 Action
进入您 Fork 后的仓库页面。
在仓库页面的导航栏中，找到并点击“Actions”选项卡。如果这是您第一次打开该仓库的 Actions 页面，可能会看到一个提示，告知您需要启用工作流。按照提示点击相应的按钮启用工作流。
工作流触发方式补充
根据 [GitHub 文档](https://docs.github.com/zh/actions)，工作流可以通过多种事件触发，除了手动触发的 workflow_dispatch，还可以通过 push、pull_request 等事件触发。

## 三、运行
### （一）选择工作流
### Download and Compress Alist with UPX
下载最新Arm64版本的[Alist](https://github.com/AlistGo/alist) 软件，并使用 UPX 工具对其进行压缩
### Download and Compress AdGuardHome with UPX
下载最新Arm64版本的[AdGuardHome](https://github.com/AdguardTeam/AdGuardHome)软件，并使用 UPX 工具对其进行压缩
### ustom File Download and Compress with UPX
自定义下载文件的 URL，根据用户提供的文件 URL 下载文件，并使用 UPX 工具对其进行压缩

根据您的需求，选择相应的工作流文件。

### （二）触发工作流

在 Actions 页面中，找到您想要运行的工作流名称（如 Download and Compress AdGuardHome with UPX），点击该工作流后点击旁边的“Run workflow”按钮。

### （三）填写输入参数
### Download and Compress AdGuardHome with UPX | Download and Compress Alist with UPX
可传入 upx_args 参数，用于指定 UPX 的压缩参数，默认为 --best。如果您需要修改该参数，例如使用 --ultra-brute 压缩模式，可以在触发工作流时将 upx_args 设置为 --ultra-brute。填写完成后，点击“Run workflow”确认触发工作流。
### Custom File Download and Compress with UPX
需要填写以下参数：
file_url：必须填写有效的文件下载 URL。根据 GitHub 文档，在填写 URL 时，要确保该 URL 是可访问的，并且具有相应的下载权限。
file_name：可根据需要填写下载文件的名称，若不填写则默认为 example。
save_path：可指定文件的保存路径，若不填写则默认为当前工作目录。在指定保存路径时，要确保该路径具有写入权限。
upx_args：可根据需要修改 UPX 的压缩参数，默认为 --best。填写完成后，点击“Run workflow”确认触发工作流。
## 四、下载upx压缩后的件
当工作流运行成功后，在 Actions 页面中找到刚刚运行的工作流记录，点击进入该记录的详情页面。
在详情页面中，找到“Artifacts”部分，点击文件的名称，即可下载压缩后的文件。
