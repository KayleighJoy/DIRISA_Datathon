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

  OnPredict() {
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
  }
}
