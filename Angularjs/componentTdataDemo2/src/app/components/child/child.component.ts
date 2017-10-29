import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-child',
    templateUrl: './child.component.html',
    styleUrls: ['./child.component.css']
})
export class ChildComponent implements OnInit {

    public msg:String;
    constructor() { 
        this.msg = "这是子组件的数据"
    }

    ngOnInit() {
    }

    childFunc(){
        alert('这是子组件的方法');
    }
}
