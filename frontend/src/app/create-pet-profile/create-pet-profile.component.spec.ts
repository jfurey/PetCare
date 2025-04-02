import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PetProfileComponent } from './create-pet-profile.component';

describe('CreatePetProfileComponent', () => {
  let component: PetProfileComponent;
  let fixture: ComponentFixture<PetProfileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [PetProfileComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PetProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
