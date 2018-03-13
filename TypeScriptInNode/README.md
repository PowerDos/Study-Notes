# 用 TypeScript + Koa2 封装 Node 企业框架

> 因为一直用纯javascript写后台，即使用了egg这种企业框架，当系统庞大的时候，用纯脚本编写的系统，后期维护起来还是相当麻烦的，还有可能导致**上线火葬场**的情况。我会在每一个小阶段提交一个版本, 学习文档《使用Typescript封装一款基础企业级Web框架》--方正

#### 目录
 - [用 TypeScrpt 编写一个基于 Koa2 的简单WEB应用](#用-typescrpt-编写一个基于-koa2-的简单web应用)
 - [拆分路由](#拆分路由)
 - [引入控制器](#引入控制器)

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

## 拆分路由
> 提交程序版本： [拆分路由](https://github.com/PowerDos/Study-Notes/commit/2059c39313756f695424c85d3b8ad220a9946b61)

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


## 引入控制器
> 我们看看现在，我们添加新接口时，我们都要在这个文件添加路由和对应的相应，耦合程度太高，如果代码量大了，就很难去维护。


> 提交程序版本: [引入控制器](https://github.com/PowerDos/Study-Notes/commit/8ac2d93ddc57644e931194ac0559c7d7ea706b50) 


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
#### 为什么引入控制器
> 把路由和路由的具体实现分开，我们这样就可以更加专注的开发业务实现过程，我们如果有新的接口要写，只需要在对应的控制器写业务流程，并映射到对应的路由。

#### 分离出控制器
> 因为每次请求, koa都会生成ctx(上下文), 我们把它加到控制器的属性中, 这样方便业务流程处理时调用ctx, 直接用this.ctx就可以调用。我们这里先写个基类BaseController, 后面直接继承就好, 避免太多重复性代码。

```typescript
import { BaseContext } from "koa";

export default class BaseController {
    ctx: BaseContext;

    constructor(ctx: BaseContext) {
        this.ctx = ctx;
    }
}
```

> 开始写我们的控制类

```typescript
import  BaseController  from './baseController';

// 继承BaseController
export default class UserController extends BaseController {
    async index() {
        this.ctx.body = 'My Home Page';
    }

    async setting() {
        this.ctx.body = 'My Setting Page';
    }
}
```

#### 改写路由
> 我们因为把业务逻辑和路由分离，我们不用在路由文件中写太多代码，所以我们把router目录删除，直接把router文件提取到外面，改写成下面的样子

```typescript
export default (controller: any) => {
    return {
        'get /': controller.home.index,
        'get /mypage': controller.user.index,
        'get /mysetting': controller.user.setting
    }
}
```

#### 改写loader文件
> 现在我们改写loader文件，达到自动加载路由，自动映射到路由上，具体实现如下

```typescript
import * as fs from 'fs';
import * as Router from 'koa-router';
import { BaseContext } from 'koa';

export class Loader {
    router: Router = new Router;
    controller: any = {};

    /**
     * 加载控制器
     */
    loadController() {
        const dirs = fs.readdirSync(__dirname + '/controller');
        // 遍历所有controller文件
        dirs.forEach(filename => {
            const property = filename.split('.')[0];                          // 读取控制器名字
            let mod = require(`${__dirname}/controller/${filename}`).default; // 导入控制器
            if (mod) {
                // 读取控制器中的所有属性
                const methodNames = Object.getOwnPropertyNames(mod.prototype).filter(names => {
                    if (names !== 'constructor') {  // 过滤掉构造器constructor
                        return names;
                    }
                });
                // 将控制器挂在到controller上
                Object.defineProperty(this.controller, property, {
                    get() {
                        const merge: { [key: string]: any } = {};
                        // 遍历属性并挂在merge上
                        methodNames.forEach(name => {
                            merge[name] = {
                                type: mod,
                                methodName: name
                            }
                        })
                        return merge;
                    }
                });
            }
        });
    }

    /**
     * 加载路由
     */
    loadRouter() {
        this.loadController();
        const mod = require(`${__dirname}/router`).default;
        const routers = mod(this.controller);
        Object.keys(routers).forEach( key => {
            const [method, path] = key.split(' ');
            (<any>this.router)[method](path, async (ctx: BaseContext) => {
                const _class = routers[key].type;        // 控制器
                const handler = routers[key].methodName; // 路由对应的控制器方法
                const instance = new _class(ctx);        // 实例化控制器
                instance[handler]();                     // 执行控制器方法
            });
        });

        return this.router.routes(); // 返回路由
    }
};
```

#### 更改app.ts文件，开启控制器新姿势
```typescript
import * as Koa from 'koa';
import { Loader } from './loader';

const app = new Koa();
const loader = new Loader();

app.use(loader.loadRouter());

app.listen(8080, '0.0.0.0', () => {
    console.log('Working');
});
```
#### 现在的目录解构
```
│  nodemon.json
│  package-lock.json
│  package.json
│  README.md
│  tsconfig.json
│
├─dist
│  │  app.js
│  │  loader.js
│  │  router.js
│  │
│  ├─controller
│  │      baseController.js
│  │      home.js
│  │      user.js
│  │
│  └─router
│          router.js
│
├─node_modules
└─src
    │  app.ts
    │  loader.ts
    │  router.ts
    │
    └─controller
            baseController.ts
            home.ts
            user.ts
```

#### 小结
> 有了控制器后，我们只需要在controller目录下专注的写好实现过程，再挂载到路由上，这样就实现了解耦，更加规范开发，方便后期维护。**值得注意的是，每一次请求我们都会重新构建controller对象，因为每次独立的请求都需要新的ctx(上下文)**

