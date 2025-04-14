import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import {GraphComponent} from './graph/graph.component';
import {ToolbarComponent} from './toolbar/toolbar.component';
import { ProgressbarComponent } from './progressbar/progressbar.component';
import { ApiService } from './api.service';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,RouterLink,GraphComponent,ToolbarComponent, ProgressbarComponent],     // RouterOutlet, RouterLink are here because of Angular Routing
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'capstone';
  message: string = '';

  
}
