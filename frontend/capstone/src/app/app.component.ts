import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import {LoginComponent} from './login/login.component'
import {GraphComponent} from './graph/graph.component'
import {ToolbarComponent} from './toolbar/toolbar.component'
import { SignupComponent } from './signup/signup.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,RouterLink,LoginComponent,GraphComponent,ToolbarComponent,SignupComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'capstone';
}
