import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ChartComponent } from './chart/chart.component';
import { ConsumePieComponent } from './consume-pie/consume-pie.component';
import { BarRiskComponent } from './bar-risk/bar-risk.component';
import { HighchartsChartComponent } from 'highcharts-angular';


import { FormsModule } from '@angular/forms';
import { VennComponent } from './venn/venn.component';
import { ChartModule } from 'angular-highcharts';
@NgModule({
  declarations: [
    
    AppComponent,
    ChartComponent,
    ConsumePieComponent,
    BarRiskComponent,
    VennComponent,
    HighchartsChartComponent
  ],
  imports: [
    FormsModule,
    NgbModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ChartModule // add ChartModule to your imports
  ],
  providers: [],
  bootstrap: [AppComponent],

})
export class AppModule { }
