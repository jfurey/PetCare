import { Component, OnInit } from '@angular/core';
import { PetCareService } from '../pet-care.service';
import { FormControl, FormGroup } from '@angular/forms';

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

type PetImage = {
  age: string;
  breed: string;
  gender: string;
  name: string;
  owner_role: string;
  pet_id: number;
  profile_picture: string;
  profile_picture_url: string;
  species: string;
  weight: string;
}

type Vaccinations = {
  created_at: string;
  date_given: string;
  next_due: string; 
  pet_id: number;
  vaccination_id: number;
  vaccine_name: string;
  veterinarian_id: number;
  veterinarian_name: string;
}

type Medication = {
  created_at: string;
  dosage: string;
  end_date: string;
  frequency: string;
  medication_id: number;
  medication_name: string;
  pet_id: number;
  prescribed_by: string;
  start_date: string;
} 

type Appointment = {
  appointment_date: string;
  appointment_id: number;
  appointment_time: string;
  appointment_type: string;
  contact_id: number;
  notes: string;
  other_appt_type: string | null;
  pet_id: number
}

@Component({
  selector: 'app-main-dashboard',
  standalone: false,
  templateUrl: './main-dashboard.component.html',
  styleUrl: './main-dashboard.component.css'
})
export class MainDashboardComponent implements OnInit{
  src!: string;
  vaccinations: Vaccinations[] = [];
  newAppointment: boolean = false;

  appointmentFormGroup!: FormGroup;

  constructor(private petCareService: PetCareService){}

  pet!: Pet;

  petImage!: PetImage;

  medication!: Medication;

  appointments!: Appointment[];

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

        this.petCareService.fetchAppointments().subscribe({
          next: (response) => {
            console.log("Appointments retrieved: ", response);
            this.appointments = response;

            
          }
        })

       
                  

        this.petCareService.getMedications().subscribe({
          next: (response) => {
            console.log("Medications received from backend: ", response);
            this.medication = response;

            this.petCareService.fetchVaccinations().subscribe({
              next: (response) => {
                console.log("Vaccinations retrieved: ", response);
                this.vaccinations = response;

                this.appointmentFormGroup = this.buildAppointmentFormGroup(this.pet);
              }
            })
          }
        })
        
      }
    })
  }

  buildAppointmentFormGroup(pet: Pet) {
    return new FormGroup ({
      pet_id: new FormControl(pet.pet_id),
      contact_id: new FormControl(pet.pet_id),
      appointment_type: new FormControl<string>(''),
      other_appt_type: new FormControl<string>(''),
      appointment_date: new FormControl<string>(''),
      appointment_time: new FormControl<string>(''),
      notes: new FormControl<string>('')
    })
  }


  onSubmit() {
    console.log(this.appointmentFormGroup.value);
    this.petCareService.createAppointment(this.appointmentFormGroup.value).subscribe({
      next: (response) => {
        console.log('Response from creating new appointment: ', response);
        
      }, 
      error: (error) => {
        console.log('Error creating appointment response: ', error);
      }
    });
     
  }


  

}
