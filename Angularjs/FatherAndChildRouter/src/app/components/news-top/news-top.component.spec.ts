import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewsTopComponent } from './news-top.component';

describe('NewsTopComponent', () => {
  let component: NewsTopComponent;
  let fixture: ComponentFixture<NewsTopComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewsTopComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewsTopComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
