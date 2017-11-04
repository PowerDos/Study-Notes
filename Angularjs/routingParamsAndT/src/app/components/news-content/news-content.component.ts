import { Component, OnInit } from '@angular/core';
// 接收动态传值， 接收get传值
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'app-news-content',
    templateUrl: './news-content.component.html',
    styleUrls: ['./news-content.component.css']
})
export class NewsContentComponent implements OnInit {
    protected newsName: String;

    constructor(private router: ActivatedRoute) { }

    ngOnInit() {
        let fatherThis = this;
        // 获取get传过来值
        this.router.queryParams.subscribe( data => {
            fatherThis.newsName = data.name;
        })
    }

}
