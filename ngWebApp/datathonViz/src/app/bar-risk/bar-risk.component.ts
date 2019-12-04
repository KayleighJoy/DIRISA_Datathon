import { Component, OnInit } from '@angular/core';
import * as Chart from 'chart.js';

import { ConnectService } from '../connect.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-bar-risk',
  templateUrl: './bar-risk.component.html',
  styleUrls: ['./bar-risk.component.scss']
})
export class BarRiskComponent implements OnInit {
  // Risk of illness
  canvas: any;
  ctx: any;

  //Subscriptions
  BarChart: Subscription;

  //Total Province Data
  tGP:number = 50;
  tL:number = 50;
  tWP:number = 50;
  tEP:number = 50;
  tNP:number = 50;
  tKZN:number = 50;
  tFS:number = 50;
  tMP:number = 50;
  tNW:number = 50;

  //Percentage
  pGP:number = 50;
  pL:number = 50;
  pWP:number = 50;
  pEP:number = 50;
  pNP:number = 50;
  pKZN:number = 50;
  pFS:number = 50;
  pMP:number = 50;
  pNW:number = 50;

  ngAfterViewInit() {
  }

  constructor(private connect: ConnectService) { }

  ngOnInit() {
    this.BarChart = this.connect.ProvinceData.subscribe(data => {
       console.log(data);
      //  this.ncGP, this.ncL, this.ncWP, this.ncNP, this.ncEP, this.ncKZN, this.ncNW, this.ncFS, this.ncMP
      this.tWP = data['Western Cape'][0] + data['Western Cape'][1];
      this.tGP = data['Gauteng'][0] + data['Gauteng'][1];
      this.tL = data['Limpopo'][0] + data['Limpopo'][1];
      this.tNP = data['Northern Cape'][0] + data['Northern Cape'][1];
      this.tEP = data['Eastern Cape'][0] + data['Eastern Cape'][1];
      this.tKZN = data['KwaZulu Natal'][0] + data['KwaZulu Natal'][1];
      this.tNW = data['North West'][0] + data['North West'][1];
      this.tFS = data['Free State'][0] + data['Free State'][1];
      this.tMP = data['Mpumalanga'][0] + data['Mpumalanga'][1];
      

      //Percentage
      this.pWP = Math.round((data['Western Cape'][0] / this.tWP) * 100);
      this.pGP = Math.round((data['Gauteng'][0] / this.tGP) * 100);
      this.pL = Math.round((data['Limpopo'][0] / this.tL) * 100);
      this.pNP = Math.round((data['Northern Cape'][0] / this.tNP) * 100);
      this.pEP = Math.round((data['Eastern Cape'][0] / this.tEP) * 100);
      this.pKZN = Math.round((data['KwaZulu Natal'][0] / this.tKZN) * 100);
      this.pNW = Math.round((data['North West'][0] / this.tNW) * 100);
      this.pFS = Math.round((data['Free State'][0] / this.tFS) * 100);
      this.pMP = Math.round((data['Mpumalanga'][0] / this.tMP) * 100);

      
      this.canvas = document.getElementById('BarRisk');
      this.ctx = this.canvas.getContext('2d');
    let myChart = new Chart(this.ctx, {
      type: 'bar',
      data: {
          labels: ["Eastern Cape", "North-West", "Western Cape", "Free State", "KwaZulu-Natal",
          "Gauteng", "Limpopo",  "Northern Cape", "Mpumalanga"
          ],
          datasets: [{
               label: ["Provincial population at risk"],
              // Change data here
              data: [this.pEP, this.pNW, this.pWP, this.pFS, this.pKZN, this.pGP, this.pL, this.pNP, this.pMP],
              backgroundColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)'
                  // 'rgba(255, 0, 0, 1)',
                  // 'rgba(54, 162, 235, 1)',
                  // 'rgba(255, 206, 86, 1)',
                  // 'rgba(242, 31, 207, 1)',
                  // 'rgba(22, 108, 27, 1)',
                  // 'rgba(177, 52, 235)',
                  // 'rgba(66, 219, 0, 1)',
                  // 'rgba(255, 136, 0, 1)',
                  // 'rgba(52, 58, 235)'
              ],
             borderWidth: 1
          }]
      },
      options: {
        scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
      },
       responsive: false,
        display:true
      }
    });
     })
  }
}
