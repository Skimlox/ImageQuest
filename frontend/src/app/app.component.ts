import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import {GraphComponent} from './graph/graph.component';
import {ToolbarComponent} from './toolbar/toolbar.component';
import { ParametersComponent } from './parameters/parameters.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,RouterLink,GraphComponent,ToolbarComponent,ParametersComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'capstone';
}
