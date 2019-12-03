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

  //Province Data
  rGP:number = 50;
  rL:number = 50;
  rWP:number = 50;
  rEP:number = 50;
  rNP:number = 50;
  rKZN:number = 50;
  rFS:number = 50;
  rMP:number = 50;
  rNW:number = 50;

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
              // Change data here
              data: [this.rGP, this.rL, this.rWP, this.rNP, this.rEP, this.rKZN, this.rNW, this.rFS, this.rMP],
              backgroundColor: [
                'rgba(255, 0, 0, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(242, 31, 207, 1)',
                  'rgba(22, 108, 27, 1)',
                  'rgba(177, 52, 235)',
                  'rgba(66, 219, 0, 1)',
                  'rgba(255, 136, 0, 1)',
                  'rgba(52, 58, 235)'
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
