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
  private url_resnet_pca = 'http://127.0.0.1:5000/resnetpca'
  private url_vgg_pca = 'http://127.0.0.1:5000/vggpca'
  private url_inception_pca = 'http://127.0.0.1:5000/inceptionpca'
  private url_resnet_tsne = 'http://127.0.0.1:5000/resnettsne'
  private url_vgg_tsne = 'http://127.0.0.1:5000/vggtsne'
  private url_inception_tsne = 'http://127.0.0.1:5000/inceptiontsne'

  
  // Datasets
  private url_dataset1 = ''
  private url_dataset2 = ''
  private url_dataset3 = ''

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

  ResNetPCA(): Observable<any> {
    return this.http.post<any>(this.url_resnet_pca, {});
  }
  VGGPCA(): Observable<any> {
    return this.http.post<any>(this.url_vgg_pca, {});
  }
  InceptionPCA(): Observable<any> {
    return this.http.post<any>(this.url_inception_pca, {});
  }

  ResNetTSNE(): Observable<any> {
    return this.http.post<any>(this.url_resnet_tsne, {});
  }
  VGGTSNE(): Observable<any> {
    return this.http.post<any>(this.url_vgg_tsne, {});
  }
  InceptionTSNE(): Observable<any> {
    return this.http.post<any>(this.url_inception_tsne, {});
  }

  // Dataset Observables
  DS1(): Observable<any> {
    return this.http.post<any>(this.url_dataset1, {});
  }
  DS2(): Observable<any> {
    return this.http.post<any>(this.url_dataset2, {});
  }
  DS3(): Observable<any> {
    return this.http.post<any>(this.url_dataset3, {});
  }
}