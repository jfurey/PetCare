import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

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

  signUpForm!: FormGroup;
  displayMessage = false;

  ngOnInit(): void {

    this.signUpForm = new FormGroup({
      firstName: new FormControl('', Validators.required),
      lastName: new FormControl ('', Validators.required),
      email: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required)
    })

    
    
  }

  onSubmit() {
    this.signUpForm.value;
    console.log(this.signUpForm.value);
    this.displayMessage = true;
  }

}
