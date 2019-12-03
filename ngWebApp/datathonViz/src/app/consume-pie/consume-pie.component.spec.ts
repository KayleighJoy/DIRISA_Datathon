import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsumePieComponent } from './consume-pie.component';

describe('ConsumePieComponent', () => {
  let component: ConsumePieComponent;
  let fixture: ComponentFixture<ConsumePieComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConsumePieComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConsumePieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
