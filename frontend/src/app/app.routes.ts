import { Routes } from '@angular/router';

// To use new components, import them into app.routes.ts at the top of the file:

import { GraphComponent } from './graph/graph.component';       // Plotly Graph
import { AppComponent } from './app.component';                 // Main Application

// path to each component
// we would have different paths and routes if we are loading a new screen when we click a button
// because our application only has one screen, this is fine
export const routes: Routes = [
    
    { path: '', component: AppComponent },
    // PageNotFound 404
    //{ path: '**', component: PageNotFoundComponent},    ///Wildcard route for error 404. Need to implement this component?

    
];
