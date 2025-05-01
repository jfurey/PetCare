import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ReactiveFormsModule } from '@angular/forms';
import { PetProfileComponent } from './create-pet-profile.component';

describe('PetProfileComponent', () => {
  let component: PetProfileComponent;
  let fixture: ComponentFixture<PetProfileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [PetProfileComponent],
      imports: [ReactiveFormsModule]
    }).compileComponents();

    fixture = TestBed.createComponent(PetProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  it('should initialize form with default values in ngOnInit', () => {
    component.ngOnInit();
    expect(component.petProfileForm).toBeDefined();
    expect(component.petProfileForm.get('petSpecies')?.value).toBe('');
  });

  it('should set required validator when pet species is "Other"', () => {
    component.ngOnInit();
    const mockEvent = { target: { value: 'Other' } };
    component.onPetSpeciesChange(mockEvent);

    const control = component.petProfileForm.get('otherPetSpecies');
    expect(control?.validator).toBeTruthy();
  });

  it('should clear validator when pet species is not "Other"', () => {
    component.ngOnInit();
    const control = component.petProfileForm.get('otherPetSpecies');
    control?.setValidators(() => null); // force validator
    const mockEvent = { target: { value: 'Dog' } };
    component.onPetSpeciesChange(mockEvent);

    expect(control?.validator).toBeNull();
  });

  it('should set displayMessage to true on submit', () => {
    component.ngOnInit();
    component.petProfileForm.patchValue({
      petSpecies: 'Dog',
      petName: 'Buddy',
      age: 3,
      breed: 'Labrador',
      sex: 'Male',
      color: 'Black',
      vetName: 'Dr. Smith',
      illnesses: 'None',
      medications: 'None'
    });

    component.onSubmit();
    expect(component.displayMessage).toBeTrue();
  });

  it('should disable submit button if form is invalid', () => {
    // Initialize the form
    component.ngOnInit();
    
    // Set petSpecies and petName as empty, making the form invalid
    component.petProfileForm.patchValue({
      petSpecies: '',
      petName: ''
    });

    fixture.detectChanges(); // Trigger change detection

    const submitButton = fixture.debugElement.nativeElement.querySelector('button');
    
    // Check if the submit button is disabled when form is invalid
    expect(submitButton.disabled).toBeTrue();
  });
});
