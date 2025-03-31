import { Component, OnInit } from '@angular/core';
import { PetCareService } from '../pet-care.service';

type User = {
  email: string;
  first_name: string;
  last_name: string;
  phone: string;
}

type Pet = {
  age: string;
  breed: string;
  gender: string;
  name: string;
  owners: any[];
  pet_id: number;
  profile_picture: any;
  species: string;
  weight: string;
}

@Component({
  selector: 'app-main-dashboard',
  standalone: false,
  templateUrl: './main-dashboard.component.html',
  styleUrl: './main-dashboard.component.css'
})
export class MainDashboardComponent implements OnInit{

  constructor(private petCareService: PetCareService){}

  pet!: Pet;

  users: User[] = []


  ngOnInit(): void {
    this.getPets();
  }

  getPets() {
    this.petCareService.getPets().subscribe({
      next: (response) => {
        console.log("Pet received from backend: ", response);
        this.pet = response;
        console.log("this.pet", this.pet);
        
      }
    })
  }

  



  

}
