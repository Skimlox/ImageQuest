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

    // The three Dataset options
    // The display may display the name from Firebase, but the function will be lableled as Dataset1 2 or 3
    // functions DS1, DS2, DS3 are in api.service.ts

    // TEST 4/10/25 10:40am. I expect the code to load as usual: graph, toolbar, etc.
    // NEXT TEST And then AFTER i implement the DS functions, then it will show console logs
    Dataset1(){

      this.NNAPI.DS1().subscribe({
        next: (response) => {
          console.log(response);
          alert('Dataset1 Selected');
        },
        error: (error) => {
          console.log(error);
          alert('Dataset1 Errored');
        }
      });
    }

    Dataset2(){
      
      this.NNAPI.DS2().subscribe({
        next: (response) => {
          console.log(response);
          alert('Dataset2 Selected');
        },
        error: (error) => {
          console.log(error);
          alert('Dataset2 Errored');
        }
      });

    }

    Dataset3(){

      this.NNAPI.DS3().subscribe({
        next: (response) => {
          console.log(response);
          alert('Dataset2 Selected');
        },
        error: (error) => {
          console.log(error);
          alert('Dataset2 Errored');
        }
      });

    }
  }
  


