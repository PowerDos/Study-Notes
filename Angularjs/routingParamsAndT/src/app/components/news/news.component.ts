import { Component, OnInit } from '@angular/core';
import { Router, NavigationExtras } from '@angular/router';

@Component({
    selector: 'app-news',
    templateUrl: './news.component.html',
    styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {

    constructor(private router: Router) { }

    ngOnInit() {
    }

    goto(id){
        // JS跳转，主要用于业务逻辑的处理后的跳转
        // routerLink 主要用于前台直接点击跳转
        this.router.navigate(['/newsdetail', id]);
    }
    getTo(id, name){
        // get传值
        // 配置参数
        let navigationExtras: NavigationExtras = {
            queryParams: {
                "id": id,
                "name": name
            }
        }
        this.router.navigate(['/newscontent'], navigationExtras);
    }
}
