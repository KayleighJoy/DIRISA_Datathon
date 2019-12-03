import { Component, OnInit } from '@angular/core';
import * as Highcharts from 'highcharts';
import * as highchartsHeatmap from 'highcharts/modules/heatmap';
declare var require: any;
const heatmap = require("highcharts/modules/heatmap.js");
heatmap(Highcharts)
const treemap = require("highcharts/modules/treemap.js");
treemap(Highcharts)
// highchartsHeatmap(Highcharts);
// let Boost = require('highcharts/modules/boost');
// let noData = require('highcharts/modules/no-data-to-display');
// let More = require('highcharts/highcharts-more');

// Boost(Highcharts);
// noData(Highcharts);
// More(Highcharts);
// noData(Highcharts);

@Component({
  selector: 'app-venn',
  templateUrl: './venn.component.html',
  styleUrls: ['./venn.component.scss']
})
export class VennComponent implements OnInit 
{
  provinces = ['Gauteng', 'Eastern Cape', 'Free State', 'KwaZulu-Natal',
  'Limpopo', 'Mpumalanga', 'Northern Cape', 'North West', 'Western Cape'];
  factors = ['Disabled', 'Unemployed', 'Male', 'Has Phone', 'Hospitalized'];
  factors1 = ['Disabled', 'Unemployed', 'Female', 'Has Phone', 'Hospitalized'];
  highcharts= Highcharts;
  chartOptions = 
  {
    chart : 
    {
      type: 'heatmap',
      marginTop: 40,
      marginBottom: 80,
      style : {
        textShadow : false,
        textOutline : false
      }
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
      minColor : '#ECDDD9',
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
        name: 'Sales per employee',
        borderWidth: 1,
        data: 
        [
          [0, 0, 10], [0, 1, 19], [0, 2, 8], [0, 3, 24], [0, 4, 67],
          [1, 0, 92], [1, 1, 58], [1, 2, 78], [1, 3, 117], [1, 4, 48],
          [2, 0, 35], [2, 1, 15], [2, 2, 123], [2, 3, 64], [2, 4, 52],
          [3, 0, 72], [3, 1, 132], [3, 2, 114], [3, 3, 19], [3, 4, 16],
          [4, 0, 38], [4, 1, 5], [4, 2, 8], [4, 3, 117], [4, 4,  115],
          [5, 0, 88], [5, 1, 32], [5, 2, 12], [5, 3, 6], [5, 4, 120],
          [6, 0, 13], [6, 1, 44], [6, 2, 88], [6, 3, 98], [6, 4, 96],
          [7, 0, 31], [7, 1, 1], [7, 2, 82], [7, 3, 32], [7, 4, 30],
          [8, 0, 85], [8, 1, 97], [8, 2, 123], [8, 3, 64], [8, 4, 84]
        ],   
        dataLabels: 
        {
          enabled: true,
          color: '#000000'
        }
      }
    ]
  };
  
  highcharts1= Highcharts;
  chartOptions1 = {
    chart : 
    {
      type: 'heatmap',
      marginTop: 40,
      marginBottom: 80,
      style : {
        textShadow : false,
        textOutline : false
      }
    },
    title : 
    {
      text: 'Factors per province(no)'
    },
    xAxis : 
    { 
      categories: this.provinces
    },
    yAxis : 
    {
      categories: this.factors1,
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
            '</b> People said no in<br><b>' +
            this.series.xAxis.categories[this.point.x] + '</b>';
      }
    },
    series : 
    [
      {
        name: 'Sales per employee',
        borderWidth: 1,
        data: 
        [
          [0, 0, 10], [0, 1, 19], [0, 2, 8], [0, 3, 24], [0, 4, 67],
          [1, 0, 92], [1, 1, 58], [1, 2, 78], [1, 3, 117], [1, 4, 48],
          [2, 0, 35], [2, 1, 15], [2, 2, 123], [2, 3, 64], [2, 4, 52],
          [3, 0, 72], [3, 1, 132], [3, 2, 114], [3, 3, 19], [3, 4, 16],
          [4, 0, 38], [4, 1, 5], [4, 2, 8], [4, 3, 117], [4, 4,  115],
          [5, 0, 88], [5, 1, 32], [5, 2, 12], [5, 3, 6], [5, 4, 120],
          [6, 0, 13], [6, 1, 44], [6, 2, 88], [6, 3, 98], [6, 4, 96],
          [7, 0, 31], [7, 1, 1], [7, 2, 82], [7, 3, 32], [7, 4, 30],
          [8, 0, 85], [8, 1, 97], [8, 2, 123], [8, 3, 64], [8, 4, 84]
        ],   
        dataLabels: 
        {
          enabled: true,
          color: '#000000'
        }
      }
    ]
  };
  ngOnInit() {
   // Highcharts.chart('container', this.options);
  
  
  }
}


