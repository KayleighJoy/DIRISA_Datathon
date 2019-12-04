import { Component, ViewChild } from '@angular/core';
import { NgForm, NgModel, NumberValueAccessor } from '@angular/forms';
import { ConnectService } from './connect.service';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  @ViewChild('RegisterF', {static: false}) RegisterForm : NgForm;
  @ViewChild('Chicken', {static: false}) ChickenEx : NgModel;
  
  constructor(private connect: ConnectService) { }

  //Prediction
  Prediction : Subscription;

  //Try get this data and change it after pressing button
  PercNB:number = 50;
  PercRF:number = 50;
  PercSVM:number = 69;
  NB:String = "yes";
  RF:String = "no";
  SVM:String = "sixty nine";
  Income = 32

  //LevelEdu, Disabled, Unemployed, Age, Gender, Income, Mobile, Hospitalized
  //Prediction Values
  LvlEdu:number = 0;
  Disabled:number = 0;
  Unemployed:number = 0;
  Age:number = 0;
  Gender:number = 0;
  IncomeRank:number = -1;
  Mobile:number = 0;
  Hospitalized:number = 0;

  SortIncomer(){
    switch(true) { 
      case (this.Income < 55600): 
        this.IncomeRank = 1;
         break; 
      case ((this.Income >= 55600) && (this.Income < 139000)): 
        this.IncomeRank = 2;
        break; 
      case ((this.Income >= 139000) && (this.Income < 278000)):
        this.IncomeRank = 3;
        break; 
      case ((this.Income >= 278000) && (this.Income < 417000)): 
        this.IncomeRank = 4;
        break; 
      
      case ((this.Income >= 417000) && (this.Income < 556000)): 
        this.IncomeRank = 5;
        break; 
      
      case ((this.Income >= 55600) && (this.Income < 695000)): 
        this.IncomeRank = 6;
        break; 
      
      case ((this.Income >= 695000) && (this.Income < 834000)): 
        this.IncomeRank = 7;
        break; 
      
      case ((this.Income >= 834000) && (this.Income < 973000)): 
        this.IncomeRank = 8;
        break; 
      case ((this.Income >= 973000) && (this.Income < 1112000)): 
        this.IncomeRank = 9;
        break; 
      case (this.Income >= 1112000) : 
        this.IncomeRank = 10;
        break; 
      default: 
        this.IncomeRank = -1;
        break;  
   }
  
  }

  ngOnInit() {
    this.Prediction = this.connect.Prediction.subscribe(data => {
      console.log(data);
    })
  }
    

  OnPredict() {
    this.SortIncomer();
    // Check if grouping is correct for income
    if (this.IncomeRank == -1)
    {
      alert("Did not fill information");
      return 0;
    }
    
    // Setup data for prediction API

    console.log(this.RegisterForm);

    //this.connect.Predict()

    //Values to work with the data
    // Values for Level Studies
    // IncHS CompHS IncUndergrad CompUndergrad IncMasters CompMasters IncPHD CompPHD
    // Values for Legally Disabled
    // NotDisabled Disabled
    // Values for Age Group
    // 1 = 18-29 2 = 30-44 3 = 45-60 4 = 60< 
    // Values for Gender
    // Male Female
    
    
    console.log(this.IncomeRank);

    
    // this.PercNB
    // this.PercRF
    // this.PercSVM
    // this.NB
    // this.RF
    // this.SVM

  }

}
