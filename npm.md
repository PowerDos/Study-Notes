# NPM node.js 模块管理 
## NPM简介
NPM是随同NodeJS一起安装的包管理工具，能解决NodeJS代码部署上的很多问题，常见的使用场景有以下几种：

    允许用户从NPM服务器下载别人编写的第三方包到本地使用。
    允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
    允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。 
## NPM常用命令
1. npm list
	查看本地模块
2. npm install mysql
	安装mysql模块
3. npm uninstall mysql
	卸载mysql模块
4. npm root
	本地模块根目录
5. npm root -g
	本服务器所有模块根目录
6. npm update mysql
	升级mysql模块
7. npm search mysql
	搜索mysql模块
8. npm -help <command>
	查看帮助