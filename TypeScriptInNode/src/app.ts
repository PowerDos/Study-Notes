import * as Koa from 'koa';
import * as Router from 'koa-router';

const app = new Koa();

const route = new Router();

route.get('/', async (ctx: Koa.Context, next: Function) => {
    ctx.body = 'Hello ts-koa!!!';
});

app.use(route.routes());

app.listen(8080, '0.0.0.0', () => {
    console.log('Working');
});
