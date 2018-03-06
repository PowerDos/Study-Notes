# 用TypeScript 封装 Node 企业框架

> 因为一直用纯javascript写后台，即使用了egg这种企业框架，当系统庞大的时候，用纯脚本编写的系统，后期维护起来还是相当麻烦的，还有可能导致**上线火葬场**的情况。我会在每一个小阶段提交一个版本, 参考文档《使用Typescript封装一款基础企业级Web框架》--方正

## 用 TypeScrpt 编写一个基于 Koa2 的简单WEB应用 
> 这里只写一些简单的步骤，详细配置和代码可以看该版本提交的程序

> 提交版本为 [用 TypeScrpt 编写一个基于 Koa2 的简单WEB应用](https://github.com/PowerDos/Study-Notes/commit/d611c33f8568d8bfce094eadceb8f7ed2cb2e914)

### 完成一个简单的WEB应用
#### 准备, 安装模块
```shell
# npm install -g typescript
# mkdir TypeScriptInNode
# cd TypeScriptInNode
# tsc -init
# npm init
# npm install --save koa
# npm install --save koa-router
# npm install --save @types/koa
# npm install --save @types/koa-router
```

#### 编写代码
```typescript
import * as Koa from 'koa';
import * as Router from 'koa-router';

const app = new Koa();

const route = new Router();

route.get('/', async (ctx: Koa.Context, next: Function) => {
    ctx.body = 'Hello ts-koa';
});

app.use(route.routes());

app.listen(8080, '0.0.0.0', () => {
    console.log('Working');
});
```

#### 打包
```shell
# tsc
```

#### 运行应用
```shell
# npm start
```

### 给应用加上自动编译TS与服务器自动重启

#### 加入nodemon
> nodemon 可以在监听文件发生变化时，自动帮我们编译重启，省去我们去编译和重启的繁琐操作。


> 安装nodemon

```shell
# npm install nodemon --save
```

> 创建nodemon配置文件，在根目录创建nodemon.json

```json
{
    "ignore": [
        "**/*.test.ts",
        "**/*.spec.ts",
        ".git",
        "node_modules"
    ],
    "watch": [
        "src"
    ],
    "exec": "npm start",
    "ext": "ts"
}
```

> 配置说明

- **ignore**：忽略的文件后缀名或者文件夹，文件路径的书写用相对于 nodemon.json 所在位置的相对路径，下同。nodemon 会默认忽略一些文件，默认忽略的文件有：.git, node_modules, bower_components, .sass-cache，如果这些文件想要加入监控，需要重写默认忽略参数字段 ignoreRoot，比如加入："ignoreRoot": [".git", "bower_components", ".sass-cache"]，然后在 watch 中将 node_modules 文件路径加入监控，那么 node_modules 内的文件也加入了监控了。
- **watch**：监控的文件夹路径或者文件路径。
- **exec**： 写的是「当你的目录改变时，执行的命令」，对于我们来说，其实就是编译+启动，这里我们写`npm start`
- **ext**：监控指定后缀名的文件，用空格间隔。默认监控的后缀文件：.js, .coffee, .litcoffee, .json。但是对于没有文件后缀的文件，比如 www 文件，我暂时找不到怎么用 nodemon 去监控，就算在 watch 中包含了，nodemon 也会忽略掉。

> package.json 中也需做相应的改变

```json
"scripts": {
    "start": "tsc && node ./dist/app.js",
    "dev": "node ./node_modules/nodemon/bin/nodemon.js"
}
```

> 启动应用

```shell
# npm run dev
```

> 启动效果

![](https://i.imgur.com/hAorldc.png)

> 目录结构

![](https://i.imgur.com/EfViPPR.png)
