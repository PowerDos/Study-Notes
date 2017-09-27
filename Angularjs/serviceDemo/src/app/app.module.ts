import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { ToDoListComponent } from './components/to-do-list/to-do-list.component';

import { StorageService } from './services/storage.service'; // 注册服务

@NgModule({
  declarations: [
    AppComponent,
    ToDoListComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [StorageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
