import { Component, OnInit } from '@angular/core';
import * as Chart from 'chart.js';

@Component({
  selector: 'app-ProPie',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.scss']
})
export class ChartComponent implements OnInit {
  // Number of reported cases
  canvas: any;
  ctx: any;
  ngAfterViewInit() {

    this.canvas = document.getElementById('NumCasesChart');
    this.ctx = this.canvas.getContext('2d');
    let myChart = new Chart(this.ctx, {
      type: 'pie',
      data: {
          labels: ["Gauteng", "Limpopo", "Western Cape", "Northern Cape", "Eastern Cape", 
            "KwaZulu-Natal", "North-West", "Free State", "Mpumalanga"
          ],
          datasets: [{
              label: 'Number of Cases Reported',
              // Change data here
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
