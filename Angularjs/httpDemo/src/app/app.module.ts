import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule, JsonpModule } from '@angular/http'; /* 注入HTTP和jsonp依赖 */
import { AppComponent } from './app.component';
import { HttpComponent } from './components/http/http.component';
import { RxjsDemoComponent } from './components/rxjs-demo/rxjs-demo.component';

@NgModule({
  declarations: [
    AppComponent,
    HttpComponent,
    RxjsDemoComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    JsonpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
