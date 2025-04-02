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
      vetName: new FormControl('', Validators.required),
      illnesses: new FormControl('', Validators.required),
      medications: new FormControl('', Validators.required),
    });
  }

  // Declare the method for the 'change' event
  onPetSpeciesChange(event: any): void {
    const selectedSpecies = event.target.value;
    if (selectedSpecies === 'Other') {
      // Logic to show a text input for the 'Other' species
      // For example, set a flag or do something specific for the 'Other' option
      this.petProfileForm.get('otherPetSpecies')?.setValidators(Validators.required);
    } else {
      // If not 'Other', clear the value or reset validators for 'otherPetSpecies'
      this.petProfileForm.get('otherPetSpecies')?.setValue('');
      this.petProfileForm.get('otherPetSpecies')?.clearValidators();
    }
  }

  onSubmit() {
    if (this.petProfileForm.valid) {
      console.log(this.petProfileForm.value);
      this.displayMessage = true;
    }
  }
}
