# Express
> Express 是一个基于 Node.js 平台的极简、灵活的 web 应用开发框架，它提供一系列强大的特性，帮助你创建各种 Web 和移动设备应用。

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