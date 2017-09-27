import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-father',
    templateUrl: './father.component.html',
    styleUrls: ['./father.component.css']
})
export class FatherComponent implements OnInit {
    private sendChildData: string;
    constructor() {
        this.sendChildData = '这是父组件的值';
    }
    fatherFun() {
        alert('这是父组件的方法');
    }
    revChildData(e) {
        alert('这是父组件，接收到子组件的值为: ' + e);
    }
    ngOnInit() {
    }

}
