"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Koa = require("koa");
const loader_1 = require("./loader");
const app = new Koa();
app.use(loader_1.loader());
app.listen(8080, '0.0.0.0', () => {
    console.log('Working');
});
