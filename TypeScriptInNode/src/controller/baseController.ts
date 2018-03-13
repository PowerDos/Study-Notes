import { BaseContext } from "koa";

export default class BaseController {
    ctx: BaseContext;

    constructor(ctx: BaseContext) {
        this.ctx = ctx;
    }
}