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
	``` Bash
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
1. `npm list`
	查看本地模块
2. `npm install mysql`
	安装mysql模块
3. `npm uninstall mysql`
	卸载mysql模块
4. `npm root`
	本地模块根目录
5. `npm root -g`
	本服务器所有模块根目录
6. `npm update mysql`
	升级mysql模块
7. `npm search mysql`
	搜索mysql模块
8. `npm -help <command>`
	查看帮助

# 开始第一个 node.js web 实例
```JavaScript
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
```
![第一个web应用](http://i.imgur.com/uqEFm2H.png)
# node.js 回调函数
>Node.js 异步编程的直接体现就是回调。
异步编程依托于回调来实现，但不能说使用了回调后程序就异步化了。
回调函数在完成任务后就会被调用，Node 使用了大量的回调函数，Node 所有 API 都支持回调函数。
例如，我们可以一边读取文件，一边执行其他命令，在文件读取完成后，我们将文件内容作为回调函数的参数返回。这样在执行代码时就没有阻塞或等待文件 I/O 操作。这就大大提高了 Node.js 的性能，可以处理大量的并发请求。

## 1. 同步操作文件(阻塞I/O)
```JavaScript
 //加载fs file 模块
 const fs = require('fs');
 file = "test.txt";
 //开始读取文件
 console.log('file start');
 //正在读取文件
 data = fs.readFileSync(file);
 console.log(data.toString());
 //读取文件结束
 console.log('file end！');
```
![同步操作文件](http://i.imgur.com/PuaItru.png)
## 2. 异步操作文件(非阻塞I/O)
```JavaScript
//加载fs file 模块
const fs = require('fs');
file = "test.txt";
//开始读取文件
console.log('file start');
//正在读取文件
//自带事件(当文件内容读取完毕时)
fs.readFile(file,function(err, data){
	 console.log(data.toString());
});
//读取文件结束
console.log('file end！');
```
![异步操作文件](http://i.imgur.com/kX5fFsu.png)
# Node.js 事件循环
>Node.js 是单进程单线程应用程序，但是通过事件和回调支持并发，所以性能非常高。<br>
>Node.js 的每一个 API 都是异步的，并作为一个独立线程运行，使用异步函数调用，并处理并发。<br>
>Node.js 基本上所有的事件机制都是用设计模式中观察者模式实现。<br>
>Node.js 单线程类似进入一个while(true)的事件循环，直到没有事件观察者退出，每个异步事件都生成一个事件观察者，如果有事件发生就调用该回调函数.<br>

```JavaScript
const events = require('events');
evt = new events.EventEmitter();
function eventHandler(){
	console.log('run');
}
//当触发eventName时，调用eventHandler
evt.on('eventName',eventHandler);
//触发eventName
evt.emit('eventName');
```