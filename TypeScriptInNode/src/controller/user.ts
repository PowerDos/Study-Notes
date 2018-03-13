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