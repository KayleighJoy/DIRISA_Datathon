import { Component, OnInit } from '@angular/core';
import * as Chart from 'chart.js';

@Component({
  selector: 'app-bar-risk',
  templateUrl: './bar-risk.component.html',
  styleUrls: ['./bar-risk.component.scss']
})
export class BarRiskComponent implements OnInit {
  // Risk of illness
  canvas: any;
  ctx: any;
  ngAfterViewInit() {

    this.canvas = document.getElementById('BarRisk');
    this.ctx = this.canvas.getContext('2d');
    let myChart = new Chart(this.ctx, {
      type: 'bar',
      data: {
          labels: ["Gauteng", "Limpopo", "Western Cape", "Northern Cape", "Eastern Cape", 
            "KwaZulu-Natal", "North-West", "Free State", "Mpumalanga"
          ],
          datasets: [{
              label: '# of Votes',
              data: [32,123,20,43,69, 420, 44, 77, 56],
              backgroundColor: [
                'rgba(255, 0, 0, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(242, 31, 207, 1)',
                'rgba(22, 108, 27, 1)',
                'rgba(131, 0, 219, 1)',
                'rgba(66, 219, 0, 1)',
                'rgba(255, 136, 0, 1)',
                'rgba(4, 20, , 1)',
              ],
             borderWidth: 1
          }]
      },
      options: {
       responsive: false,
        display:true
      }
    });
  }

  constructor() { }

  ngOnInit() {
  }
}
