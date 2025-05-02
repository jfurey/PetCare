import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MainDashboardComponent } from './main-dashboard.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('MainDashboardComponent', () => {
  let component: MainDashboardComponent;
  let fixture: ComponentFixture<MainDashboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MainDashboardComponent],
      imports: [HttpClientTestingModule]
    }).compileComponents();

    fixture = TestBed.createComponent(MainDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
