import { Component, ViewChild } from '@angular/core';

import { NgForm, NgModel } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  @ViewChild('RegisterF', {static: false}) RegisterForm : NgForm;
  @ViewChild('Chicken', {static: false}) ChickenEx : NgModel;


  //Try get this data and change it after pressing button
  PercNB:number = 50;
  PercRF:number = 50;
  PercSVM:number = 69;
  NB:String = "yes";
  RF:String = "no";
  SVM:String = "sixty nine";

  OnPredict() {
    //Values to work with the data
    // Values for Level Studies
    // IncHS CompHS IncUndergrad CompUndergrad IncMasters CompMasters IncPHD CompPHD
    // Values for Legally Disabled
    // NotDisabled Disabled
    // Values for Age Group
    // 1 = 18-29 2 = 30-44 3 = 45-60 4 = 60< 
    // Values for Gender
    // Male Female
    
    console.log(this.RegisterForm);
    console.log(this.ChickenEx.value);


    // this.PercNB
    // this.PercRF
    // this.PercSVM
    // this.NB
    // this.RF
    // this.SVM

  }
}
