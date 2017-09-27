import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
    selector: 'app-child',
    templateUrl: './child.component.html',
    styleUrls: ['./child.component.css']
})
export class ChildComponent implements OnInit {
    @Input() revFatherData: string;
    @Input() revFatherFun: any;
    @Output() sendMsgToFather = new EventEmitter();
    constructor() { }
    ngOnInit() {
    }
    childFun() {
        // 可传值可不传
        this.sendMsgToFather.emit('这是子组件发来的值');
    }
}
