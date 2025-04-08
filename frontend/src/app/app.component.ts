import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import {GraphComponent} from './graph/graph.component';
import {ToolbarComponent} from './toolbar/toolbar.component';
import { ApiService } from './api.service';

// Angular Fire Database
import { AngularFireDatabase } from 'angularfire2/database';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,RouterLink,GraphComponent,ToolbarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

// 
export class AppComponent {
  title = 'capstone';
  message: string = '';

  
  // // Getting the Main2 Dataset from FirebaseDatabase
  // main2: any[];

  // constructor(db: AngularFireDatabase) {
  //   // Initialization inside the constructor
  //   this.main2 = [];
    
  //   db.list('/main2')
  //     .valueChanges()
  //     .subscribe(main2  => {
  //       this.main2 = main2;
  //       console.log(this.main2);
  //     });
  // }
  
  
}
