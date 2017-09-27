import { Component, OnInit } from '@angular/core';
import { StorageService } from '../../services/storage.service';

@Component({
    selector: 'app-to-do-list',
    templateUrl: './to-do-list.component.html',
    styleUrls: ['./to-do-list.component.css']
})
export class ToDoListComponent implements OnInit {
    protected list: any[];
    protected toDoThing: any;
    constructor(private storage: StorageService) {
        this.list = [];
        this.toDoThing = '';
    }
    // 键盘松开的事件
    keyUpFunc(e) {
        if (e.keyCode === 13) {
            const obj = {
                toDoThing: this.toDoThing,
                status: 1
            }
            this.list.push(obj);
            this.storage.setItem('todolist', this.list);
            this.toDoThing = '';
        }
    }

    changeStatus(index) {
        this.list[index].status = 0;
        this.storage.setItem('todolist', this.list);
    }

    deleteThing(index) {
        this.list.splice(index, 1);
        this.storage.setItem('todolist', this.list);
    }
    ngOnInit() {
        const todolist = this.storage.getItem('todolist');
        if (todolist) {
            this.list = todolist;
        }
    }

}

