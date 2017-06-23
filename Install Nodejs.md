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