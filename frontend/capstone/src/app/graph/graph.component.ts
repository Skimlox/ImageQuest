import { Component} from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { PlotlyModule } from 'angular-plotly.js';
import { ToolbarComponent } from '../toolbar/toolbar.component';

@Component({
  selector: 'app-graph',
  imports: [PlotlyModule, RouterOutlet, RouterLink,ToolbarComponent],
  standalone: true,
  templateUrl: './graph.component.html',
  styleUrl: './graph.component.css',
})

export class GraphComponent {
  public graph = {
    data: [{x: [1999, 2000, 2001, 2002],
    y: [10, 15, 13, 17],
    z: [4],
    type: 'scatter3d'
    }],
    layout: { 
      width: 1250,
      height: 700,
      shapes: [{
        type: 'rect',
        xref: 'paper',
        yref: 'paper',
        x0: 0,
        y0: 0,
        x1: 1,
        y1: 1,
        line: {
          color: 'black',
          width: 3
        },
        fillcolor: 'rgba(0,0,0,0)',
        
    }],
  }
}

};
