import { Component, ElementRef, ViewChild } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ApiService } from '../api.service';
@Component({
  selector: 'app-toolbar',
  imports: [CommonModule],
  standalone: true,
  templateUrl: './toolbar.component.html',
  styleUrl: './toolbar.component.css'
})
export class ToolbarComponent {
  constructor(private NNAPI: ApiService) { }
  
  ResNet50() {
    
    this.NNAPI.ResNet().subscribe({
      next: (response) => {
        console.log(response);
        alert('ResNet feature extraction successful');
      },
      error: (error) => {
        console.log(error);
        alert('ResNet feature extraction not successful');
      }
    });
    }
 VGG16() {
    this.NNAPI.VGG().subscribe({
      next: (response) => {
        console.log(response);
        alert('VGG feature extraction successful');
      },
      error: (error) => {
        console.log(error);
        alert('VGG feature extraction not successful');
      }
    });
    }
  InceptionV3() {
    
    this.NNAPI.Inception().subscribe({
      next: (response) => {
        console.log(response);
        alert('Inception feature extraction successful');
      },
      error: (error) => {
        console.log(error);
        alert('Inception feature extraction not successful');
      }
    });
    }

    // WIP Create a Constructor/Objecct Initialize for the Datasets
    // Datasets(){

    // }
  }
  


