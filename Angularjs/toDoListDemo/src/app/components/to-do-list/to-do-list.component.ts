import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-to-do-list',
    templateUrl: './to-do-list.component.html',
    styleUrls: ['./to-do-list.component.css']
})
export class ToDoListComponent implements OnInit {
    protected list: any[];
    protected toDoThing: any;
    constructor() {
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
            this.toDoThing = '';
        }
    }

    changeStatus(index) {
        this.list[index].status = 0;
    }

    deleteThing(index) {
        this.list.splice(index, 1);
    }
    ngOnInit() {
    }

}
