import { Component, ViewChild } from '@angular/core';

import { NgForm, NgModel } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  @ViewChild('RegisterF', {static: false}) RegisterForm : NgForm;
  @ViewChild('PasswordRepeat', {static: false}) fPasswordRepeat :NgModel;
  @ViewChild('Password', {static: false}) fPassword :NgModel;
  @ViewChild('Name', {static: false}) fname :NgModel;
  @ViewChild('Surname', {static: false}) fsurname :NgModel;
  @ViewChild('ID_Number', {static: false}) fid :NgModel;
  @ViewChild('Cell_num', {static: false}) fcell :NgModel;
  @ViewChild('UserType', {static: false}) fusertype :NgModel;
}
