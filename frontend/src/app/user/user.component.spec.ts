import { ComponentFixture, TestBed, fakeAsync, tick } from '@angular/core/testing';
import { UserComponent } from './user.component';
import { PetCareService } from '../pet-care.service';
import { ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { of, throwError } from 'rxjs';

describe('UserComponent', () => {
  let component: UserComponent;
  let fixture: ComponentFixture<UserComponent>;
  let mockPetCareService: jasmine.SpyObj<PetCareService>;
  let mockRouter: any;

  beforeEach(async () => {
    mockPetCareService = jasmine.createSpyObj('PetCareService', [
      'getUserProfile',
      'updateUserProfile'
    ]);

    mockRouter = jasmine.createSpyObj('Router', ['navigate']);

    await TestBed.configureTestingModule({
      imports: [
        ReactiveFormsModule,
        HttpClientTestingModule,
        UserComponent
      ],
      providers: [
        { provide: PetCareService, useValue: mockPetCareService },
        { provide: Router, useValue: mockRouter }
      ]
    }).compileComponents();
  });

  beforeEach(() => {
    mockPetCareService.getUserProfile.and.returnValue(of({
      first_name: 'Jane',
      last_name: 'Doe',
      email: 'jane@example.com',
      phone: '1234567890',
      address: '123 Main St'
    }));

    mockPetCareService.updateUserProfile.and.returnValue(of({}));

    fixture = TestBed.createComponent(UserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  it('should initialize form with controls and disabled email', () => {
    expect(component.userProfileForm).toBeDefined();
    expect(component.userProfileForm.controls['first_name']).toBeDefined();
    expect(component.userProfileForm.get('email')?.disabled).toBeTrue();
  });

  it('should patch form with profile data on load', () => {
    expect(mockPetCareService.getUserProfile).toHaveBeenCalled();
    expect(component.userProfileForm.value.first_name).toBe('Jane');
  });

  it('should log error if getUserProfile fails', fakeAsync(() => {
    const errorSpy = spyOn(console, 'error');
    mockPetCareService.getUserProfile.and.returnValue(
      throwError(() => new Error('Load error'))
    );

    component.loadUserProfile();
    tick();

    expect(errorSpy).toHaveBeenCalledWith('Error retrieving user profile: ', jasmine.any(Error));
  }));

  it('should not call updateUserProfile if form is invalid', () => {
    component.userProfileForm.controls['first_name'].setValue('');
    component.onUpdate();

    expect(mockPetCareService.updateUserProfile).not.toHaveBeenCalled();
  });

  it('should call updateUserProfile with correct data', fakeAsync(() => {
    const validData = {
      first_name: 'Jane',
      last_name: 'Doe',
      email: 'jane@example.com',
      phone: '1234567890',
      address: '123 Main St'
    };

    component.userProfileForm.setValue(validData);
    component.onUpdate();
    tick();

    expect(mockPetCareService.updateUserProfile).toHaveBeenCalledWith(validData);
  }));

  it('should log error if updateUserProfile fails', fakeAsync(() => {
    const errorSpy = spyOn(console, 'error');
    mockPetCareService.updateUserProfile.and.returnValue(
      throwError(() => new Error('Update error'))
    );

    const formValues = {
      first_name: 'Jane',
      last_name: 'Doe',
      email: 'jane@example.com',
      phone: '1234567890',
      address: '123 Main St'
    };

    component.userProfileForm.setValue(formValues);
    component.onUpdate();
    tick();

    expect(errorSpy).toHaveBeenCalledWith('Error updating profile:', jasmine.any(Error));
  }));
});
