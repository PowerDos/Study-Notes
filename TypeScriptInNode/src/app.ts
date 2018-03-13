import * as Koa from 'koa';
import { Loader } from './loader';

const app = new Koa();
const loader = new Loader();

app.use(loader.loadRouter());

app.listen(8080, '0.0.0.0', () => {
    console.log('Working');
});
