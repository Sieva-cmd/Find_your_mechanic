import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EndfooterComponent } from './endfooter.component';

describe('EndfooterComponent', () => {
  let component: EndfooterComponent;
  let fixture: ComponentFixture<EndfooterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EndfooterComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EndfooterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
