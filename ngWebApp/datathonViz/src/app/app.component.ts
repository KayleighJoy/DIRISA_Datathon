import { Component, ViewChild } from '@angular/core';
import { NgForm, NgModel, NumberValueAccessor } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  @ViewChild('RegisterF', {static: false}) RegisterForm : NgForm;
  @ViewChild('Chicken', {static: false}) ChickenEx : NgModel;
  @ViewChild('Income' , {static: false}) Income : NgModel;
  //Try get this data and change it after pressing button
  PercNB:number = 50;
  PercRF:number = 50;
  PercSVM:number = 69;
  NB:String = "yes";
  RF:String = "no";
  SVM:String = "sixty nine";
  IncomeRank:number = -1;
  

  SortIncomer(){
    // 0-55599 -1
    // 55600-138999-2
    // 139000-277999-3
    // 278000-416999-4
    // 417000-555999-5
    // 556000-694999-6
    // 695000-833999-7
    // 834000-972999-8
    // 973000-1111999-9
    // >1112000-10
    console.log("Chickens")
    switch(true) { 
      case (this.Income.value < 55600): 
        this.IncomeRank = 1;
         break; 
      case ((this.Income.value >= 55600) && (this.Income.value < 139000)): 
        this.IncomeRank = 2;
        break; 
      case ((this.Income.value >= 139000) && (this.Income.value < 278000)):
        this.IncomeRank = 3;
        break; 
      case ((this.Income.value >= 278000) && (this.Income.value < 417000)): 
        this.IncomeRank = 4;
        break; 
      
      case ((this.Income.value >= 417000) && (this.Income.value < 556000)): 
        this.IncomeRank = 5;
        break; 
      
      case ((this.Income.value >= 55600) && (this.Income.value < 695000)): 
        this.IncomeRank = 6;
        break; 
      
      case ((this.Income.value >= 695000) && (this.Income.value < 834000)): 
        this.IncomeRank = 7;
        break; 
      
      case ((this.Income.value >= 834000) && (this.Income.value < 973000)): 
        this.IncomeRank = 8;
        break; 
      case ((this.Income.value >= 973000) && (this.Income.value < 1112000)): 
        this.IncomeRank = 9;
        break; 
      case (this.Income.value >= 1112000) : 
        this.IncomeRank = 10;
        break; 
      default: 
        this.IncomeRank = -1;
        break;  
   }
  
  }

  OnPredict() {
    
    this.SortIncomer();
    console.log(this.IncomeRank)
    if (this.IncomeRank == -1)
    {
      alert("Did not fill information");
      return 0;
    }
    
    //COMPLETE THIS with the income


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
