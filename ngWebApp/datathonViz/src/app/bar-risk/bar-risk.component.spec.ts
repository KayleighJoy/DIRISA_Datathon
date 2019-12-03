import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BarRiskComponent } from './bar-risk.component';

describe('BarRiskComponent', () => {
  let component: BarRiskComponent;
  let fixture: ComponentFixture<BarRiskComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BarRiskComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BarRiskComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
