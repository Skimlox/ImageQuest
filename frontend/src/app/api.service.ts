import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private url = 'http://127.0.0.1:5000/resnet'
  constructor(private http: HttpClient) { }
  
  ResNet(): Observable<any> {
    return this.http.post<any>(this.url, {});
  }

}