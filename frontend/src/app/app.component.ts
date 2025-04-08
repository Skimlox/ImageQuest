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


// changing template/styleURLs from ./app.component.html and .app/component.css to
// ./toolbar/toolbar.component.html and ./toolbar/toolbar.component.css
// REVERTED
// doing so would make the Resnet50, VGG16, InceptionV3 no longer exist to the app.
// Might need to somehow do the AngularFireDatabase... and then also forward to the toolbar.component html and css


// 
export class AppComponent {
  title = 'capstone';
  message: string = '';


  // WIP Getting the Main2 Dataset from FirebaseDatabase
  // Uncommenting this will cause the webapp to load a blank page.
  // Something to do with if this is non-empty, then the application doesn't know where the html/css actually is.
  // I will try to fix this up above in @Component
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
