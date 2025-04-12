import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private url = 'http://127.0.0.1:5000'

  constructor(private http: HttpClient) { }
  DeclareModel(model: string): Observable<any> {
    return this.http.post<any>(`${this.url}/setmodel`, {model});
  }
  
  FeatureExtraction(model: string): Observable<any> {
    return this.http.post(`${this.url}/${model}`, {});
  }
  
  DimensionalityReduction(method: 'pca' | 'tsne'): Observable<any> {
    return this.http.post<any>(`${this.url}/${method}`, {});
  }
}