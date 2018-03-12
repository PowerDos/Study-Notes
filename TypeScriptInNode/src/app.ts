"use strict";
import * as Koa from 'koa';
import { loader } from './loader';

const app = new Koa();

app.use(loader());

app.listen(8080, '0.0.0.0', () => {
    console.log('Working');
});
