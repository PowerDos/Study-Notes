import { Component, OnInit } from '@angular/core';
import { Routes, ActivatedRoute, Params } from '@angular/router';

@Component({
    selector: 'app-news-detail',
    templateUrl: './news-detail.component.html',
    styleUrls: ['./news-detail.component.css']
})
export class NewsDetailComponent implements OnInit {
    private id: Number;
    protected newsTitle: String;

    constructor(private router: ActivatedRoute) { }

    ngOnInit() {
        // 获取传过来的参数
        this.router.params.subscribe(data => this.id = parseInt(data.id));
        switch(this.id){
            case 1:
                this.newsTitle = "一";
                break;
            case 2:
                this.newsTitle = "二";
                break;
            case 3:
                this.newsTitle = "三";
                break;
            default:
                this.newsTitle = "五";
                break;
        }
    }

}
