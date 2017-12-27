import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-child',
    templateUrl: './child.component.html',
    styleUrls: ['./child.component.css']
})
export class ChildComponent implements OnInit {

    constructor() { }

    ngOnInit() {
    }

    chlidRun() {
        alert('这是子组件的Run方法');
    }
}
