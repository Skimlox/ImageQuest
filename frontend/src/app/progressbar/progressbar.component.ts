// Based on W3 Schools JS Progress Bar AND toolbar.component.ts

import { Component, ElementRef, ViewChild } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-progressbar',
  imports: [CommonModule],
  standalone: true,
  templateUrl: './progressbar.component.html',
  styleUrl: './progressbar.component.css'
})
export class ProgressbarComponent {
  constructor(private NNAPI: ApiService) { }
}


