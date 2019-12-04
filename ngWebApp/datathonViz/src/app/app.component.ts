import { Component, ViewChild } from '@angular/core';
import { NgForm, NgModel, NumberValueAccessor } from '@angular/forms';
import { ConnectService } from './connect.service';
import { Subscription } from 'rxjs';
import { stringify } from 'querystring';
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
  PercSVM:number = 0;
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
      //     PercSVM:number = 69;
      // SVM:String = "sixty nine";
      //       prob: 0.7186360464140141
      // status: "At Risk"
      
      this.PercSVM = data['prob'] * 100;
      
      this.SVM = data['status']
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
    this.LvlEdu = this.RegisterForm.value.LevelEducation
    this.Disabled = this.RegisterForm.value.Disabled
    this.Unemployed = this.RegisterForm.value.Employed
    this.Age = this.RegisterForm.value.AgeGroup
    this.Gender = this.RegisterForm.value.Gender
    // IncomeRank
    this.Mobile = this.RegisterForm.value.Mobile
    this.Hospitalized = this.RegisterForm.value.Hospital
    
    this.connect.Predict(this.LvlEdu,this.Disabled,this.Unemployed,this.Age,this.Gender,this.IncomeRank,this.Mobile,this.Hospitalized);
    
    console.log(this.IncomeRank);
  }

}
