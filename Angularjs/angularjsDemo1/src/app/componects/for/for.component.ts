import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-for',
    templateUrl: './for.component.html',
    styleUrls: ['./for.component.css']
})
export class ForComponent implements OnInit {
    public list: any[];
    constructor() {
        this.list = ['苹果', '梨', '草莓', '西瓜'];
    }

    ngOnInit() {
    }

}
