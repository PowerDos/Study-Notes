import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { NewsComponent } from './components/news/news.component';
import { NewsDetailComponent } from './components/news-detail/news-detail.component';
import { NewsContentComponent } from './components/news-content/news-content.component';

const routes: Routes = [
    {
        path: "home",
        component: HomeComponent
    },
    {
        path: "news",
        component: NewsComponent
    },
    {
        path: "newsdetail/:id",
        component: NewsDetailComponent
    },
    {
        path: "newscontent",
        component: NewsContentComponent
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
