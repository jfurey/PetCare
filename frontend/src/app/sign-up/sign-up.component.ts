import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { PetCareService } from '../pet-care.service';

type  User = {
  firstName: string,
  lastName: string,
  email: string
}

@Component({
  selector: 'app-sign-up',
  standalone: false,
  templateUrl: './sign-up.component.html',
  styleUrl: './sign-up.component.css'
})
export class SignUpComponent implements OnInit {

  constructor(private petCareService: PetCareService) {}

  signUpForm!: FormGroup;
  displayMessage = false;

  ngOnInit(): void {

    this.signUpForm = new FormGroup({
      first_name: new FormControl('', Validators.required),
      last_name: new FormControl ('', Validators.required),
      email: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required)
    })

    
    
  }

  onSubmit() {
    this.signUpForm.value;
    console.log(this.signUpForm.value);
    this.displayMessage = true;
    this.petCareService.addUser(this.signUpForm.value).subscribe({
      next: (response) => {
        console.log('Response from adding new user: ', response);
        
      }, 
      error: (error) => {
        console.log("Error addng user: ", error);
        
      }
    })
  }

}
