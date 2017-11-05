import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { NewsComponent } from './components/news/news.component';
import { NewsTopComponent } from './components/news-top/news-top.component';
import { NewsHotComponent } from './components/news-hot/news-hot.component';
import { NewsListComponent } from './components/news-list/news-list.component';
import { WelcomeComponent } from './components/welcome/welcome.component';

const routes: Routes = [
    {
        path: "home",
        component: HomeComponent,
        children: [  // 子路由写在这里
            {
                path: "welcome",
                component: WelcomeComponent
            },
            {
                path: "**",
                component: WelcomeComponent
            }
        ]
    },
    {
        path: "news",
        component: NewsComponent,
        children: [
            {
                path: "newstop",
                component: NewsTopComponent
            },
            {
                path: "newshot",
                component: NewsHotComponent
            },
            {
                path: "newslist",
                component: NewsListComponent
            },
            {
                path: "**",
                component: NewsHotComponent
            }
        ]
    },
    {
        path: "**",
        component: HomeComponent
    }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
