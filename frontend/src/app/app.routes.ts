import { Routes } from '@angular/router';
import { GraphComponent } from './graph/graph.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';

export const routes: Routes = [
    {
        path: '',
        component: LoginComponent,
    }
    ,
    {
        path: 'main',
        component: GraphComponent,
    }
,
    {
        path: 'signup',
        component: SignupComponent,

        
    }
    
];
