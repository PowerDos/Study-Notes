"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const index = async (ctx, next) => {
    ctx.body = 'Welcome';
};
const myPage = async (ctx, next) => {
    ctx.body = 'My Home Page';
};
exports.default = {
    'get /': index,
    'get /mypage': myPage
};
