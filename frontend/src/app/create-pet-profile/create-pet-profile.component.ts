import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

type PetProfile = {
  petSpecies: string;
  otherPetSpecies?: string;
  petName: string;
  age: number;
  breed: string;
  sex: string;
  color: string;
  microchip?: string;
  vetName: string;
  illnesses: string;
  medications: string;
};

@Component({
  selector: 'app-create-pet-profile',
  templateUrl: './create-pet-profile.component.html',
  styleUrls: ['./create-pet-profile.component.css'],
  standalone: false
})

export class PetProfileComponent implements OnInit {
  petProfileForm!: FormGroup;
  displayMessage = false;

  ngOnInit(): void {
    this.petProfileForm = new FormGroup({
      petSpecies: new FormControl('', Validators.required),
      otherPetSpecies: new FormControl(''),
      petName: new FormControl('', Validators.required),
      age: new FormControl('', [Validators.required, Validators.min(0)]),
      breed: new FormControl('', Validators.required),
      sex: new FormControl('', Validators.required),
      color: new FormControl('', Validators.required),
      microchip: new FormControl(''), // Optional field
      vetName: new FormControl('', ),
      illnesses: new FormControl('', ),
      medications: new FormControl('',),
    });
  }

  // Declare the method for the 'change' event
  onPetSpeciesChange(event: any): void {
    const selectedSpecies = event.target.value;
    const otherPetSpeciesControl = this.petProfileForm.get('otherPetSpecies');
    
    if (selectedSpecies === 'Other') {
      // If 'Other' is selected, make the text input required
      otherPetSpeciesControl?.setValidators(Validators.required);
    } else {
      // For all other selections, clear validators and reset the field
      otherPetSpeciesControl?.clearValidators();
      otherPetSpeciesControl?.setValue('');
    }
    // Update the validation state immediately
    otherPetSpeciesControl?.updateValueAndValidity();
  }

  onSubmit() {
    
      console.log('Pet profile form: ', this.petProfileForm.value);
      this.displayMessage = true;
    
  }
}