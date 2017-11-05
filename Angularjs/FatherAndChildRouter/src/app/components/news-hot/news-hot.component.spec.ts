import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewsHotComponent } from './news-hot.component';

describe('NewsHotComponent', () => {
  let component: NewsHotComponent;
  let fixture: ComponentFixture<NewsHotComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewsHotComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewsHotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
