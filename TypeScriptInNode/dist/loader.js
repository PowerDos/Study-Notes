"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const fs = require("fs");
const Router = require("koa-router");
class Loader {
    constructor() {
        this.router = new Router;
        this.controller = {};
    }
    /**
     * 加载控制器
     */
    loadController() {
        const dirs = fs.readdirSync(__dirname + '/controller');
        // 遍历所有controller文件
        dirs.forEach(filename => {
            const property = filename.split('.')[0]; // 读取控制器名字
            let mod = require(`${__dirname}/controller/${filename}`).default; // 导入控制器
            if (mod) {
                // 读取控制器中的所有属性
                const methodNames = Object.getOwnPropertyNames(mod.prototype).filter(names => {
                    if (names !== 'constructor') {
                        return names;
                    }
                });
                // 将控制器挂在到controller上
                Object.defineProperty(this.controller, property, {
                    get() {
                        const merge = {};
                        // 遍历属性并挂在merge上
                        methodNames.forEach(name => {
                            merge[name] = {
                                type: mod,
                                methodName: name
                            };
                        });
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
        Object.keys(routers).forEach(key => {
            const [method, path] = key.split(' ');
            this.router[method](path, async (ctx) => {
                const _class = routers[key].type; // 控制器
                const handler = routers[key].methodName; // 路由对应的控制器方法
                const instance = new _class(ctx); // 实例化控制器
                instance[handler](); // 执行控制器方法
            });
        });
        return this.router.routes(); // 返回路由
    }
}
exports.Loader = Loader;
;
