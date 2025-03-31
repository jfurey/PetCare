import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PetCareService {

  constructor( private http: HttpClient) { }

  baseUrl = "http://localhost:5001";

  getPets(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/pets/${4}`);
  }

  getUsers(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/users`)
  }
}
