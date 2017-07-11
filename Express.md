# Express
> Express 是一个基于 Node.js 平台的极简、灵活的 web 应用开发框架，它提供一系列强大的特性，帮助你创建各种 Web 和移动设备应用。

## 目录：
1. [Install Express](#install-express) 
2. [Start Express](#start-express)
3. [中间件](#中间件) 
4. [Request](#request)
5. [GET和POST请求](#get和post请求)
	- [GET](#get)
	- [POST](#post)

# Install Express
> 安装环境：Linux<br>
> 安装Express:<br>
> 命令行输入: `npm install express -g`<br>
> 安装完如果不能直接在命令行输入express 创建express项目等，请自行建立软连接(安装在node的bin目录下)。

# Start Express 
> 1. 安装应用生成器： `npm install express-generator -g`
> 2. 创建一个应用： `express firstapp`
> 3. 进入firstapp文件夹: `cd firstapp`
> 4. 安装依赖包： `npm install`
> 5. 启动应用： `DEBUG=firstapp npm start`

# 中间件
> 中间件（Middleware） 是一个函数，它可以访问请求对象（request object (req)）, 响应对象（response object (res)）, 和 web 应用中处于请求-响应循环流程中的中间件，一般被命名为 next 的变量。<br>每个中间件可以从App实例，接收三个参数，依次为request对象（代表HTTP请求）、response对象（代表HTTP回应），next回调函数（代表下一个中间件）。每个中间件都可以对HTTP请求（request对象）进行加工，并且决定是否调用next方法，将request对象再传给下一个中间件。

```javascript
var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
	if (req.query.id == 1) {
		// 如果id等于1，则执行下一个中间件
		next();
	}else {
		// 否则结束
		res.send("结束");
	}
});

router.get('/', function(req, res, next){
	res.send("这里是第二个中间件");
});

module.exports = router;
```

> 或者可以这样写

```javascript
var express = require('express');
var router = express.Router();

const cb0 = function(req, res, next){
	if (req.query.id == 1) {
		// 如果id等于1，则执行下一个中间件
		next();
	}else {
		// 否则结束
		res.send("结束");
	}
}

const cb1 = function(req, res, next){
	res.send("这里是第二个中间件");
}

router.get('/', [cb0, cb1]);
module.exports = router;
```
> 实际效果

![只经过一个中间件](http://i.imgur.com/m9IAXHg.png)
![经过两个中间件](http://i.imgur.com/TmlUlig.png)

# Request
```javascript
var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
	// 访问地址路径 比如: /index
	console.log('req.baseUrl: ', req.baseUrl);
	// 获取cookie的值,因为没有设置cookie，就不演示
	// console.log('req.cookie: ', req.cookie.user);
	console.log('req.fresh: ', req.fresh);
	// 获取域名
	console.log('req.hostname: ', req.hostname);
	console.log('req.ip: ', req.ip);
	console.log('req.ips: ', req.ips);
	console.log('req.originalUrl: ', req.originalUrl);
	// 本中间件后的路径，比如访问localhost/index/ ,path就是/
	console.log('req.path: ', req.path);
	//访问协议
	console.log('req.protocol: ', req.protocol);
	// 是否是异步请求
	console.log('req.xhr: ', req.xhr);
	res.end(" ");
});

module.exports = router;
```
> 输出数据：<br>
> req.baseUrl:  /index<br>
> req.fresh:  false<br>
> req.hostname:  localhost<br>
> req.ip:  ::1<br>
> req.ips:  []<br>
> req.originalUrl:  /index<br>
> req.path:  /<br>
> req.protocol:  http<br>
> req.xhr:  false<br>

# GET和POST请求
## GET
> 获取url的参数<br>
> 假设url为：`http://localhost/index?id=1&name=Gavin`<br>
> 获取参数 `req.query.name`<br>
> 获取全部参数并转换为json `JSON.stringify(req.query)`<br>
> 还有一种获取方法，但在4.x版本中废除了 `req.param('name')`

```javascript
const express = require('express');
const router = express.Router();
//get方式访问
router.get('/', function(req, res, next) {
	//获取所有的get数据
	json = JSON.stringify(req.query);
	console.log("GET:"+json);
	res.send("GET:"+json);
});
module.exports = router;
```

## POST
> 假设POST过来的数据是 id=1&name=Gavin<br>
> 获取参数： `req.body.name`<br>
> 获取全部参数并转换为json： `JSON.stringify(req.body)`

```javascript
const express = require('express');
const router = express.Router();
//post方式访问
router.post('/', function(req, res, next){
	//获取所有post数据
	json = JSON.stringify(req.body);
	console.log("POST:" + json);
	res.send("POST:" + json);
});

module.exports = router;
```