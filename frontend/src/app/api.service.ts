import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private url_resnet = 'http://127.0.0.1:5000/resnet'
  private url_vgg = 'http://127.0.0.1:5000/vgg'
  private url_inception = 'http://127.0.0.1:5000/inception'
  constructor(private http: HttpClient) { }
  
  ResNet(): Observable<any> {
    return this.http.post<any>(this.url_resnet, {});
  }
  VGG(): Observable<any> {
    return this.http.post<any>(this.url_vgg, {});
  }
  Inception(): Observable<any> {
    return this.http.post<any>(this.url_inception, {});
  }
}