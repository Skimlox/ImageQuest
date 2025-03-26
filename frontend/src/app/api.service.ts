import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:5000/index'
  constructor(private http: HttpClient) { }
  getHelloMessage(): Observable<{ message: string }> {
    return this.http.get<{ message: string }>(this.apiUrl);
}
}