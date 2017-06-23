# Node.js-Notes
Node.js Study Notes
# Install Node.js
1. 下载node.js
	
	前往[https://nodejs.org/en/](https://nodejs.org/en/ "https://nodejs.org/en/")下载node.js稳定版
	![下载稳定版](http://i.imgur.com/1byvubu.png)


2. 安装环境(windows 7 64位环境下)
	
	- 一直Next就可以了
	
	![安装](http://i.imgur.com/gRew5uL.png)
	
	- 在终端直接查看node.js的版本，查询到即安装成功
	
	![安装完成](http://i.imgur.com/awvnLdR.png)


3. 结合Sublime开发
	
	- 创建新的编译环境
	
	  ![创建新编译环境](http://i.imgur.com/IDga1Cv.png)
	- 在里面写入
	```
	{
		"cmd": ["node", "$file"],
		"selector": "source.js"
	}
	```
	- 保存并重命名
	
	![保存并重命名](http://i.imgur.com/Jzs3iNo.png)
	- 写一个js文件，输出Hello World.按Ctrl+B进行编译，如果无反应，请重启sublime，出现Hello World即为成功
	
	![sublime](http://i.imgur.com/LXs03iI.png)

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

# 开始第一个 node.js web 实例
	//加载http web模块
	const http = require('http');
	cs = function (req, res) {
		//设置head头
		res.writeHead('200',{'content-type':'text/html;charset=utf-8'});
		//给客户端返回内容
		res.write('hello world! Gavin first Node.js Web'); 
		res.end();
	}
	//监听端口
	http.createServer(cs).listen(666);
	console.log('http is ok');