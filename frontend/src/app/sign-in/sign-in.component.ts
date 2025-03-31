import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { PetCareService } from '../pet-care.service';

type User = {
  email: string;
  first_name: string;
  last_name: string;
  phone: string;
}

@Component({
  selector: 'app-sign-in',
  standalone: false,
  templateUrl: './sign-in.component.html',
  styleUrl: './sign-in.component.css'
})
export class SignInComponent implements OnInit {
  userExists = false;

  constructor(private router:Router, private petCareService: PetCareService){}

  loginForm!: FormGroup;

  ngOnInit(): void {
    this.loginForm = new FormGroup({
      username: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required),
    })
   
  }

  onSubmit(){
    this.loginForm.value;
    console.log(this.loginForm.value);

    this.checkExistentUsers();

  }

  goToSignUp(){
    this.router.navigate(['sign-up']);
  }

  goToMainDashboard(){
    this.router.navigate(['main-dashboard']);
  }

  checkExistentUsers() {
    this.petCareService.getUsers().subscribe({
      next: (response) => {
        console.log('Users: ', response);
        const users : User[] = response;
        for( let user of users) {
          console.log("user: ", user.email);
          console.log("loginForm username: ", this.loginForm.controls['username'].value);
          
          if (user.email.toLowerCase()===this.loginForm.controls['username'].value) {
            this.userExists = true;
            break;
            
          }
        }
        if (this.userExists == true) {
          console.log('User already exists');
          this.loginForm.reset();
          this.userExists = false;
        }
        else {
          this.goToMainDashboard();
        }
      
      },
      error: (error) => {
        console.log('Error retrieving users: ', error);
        
      }
    })
  }

}
