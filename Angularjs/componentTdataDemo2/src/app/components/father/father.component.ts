import { Component, OnInit, ViewChild } from '@angular/core';

@Component({
    selector: 'app-father',
    templateUrl: './father.component.html',
    styleUrls: ['./father.component.css']
})
export class FatherComponent implements OnInit {

    @ViewChild('childObj') childObj;
    constructor() { }

    ngOnInit() {
    }

    fatherChangeChildData(){
        this.childObj.msg = "父组件改变后的数据";
        alert('改变完子组件的数据');
    }
}
