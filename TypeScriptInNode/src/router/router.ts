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