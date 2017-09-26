import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-news',
    templateUrl: './news.component.html',
    styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {
    public title: string;
    public content: string;
    public id: string;
    constructor() {
        this.title = '这是新闻标题';
        this.content = '<h3> 这是新闻内容 <h3>';
        this.id = 'news';
    }

    ngOnInit() {
    }

}
