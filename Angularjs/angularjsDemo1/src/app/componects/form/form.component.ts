import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-form',
    templateUrl: './form.component.html',
    styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {

    constructor() { }

    ngOnInit() {
    }

    keyUpFn(e) {
        if (e.keyCode === 13) {
            alert('按了回车');
        }
    }
}
