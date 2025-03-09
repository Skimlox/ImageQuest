import { NgModule} from '@angular/core';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { GraphComponent } from './graph/graph.component';
import { PlotlyModule } from 'angular-plotly.js';
import * as Plotly from 'plotly.js';
PlotlyModule.plotlyjs = Plotly;
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    GraphComponent],
  imports: [
    CommonModule,
    PlotlyModule,
    BrowserModule
  ],
  
})
export class AppModule { }
