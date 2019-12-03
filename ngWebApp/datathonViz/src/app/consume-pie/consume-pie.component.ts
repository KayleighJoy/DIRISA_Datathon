import { Component, OnInit } from '@angular/core';
import * as Chart from 'chart.js';

@Component({
  selector: 'app-consume-pie',
  templateUrl: './consume-pie.component.html',
  styleUrls: ['./consume-pie.component.scss']
})
export class ConsumePieComponent implements OnInit {
  // Number of Medicine Consumed per provinces
  //Province Data
  nmGP:number = 50;
  nmL:number = 50;
  nmWP:number = 50;
  nmEP:number = 50;
  nmNP:number = 50;
  nmKZN:number = 50;
  nmFS:number = 50;
  nmMP:number = 50;
  nmNW:number = 50;
  
  canvas: any;
  ctx: any;

  ngAfterViewInit() {
    
    this.canvas = document.getElementById('MedConsumedChart');
    this.ctx = this.canvas.getContext('2d');
    let myChart = new Chart(this.ctx, {
      type: 'pie',
      data: {
          labels: ["Gauteng", "Limpopo", "Western Cape", "Northern Cape", "Eastern Cape", 
            "KwaZulu-Natal", "North-West", "Free State", "Mpumalanga"
          ],
          datasets: [{
              label: 'Number of Medicine bought/consumed per province',
              // Change data here
              data: [this.nmGP, this.nmL, this.nmWP, this.nmNP, this.nmEP, this.nmKZN, this.nmNW, this.nmFS, this.nmMP],
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
