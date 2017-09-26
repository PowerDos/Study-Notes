import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // 导入FormsModule

import { AppComponent } from './app.component';
import { NewsComponent } from './componects/news/news.component';
import { ForComponent } from './componects/for/for.component';
import { IfComponent } from './componects/if/if.component';
import { EventComponent } from './componects/event/event.component';
import { FormComponent } from './componects/form/form.component';
import { DataBindingComponent } from './componects/data-binding/data-binding.component';

@NgModule({
  declarations: [
    AppComponent,
    NewsComponent,
    ForComponent,
    IfComponent,
    EventComponent,
    FormComponent,
    DataBindingComponent
  ],
  imports: [
    BrowserModule,
    FormsModule  // 导入FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
