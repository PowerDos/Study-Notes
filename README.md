# Node.js-Notes
个人的 Node.js 学习笔记，有兴趣的小伙伴可以了解下，希望能帮到你们
### 目录
1. [安装Node.js](#install-nodejs)
2. [NPM node.js 模块管理](#NPM node.js 模块管理)	
	- [NPM简介](#NPM简介)
	- [NPM常用命令](#NPM常用命令)
3. [开始第一个 node.js web 实例](#开始第一个 node.js web 实例)


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
>NPM是随同NodeJS一起安装的包管理工具，能解决NodeJS代码部署上的很多问题，常见的使用场景有以下几种：
>- 允许用户从NPM服务器下载别人编写的第三方包到本地使用。
>- 允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
>- 允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。
 
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

# Node.js 模块
> 为了让Node.js的文件可以相互调用，Node.js提供了一个简单的模块系统。<br>
模块是Node.js 应用程序的基本组成部分，文件和模块是一一对应的。换言之，一个 Node.js 文件就是一个模块，这个文件可能是JavaScript 代码、JSON 或者编译过的C/C++ 扩展。

## 自定义模块
在demo.js同级目录下创建show.js，编写模块代码
``` Javascript
// 自定义show模块
// 定义show类
function show() {
	this.name = 'user';
	this.say = function(){
		console.log('my name is ' + this.name);
	}
}
module.exports = new show();
```
在demo.js文件中调用我们自定义的show模块
``` JavaScript
//调用自定义模块
const show = require('./show');
show.say();
```

# Node.js 函数
## 常用函数
``` Javascript
function show(){
	console.log('show');
}
```
## 匿名函数
``` Javascript
show = function(){
	console.log('show');
}
```

# Node.js 路由
自己写个路由，一般实际应用大多是直接用框架
``` JavaScript
const http = require('http');
const url = require('url');
cs = function(request,res){
	urlStr = request.url; //获取访问url路径字符串
	urlPath = url.parse(urlStr).pathname; //转换url路径
	res.writeHead('200',{'content-type':'text/html;charset=utf-8'});
	switch (urlPath) { //选择页面
		case '/index':
			res.write('index page');
			break;
		case '/add':
			res.write('add page');
			break;
		case '/delete':
			res.write('delete page');
			break;
		case '/update':
			res.write('update page');
			break;
		case '/sreach':
			res.write('sreach');
			break;
		default:
			res.write('undefined page');
	}	
	console.log("访问的url路径:"+urlPath);
	res.end();
}
http.createServer(cs).listen(666);
console.log('Server Is Running Successfully!');
```
![路由](http://i.imgur.com/NAGU7hj.png)
# Node.js 全局对象
## __filename
本文件全路径<br>
`console.log(__filename);`<br>
输出：D:\NodeWorkSpace\demo.js
## __dirname
表示当前执行脚本所在的目录。<br>
`console.log(__dirname);`<br>
输出：D:\NodeWorkSpace
## console
1. `console.log` 向标准输出流打印字符并以换行符结束
2. `console.info` 该命令的作用是返回信息性消息，这个命令与console.log差别并不大，除了在chrome中只会输出文字外，其余的会显示一个蓝色的惊叹号。
3. `console.warn` 输出警告消息。控制台出现有黄色的惊叹号。
4. `console.error` 输出错误消息的。控制台在出现错误时会显示是红色的叉子。
5. `console.time`输出时间，表示计时开始。
6. `console.timeEnd`结束时间，表示计时结束

``` javascript
console.log("log");
console.info("information");
console.warn("warn");
console.error("error");
console.time('x');
for (var i = 0; i <= 100000; i++) {
	
}
console.timeEnd('x');
```
![console](http://i.imgur.com/pMfXeKB.png)
## process
### 属性
1. `stdout` 标准输出流。
2. `stderr` 标准错误流。
3. `stdin` 标准输入流。
4. `argv` argv 属性返回一个数组，由命令行执行脚本时的各个参数组成。它的第一个成员总是node，第二个成员是脚本文件名，其余成员是脚本文件的参数。
5. `execPath` 返回执行当前脚本的 Node 二进制文件的绝对路径。
6. `execArgv` 返回一个数组，成员是命令行下执行脚本时，在Node可执行文件与脚本文件之间的命令行参数。
7. `env` 返回一个对象，成员为当前 shell 的环境变量
8. `exitCode` 进程退出时的代码，如果进程优通过 process.exit() 退出，不需要指定退出码。
9. `version` Node 的版本，比如v0.10.18。
10. `versions` 一个属性，包含了 node 的版本和依赖.
11. `config` 一个包含用来编译当前 node 执行文件的 javascript 配置选项的对象。它与运行 ./configure 脚本生成的 "config.gypi" 文件相同。
12. `pid` 当前进程的进程号。
13. `title` 进程名，默认值为"node"，可以自定义该值。
14. `arch` 当前 CPU 的架构：'arm'、'ia32' 或者 'x64'。
15. `platform` 运行程序所在的平台系统 'darwin', 'freebsd', 'linux', 'sunos' 或 'win32'
16. `mainModule` require.main 的备选方法。不同点，如果主模块在运行时改变，require.main可能会继续返回老的模块。可以认为，这两者引用了同一个模块。

### 方法
1. `abort()` 这将导致 node 触发 abort 事件。会让 node 退出并生成一个核心文件。
2. `chdir(directory)` 改变当前工作进程的目录，如果操作失败抛出异常。
3. `cwd()` 返回当前进程的工作目录
4. `exit([code])` 使用指定的 code 结束进程。如果忽略，将会使用 code 0。
5. `getgid()` 获取进程的群组标识（参见 getgid(2)）。获取到得时群组的数字 id，而不是名字。
6. 注意：这个函数仅在 POSIX 平台上可用(例如，非Windows 和 Android)。
7. `setgid(id)` 设置进程的群组标识（参见 setgid(2)）。可以接收数字 ID 或者群组名。如果指定了群组名，会阻塞等待解析为数字 ID 。
8. 注意：这个函数仅在 POSIX 平台上可用(例如，非Windows 和 Android)。
9. `getuid()` 获取进程的用户标识(参见 getuid(2))。这是数字的用户 id，不是用户名。
10. 注意：这个函数仅在 POSIX 平台上可用(例如，非Windows 和 Android)。
11. `setuid(id)` 设置进程的用户标识（参见setuid(2)）。接收数字 ID或字符串名字。果指定了群组名，会阻塞等待解析为数字 ID 。
12. 注意：这个函数仅在 POSIX 平台上可用(例如，非Windows 和 Android)。
13. `getgroups()` 返回进程的群组 iD 数组。POSIX 系统没有保证一定有，但是 node.js 保证有。
14. 注意：这个函数仅在 POSIX 平台上可用(例如，非Windows 和 Android)。
15. `setgroups(groups)` 设置进程的群组 ID。这是授权操作，所有你需要有 root 权限，或者有 CAP_SETGID 能力。
16. 注意：这个函数仅在 POSIX 平台上可用(例如，非Windows 和 Android)。
17. `initgroups(user, extra_group)` 读取 /etc/group ，并初始化群组访问列表，使用成员所在的所有群组。这是授权操作，所有你需要有 root 权限，或者有 CAP_SETGID 能力。
18. 注意：这个函数仅在 POSIX 平台上可用(例如，非Windows 和 Android)。
19. `kill(pid[, signal])` 发送信号给进程. pid 是进程id，并且 signal 是发送的信号的字符串描述。信号名是字符串，比如 'SIGINT' 或 'SIGHUP'。如果忽略，信号会是 'SIGTERM'。
20. `memoryUsage()` 返回一个对象，描述了 Node 进程所用的内存状况，单位为字节。
21. `nextTick(callback)` 一旦当前事件循环结束，调用回到函数。
22. `umask([mask])` 设置或读取进程文件的掩码。子进程从父进程继承掩码。如果mask 参数有效，返回旧的掩码。否则，返回当前掩码。
23. `uptime()` 返回 Node 已经运行的秒数。
24. `hrtime()` 返回当前进程的高分辨时间，形式为 [seconds, nanoseconds]数组。它是相对于过去的任意事件。该值与日期无关，因此不受时钟漂移的影响。主要用途是可以通过精确的时间间隔，来衡量程序的性能。你可以将之前的结果传递给当前的 process.hrtime() ，会返回两者间的时间差，用来基准和测量时间间隔。

### 示例
``` JavaScript
version = process.version;
console.log(version);
cwd = process.cwd();
console.log(cwd);
```
输出：
v6.11.0
D:\NodeWorkSpace

# Node.js 常用工具
1. ### `util.inspect` 将任意对象转换 为字符串
``` JavaScript
// 加载模块
const util = require('util');
obj = {'name':'Gavin','sex':'male','age':'16'}
console.log(typeof(obj));
console.log(util.inspect(obj));
console.log(typeof(util.inspect(obj)));
```
> 输出：
object
{ name: 'Gavin', sex: 'male', age: '16' }
string
2. ### `util.isArray();` 判断是否是数组
```JavaScript
// 加载模块
const util = require('util');
arr = ['a','b','c'];
console.log(util.isArray(arr));
```
>输出：true
3. ### `util.isBoolean();` 判断是否是boolean类型的
``` JavaScript
// 加载模块
const util = require('util');
obj = {'name':'Gavin','sex':'male','age':'16'}
console.log(util.isBoolean(obj));
```
>输出：false
4. ### `util.isDate();` 判断是否是日期
``` JavaScript
// 加载模块
const util = require('util');
tobj = new Date();
console.log(util.isDate(tobj))
```
>输出：true
5. ### `util.isFunction();` 判断是否是函数
6. ### `util.isObject();` 判断是否是对象
7. ### `util.isRegExp();` 是否是正则对象
``` JavaScript
// 加载模块
const util = require('util');
console.log(util.isRegExp(/^\d{11}$/ig));
```
>输出：true


``` JavaScript

```