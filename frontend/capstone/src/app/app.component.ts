import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {LoginComponent} from './login/login.component'
import {GraphComponent} from './graph/graph.component'
import { Plotly } from 'angular-plotly.js';
@Component({
  selector: 'app-root',
  imports: [RouterOutlet,LoginComponent,GraphComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'capstone';
}
