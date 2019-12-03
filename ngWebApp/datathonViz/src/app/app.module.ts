import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ChartComponent } from './chart/chart.component';
import { ConsumePieComponent } from './consume-pie/consume-pie.component';
import { BarRiskComponent } from './bar-risk/bar-risk.component';


import { FormsModule } from '@angular/forms';
@NgModule({
  declarations: [
    FormsModule,
    AppComponent,
    ChartComponent,
    ConsumePieComponent,
    BarRiskComponent
  ],
  imports: [
    NgbModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
