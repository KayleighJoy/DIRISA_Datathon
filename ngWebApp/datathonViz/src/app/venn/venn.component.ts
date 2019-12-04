import { Component, OnInit } from '@angular/core';
import * as Highcharts from 'highcharts';
import * as highchartsHeatmap from 'highcharts/modules/heatmap';
import { ConnectService } from '../connect.service';
import { Subscription } from 'rxjs';

declare var require: any;
const heatmap = require("highcharts/modules/heatmap.js");
heatmap(Highcharts)
const treemap = require("highcharts/modules/treemap.js");
treemap(Highcharts)

@Component({
  selector: 'app-venn',
  templateUrl: './venn.component.html',
  styleUrls: ['./venn.component.scss']
})
export class VennComponent implements OnInit 
{
  //HeatChart 
  HeatChart : Subscription;

  constructor(private connect: ConnectService){ }

  arrEP = []
  arrGau = []
  arrNP = []
  arrWP = []
  arrNW = []
  arrMP = []
  arrKZN = []
  arrL = []
  arrFS = []
  ngOnInit() {
    this.connect.getHeatChart()

    this.HeatChart = this.connect.HeatChart.subscribe(data => {
      this.arrEP = data["Eastern Cape"].split("-");
      this.arrNP = data["Northern Cape"].split("-");
      this.arrWP = data["Western Cape"].split("-");
      this.arrFS = data["Free State"].split("-");
      this.arrGau = data["Gauteng"].split("-");
      this.arrL = data["Limpopo"].split("-");
      this.arrMP = data["Mpumalanga"].split("-");
      this.arrNW = data["North West"].split("-");
      this.arrKZN = data["KwaZulu Natal"].split("-");

      console.log(this.arrGau);   
      
    })
  }



  provinces = ['Gauteng', 'Eastern Cape', 'Free State', 'KwaZulu-Natal',
  'Limpopo', 'Mpumalanga', 'Northern Cape', 'North West', 'Western Cape'];
  factors = ['Disabled', 'Unemployed', 'Male', 'Has Phone', 'Hospitalized'];
  factors1 = ['Disabled', 'Unemployed', 'Female', 'Has Phone', 'Hospitalized'];
  highcharts= Highcharts;
   
  // //marginTop: 40,
  //     width : 700,
  //     height: 800
  //marginBottom: 80
  chartOptions = 
  {
    chart : 
    {
      type: 'heatmap',
      marginTop: 40,
      width: 1400,
      height: 700,
      marginBottom: 80,
      style : {
        textShadow : false,
        textOutline : false
      },
    },
    title : 
    {
      text: 'Factors per province(yes)'
    },
    xAxis : 
    { 
      categories: this.provinces
    },
    yAxis : 
    {
      categories: this.factors,
      title : null
    },
    colorAxis : 
    {
      min : 0,
      minColor : '#EEC1B6',
      maxColor : '#790400'
    },
    legend : 
    {
      align : 'right',
      layout : 'vertical',
      margin : 0,
      verticalAlign : 'top',
      y : 25,
      symbolHeight : 280
    },
    tooltip : 
    {
      formatter: function () 
      {
         return this.point.value +
            '</b> People said yes in<br><b>' +
            this.series.xAxis.categories[this.point.x] + '</b>';
      }
    },
    series : 
    [
      {
        name: 'HeatMapFactors',
        borderWidth: 1,
        data: 
        [
          [0, 0, 3], [0, 1, 34], [0, 2, 19], [0, 3, 33], [0, 4, 6],
          [1, 0, 4], [1, 1, 21], [1, 2, 18], [1, 3, 28], [1, 4, 10],
          [2, 0, 6], [2, 1, 26], [2, 2, 16], [2, 3, 28], [2, 4, 10],
          [3, 0, 3], [3, 1, 23], [3, 2, 15], [3, 3, 27], [3, 4, 7],
          [4, 0, 3], [4, 1, 21], [4, 2, 13], [4, 3, 22], [4, 4,  4],
          [5, 0, 3], [5, 1, 25], [5, 2, 15], [5, 3, 27], [5, 4, 6],
          [6, 0, 5], [6, 1, 25], [6, 2, 15], [6, 3, 24], [6, 4, 9],
          [7, 0, 5], [7, 1, 24], [7, 2, 19], [7, 3, 28], [7, 4, 9],
          [8, 0, 2], [8, 1, 37], [8, 2, 20], [8, 3, 35], [8, 4, 8]
        ],   
        dataLabels: 
        {
          enabled: true,
          color: '#000000'
        }
      }
    ]
  };
  
}


