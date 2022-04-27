import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class UserService {
  baseurl!:'http://127.0.0.1:8000/api/register/'
  
  constructor(private http: HttpClient) { }
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }
  registerNewUser(userData: any): Observable <any> {
    return this.http.post('http://127.0.0.1:8000/api/register/', userData, this.httpOptions)
  }
}