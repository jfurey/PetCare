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

  showMessage = false;

  message!: string;

  constructor(private router:Router, private petCareService: PetCareService){}

  loginForm!: FormGroup;

  ngOnInit(): void {
    this.loginForm = new FormGroup({
      email: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required),
    })
   
  }

  onSubmit(){
    const credentials = this.loginForm.value;
    console.log("credentials: ", credentials);

    this.petCareService.login(credentials).subscribe({
      next: (response) => {
        console.log("Response from login: ", response);
        if(response) {
          this.goToMainDashboard();
        }
      
      },
      error: (error) => {
        this.showMessage = true;
        this.message = `Try again with legitimate credentials:\n
                        login@test.com\n
                        password: mytestpass123`;
        

      }
    })

    

  }

  goToSignUp(){
    this.router.navigate(['sign-up']);
  }

  goToMainDashboard(){
    this.router.navigate(['main-dashboard']);
  }

  checkExistentUsers(object: Object) {
    this.petCareService.login(object).subscribe({
      next: (response) => {
        console.log("Response from login: ", response);
        
      
      }
    })
  }
  //       console.log('Users: ', response);
  //       const users : User[] = response;
  //       for( let user of users) {
  //         console.log("user: ", user.email);
  //         console.log("loginForm username: ", this.loginForm.controls['username'].value);
          
  //         if (user.email.toLowerCase()===this.loginForm.controls['username'].value) {
  //           this.userExists = true;
  //           break;
            
  //         }
  //       }
  //       if (this.userExists === true) {
  //         this.goToMainDashboard();
  //         console.log('inside the userExists===true:', this.userExists);
          
          
  //       }
  //       else {
  //         this.loginForm.reset();
  //         this.userExists = false;
  //         console.log('inside the userExists===false:', this.userExists);
  //       }
      
  //     },
  //     error: (error) => {
  //       console.log('Error retrieving users: ', error);
        
  //     }
  //   })
  // }

}
