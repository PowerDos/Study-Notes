"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const baseController_1 = require("./baseController");
// 继承BaseController
class UserController extends baseController_1.default {
    async index() {
        this.ctx.body = 'My Home Page';
    }
    async setting() {
        this.ctx.body = 'My Setting Page';
    }
}
exports.default = UserController;
