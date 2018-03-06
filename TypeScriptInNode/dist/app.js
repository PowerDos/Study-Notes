"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Koa = require("koa");
const Router = require("koa-router");
const app = new Koa();
const route = new Router();
route.get('/', async (ctx, next) => {
    ctx.body = 'Hello ts-koa!!!';
});
app.use(route.routes());
app.listen(8080, '0.0.0.0', () => {
    console.log('Working');
});
