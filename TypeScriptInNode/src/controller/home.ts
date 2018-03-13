import  BaseController  from './baseController';

// 继承BaseController
export default class HomeController extends BaseController {
    async index() {
        this.ctx.body = 'Welcome';
    }
}