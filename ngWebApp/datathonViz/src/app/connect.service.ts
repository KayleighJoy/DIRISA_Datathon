import { HttpClient } from '@angular/common/http';
import { Observable, throwError, Subject } from 'rxjs';
import { catchError, retry, subscribeOn } from 'rxjs/operators';
import { HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';
//import { runInThisContext } from 'vm';

@Injectable({
  providedIn: 'root'
})

export class ConnectService {
  // http://127.0.0.1:5000/getAllProvinceData
  Link = "http://localhost:5000";
  PieChart = new Subject<JSON>();
  BarChart = new Subject<JSON>();
  constructor(private http: HttpClient) { }


  UpdatePieChart(dt: JSON) {
    this.PieChart.next(dt)
  }

  UpdateBarChart(dt: JSON) {
    this.BarChart.next(dt)
  }

   getPieChart(){
     this.http.get(this.Link +'/getAllProvinceData').subscribe(response => {
         catchError(this.handleError)
         this.UpdatePieChart(JSON.parse(JSON.stringify(response)));
     })
   }

  getBarChart(){
    this.http.get(this.Link +'/AllTeams').subscribe(response => {
        catchError(this.handleError)
        this.UpdateBarChart(JSON.parse(JSON.stringify(response)));
    })
  }

// Predict(LevelEdu, Disabled, Unemployed, Age, Gender, Income, Mobile, Hospitalized) {
//     var data = {
//         "playerID": PlayerID,
//         "teamID": TeamID
//     }
//     this.http.post(this.Link + "/addPlayer", data).subscribe(response => {
//         catchError(this.handleError) //send to catcherror
//         console.log(response)
//     })
// }

handleError(error: HttpErrorResponse) {
  if (error.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error.message);
  } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      console.error(
          `Backend returned code ${error.status}, ` +
          `body was: ${error.error}`);
  }
  // return an observable with a user-facing error message
  return throwError(
      'Something bad happened; please try again later.');
};
}
