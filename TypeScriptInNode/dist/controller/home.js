"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const baseController_1 = require("./baseController");
// 继承BaseController
class HomeController extends baseController_1.default {
    async index() {
        this.ctx.body = 'Welcome';
    }
}
exports.default = HomeController;
