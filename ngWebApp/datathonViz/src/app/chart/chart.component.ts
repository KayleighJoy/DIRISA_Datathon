import { Component, OnInit } from '@angular/core';
import * as Chart from 'chart.js';
import { Connect } from 'Connect'
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-ProPie',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.scss']
})
export class ChartComponent implements OnInit {
  // Number of reported cases
  canvas: any;
  ctx: any;

  //Subscriptions
  //PieData : Subscription;

  //Province Data
  ncGP:number = 50;
  ncL:number = 50;
  ncWP:number = 50;
  ncEP:number = 50;
  ncNP:number = 50;
  ncKZN:number = 50;
  ncFS:number = 50;
  ncMP:number = 50;
  ncNW:number = 50;

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
              data: [this.ncGP, this.ncL, this.ncWP, this.ncNP, this.ncEP, this.ncKZN, this.ncNW, this.ncFS, this.ncMP],
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

  constructor(private connect: Connect) { }
  //constructor() { }

  ngOnInit() {
    // this.connect.getPieChart()


    // this.PieData = this.connect.PieChart.subscribe(data => {
    //   console.log(data);
    //   // for (var result in data) {
    //   //   this.arDrills.push(new Drill(data[result]['ID'], data[result]['Name'], data[result]['Description'], data[result]['Link'], data[result]['CoachID']))
    //   //   this.arDrills[result].setSessionID(data[result]['SessionID'])
    //   // }
    // })
  }

  

}
