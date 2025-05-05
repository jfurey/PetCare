import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PetCareService {

  public user: any = null;
  baseUrl = "http://localhost:5001"; 

  constructor(private http: HttpClient) {
    const saved = localStorage.getItem('user');
    this.user = saved ? JSON.parse(saved) : null;
  }

  isLoggedIn(): boolean {
    return this.user !== null;
  }

  setUser(userData: any): void {
    this.user = userData;
    localStorage.setItem('user', JSON.stringify(userData));
  }

  logout(): void {
    this.user = null;
    localStorage.removeItem('user');
  }

  getUser(): any {
    return this.user;
  }

  getPets(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/pets/${4}`);
  }

  getPetImage(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/pets/user/${4}`);
  }

  login(credentials: Object): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/users/login`, credentials);
  }

  getUserProfile(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/user-profile`);
  }

  updateUserProfile(profile: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/user-profile`, profile);
  }

  getMedications(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/medications/${1}`);
  }

  fetchAppointments(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/appointments`);
  }

  fetchVaccinations(): Observable<any>{
    return this.http.get<any>(`${this.baseUrl}/vaccinations/pet/${2}`);
  }
  
}
