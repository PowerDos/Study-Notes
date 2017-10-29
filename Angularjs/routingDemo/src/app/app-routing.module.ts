import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// 引入组件
import { HomeComponent } from './components/home/home.component';
import { NewsComponent } from './components/news/news.component';
import { AboutUsComponent } from './components/about-us/about-us.component';

// 配置路由
const routes: Routes = [
    {
        path: 'home',
        component: HomeComponent
    },
    {
        path: 'news',
        component: NewsComponent
    },
    {
        path: 'about_us',
        component: AboutUsComponent
    },
    {
        path: '', // 无路径时，默认显示home组件
        component: HomeComponent,
        pathMatch: 'full'
    },
    {
        path: '**',  // 全部没有匹配到时，自动跳转到home
        redirectTo: 'home'
    }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
