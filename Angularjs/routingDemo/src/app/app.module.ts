import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module'; // 引入路由模块
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { NewsComponent } from './components/news/news.component';
import { AboutUsComponent } from './components/about-us/about-us.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NewsComponent,
    AboutUsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule // 导入路由模块
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
