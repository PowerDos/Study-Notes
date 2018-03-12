"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const fs = require("fs");
const Router = require("koa-router");
const router = new Router;
function loader() {
    const dirs = fs.readdirSync(__dirname + '/router');
    // 遍历所有的router文件
    dirs.forEach(filename => {
        const mod = require(__dirname + '/router/' + filename).default;
        // 将路由文件中的路由及方法挂在到router上
        Object.keys(mod).map(key => {
            const [method, path] = key.split(' '); // 分出方式和路由路径
            const handler = mod[key]; // 路由对应的执行方法
            router[method](path, handler); // 挂载到router
        });
    });
    return router.routes();
}
exports.loader = loader;
