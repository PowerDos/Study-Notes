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

### 拆分路由
#### 目前的应用代码
``` typescript
import * as Koa from 'koa';
import * as Router from 'koa-router';

const app = new Koa();

const route = new Router();

route.get('/', async (ctx: Koa.Context, next: Function) => {
    ctx.body = 'Welcome';
});

route.get('/mypage', async (ctx: Koa.Context, next: Function) => {
    ctx.body = 'My Home Page';
})

app.use(route.routes());

app.listen(8080, '0.0.0.0', () => {
    console.log('Working');
});
```
#### 为什么拆分路由
> 你会发现，如果我们有很多路由的话，我们就会不断在这个文件添加代码，这样一来，如果代码量多了，会非常杂乱，后期维护起来很麻烦，所以我们把路由这一块拆分出来

#### 开始拆分路由
> 我们把路由单独写在一个文件中

```typescript
import { Context } from "koa";

"use strict";

const index = async (ctx: Context, next: any) => {
    ctx.body = 'Welcome';
}

const myPage = async (ctx: Context, next: any) => {
    ctx.body = 'My Home Page';
}

export default {
    'get /': index,
    'get /mypage': myPage
}
```
> 为了解放生产力，让所有的路由文件中的路由自动加载进入，我们做一个loader专门来做加载

```typescript
import * as fs from 'fs';
import * as Router from 'koa-router';

const router = new Router;

export function loader() {
    const dirs = fs.readdirSync(__dirname + '/router');
    // 遍历所有的router文件
    dirs.forEach( filename => {
        const mod = require(__dirname + '/router/' + filename).default;
        // 将路由文件中的路由及方法挂在到router上
        Object.keys(mod).map(key => {
            const [ method, path ] = key.split(' '); // 分出方式和路由路径
            const handler = mod[key];                // 路由对应的执行方法
            (<any>router)[method](path, handler);    // 挂载到router
        });
    });

    return router.routes();
}
```

> 现在我们再改下app.ts这个文件

```typescript
"use strict";
import * as Koa from 'koa';
import { loader } from './loader';

const app = new Koa();

app.use(loader());

app.listen(8080, '0.0.0.0', () => {
    console.log('Working');
});
```
#### 现在的目录
![](https://i.imgur.com/Q7mDILs.png)

#### 小结
> 现在我们已经把路由提出去了，接下来我们需要新建页面路由，就是在router目录下，新建路由文件或者添加路由到我们现有文件router.ts中，是不是又自动化了一点。