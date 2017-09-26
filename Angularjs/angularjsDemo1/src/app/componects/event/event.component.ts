import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-event',
    templateUrl: './event.component.html',
    styleUrls: ['./event.component.css']
})
export class EventComponent implements OnInit {
    public name: string;
    public age: number;
    constructor() {
        this.name = 'Gavin';
        this.age = 18;
    }

    ngOnInit() {
    }

    getInfo() {
        alert(`姓名: ${this.name}， 年龄: ${this.age}`);
    }

    changeAge() {
        this.age = 20;
    }
}
