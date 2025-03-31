import { Component, OnInit } from '@angular/core';
import { PetCareService } from '../pet-care.service';

type User = {
  email: string;
  first_name: string;
  last_name: string;
  phone: string;
}

@Component({
  selector: 'app-main-dashboard',
  standalone: false,
  templateUrl: './main-dashboard.component.html',
  styleUrl: './main-dashboard.component.css'
})
export class MainDashboardComponent implements OnInit{

  constructor(private petCareService: PetCareService){}

  pets: object[] = []

  users: User[] = []


  ngOnInit(): void {
    this.getPets();
  }

  getPets() {
    this.petCareService.getPets().subscribe({
      next: (response) => {
        console.log("list of pets received from backend: ", response);
        this.pets = response;
        
      }
    })
  }

  



  

}
