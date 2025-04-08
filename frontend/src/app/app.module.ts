import { NgModule} from '@angular/core';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { GraphComponent } from './graph/graph.component';
import { PlotlyModule } from 'angular-plotly.js';
import * as Plotly from 'plotly.js';
import { provideHttpClient } from '@angular/common/http';
import { ParametersComponent } from './parameters/parameters.component';

// Imports for Angular Framework to connect to Firebase Database  
import { AngularFireModule } from 'angularfire2';
import { AngularFireDatabaseModule } from 'angularfire2/database';
import { environment } from '../environments/environment';

PlotlyModule.plotlyjs = Plotly;
@NgModule({
  declarations: [
    AppComponent,
    GraphComponent,
    ParametersComponent,],
  providers: [
    provideHttpClient()
  ],
  imports: [
    CommonModule,
    PlotlyModule,
    BrowserModule,
    AngularFireModule.initializeApp(environment.firebase),
    AngularFireDatabaseModule
  ],
  bootstrap: [AppComponent]
  
})
export class AppModule { }
