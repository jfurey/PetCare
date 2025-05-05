import { Component } from '@angular/core';
import { PetCareService } from './pet-care.service'; // Make sure the path is correct

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  standalone: false,
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'myApp';

  constructor(public petCareService: PetCareService) {}
}
