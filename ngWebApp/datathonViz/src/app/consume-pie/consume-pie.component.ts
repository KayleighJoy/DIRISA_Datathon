import { Component, OnInit } from '@angular/core';
import * as Chart from 'chart.js';
import { ConnectService } from '../connect.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-consume-pie',
  templateUrl: './consume-pie.component.html',
  styleUrls: ['./consume-pie.component.scss']
})
export class ConsumePieComponent implements OnInit {
  // Number of Medicine Consumed per provinces
  //Province Data
  GP:number = 0;
  L:number = 0;
  WP:number = 0;
  EP:number = 0;
  NP:number = 0;
  KZN:number = 0;
  FS:number = 0;
  MP:number = 0;
  NW:number = 0;
  
  //Percentage
  pGP:number = 0;
  pL:number = 0;
  pWP:number = 0;
  pEP:number = 0;
  pNP:number = 0;
  pKZN:number = 0;
  pFS:number = 0;
  pMP:number = 0;
  pNW:number = 0;


  TotalNSA:number = 0;
  TotSA:number = 0;

  //Total Percentage
  TotalPNSA:number = 0;

  canvas: any;
  ctx: any;

  AllData : Subscription;

  ngAfterViewInit() { }
    
  constructor(private connect: ConnectService) { }

  ngOnInit() {
    this.AllData = this.connect.ProvinceData.subscribe(data => {
       console.log(data);
      
      //Percentage Illness per province
      this.WP = data['Western Cape'][0]
      this.GP = data['Gauteng'][0];
      this.L = data['Limpopo'][0];
      this.NP = data['Northern Cape'][0];
      this.EP = data['Eastern Cape'][0];
      this.KZN = data['KwaZulu Natal'][0];
      this.NW = data['North West'][0];
      this.FS = data['Free State'][0];
      this.MP = data['Mpumalanga'][0];

       //  Total Non Illness in SA
      this.TotalNSA = data['Western Cape'][1] + data['Gauteng'][1] + data['Limpopo'][1] + data['Northern Cape'][1] + data['Eastern Cape'][1] + data['KwaZulu Natal'][1] + data['North West'][1] + data['Free State'][1] + data['Mpumalanga'][1];
      
      //Total reports In South Africa
      this.TotSA = this.TotalNSA + this.WP + this.GP + this.L + this.NP + this.EP + this.KZN + this.NW + this.FS + this.FS;

      

      //Percentage
      this.pWP = (this.WP / this.TotSA) * 100;
      this.pGP = (this.GP / this.TotSA) * 100;
      this.pL = (this.L / this.TotSA) * 100;
      this.pNP = (this.NP / this.TotSA) * 100;
      this.pEP = (this.EP / this.TotSA) * 100;
      this.pKZN = (this.KZN / this.TotSA) * 100;
      this.pNW = (this.NW / this.TotSA) * 100;
      this.pFS = (this.FS / this.TotSA) * 100;
      this.pMP = (this.MP / this.TotSA) * 100;

      this.TotalPNSA = (this.TotalNSA/this.TotSA) * 100;
      
      this.canvas = document.getElementById('MedConsumedChart');
      this.ctx = this.canvas.getContext('2d');
    let myChart = new Chart(this.ctx, {
      type: 'pie',
      data: {
          labels: ["Gauteng", "Limpopo", "Western Cape", "Northern Cape", "Eastern Cape", 
            "KwaZulu-Natal", "North-West", "Free State", "Mpumalanga", "Healthy Population in South Africa"
          ],
          datasets: [{
               label: ["Provincial population at risk"],
              // Change data here
              data: [this.pGP, this.pL, this.pWP, this.pNP, this.pEP, this.pKZN, this.pNW, this.pFS, this.pMP, this.TotalPNSA],
              backgroundColor: [
                'rgba(255, 0, 0, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(242, 31, 207, 1)',
                'rgba(22, 108, 27, 1)',
                'rgba(177, 52, 235)',
                'rgba(66, 219, 0, 1)',
                'rgba(255, 136, 0, 1)',
                'rgba(52, 58, 235)',
                'rgba(105, 105, 105)'
              ],
              borderWidth: 1
          }]
      },
      options: {
        responsive: false,
        display:true
      }
    });
     })
  }
}
