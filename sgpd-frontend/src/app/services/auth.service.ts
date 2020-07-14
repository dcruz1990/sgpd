import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { map, catchError } from 'rxjs/operators';
import { JwtHelperService } from '@auth0/angular-jwt';
import { throwError, BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  $loginStatus = new BehaviorSubject('false')

  loginStatusObs = this.$loginStatus.asObservable()

  jwtHelper = new JwtHelperService();

  decodedToken;

  constructor(private http: HttpClient) { }

  login(data: any) {
    return this.http.post(environment.apiUrl + 'auth/login/', data).pipe(
      map((response: any,) => {
        this.$loginStatus.next('true')
        localStorage.setItem('token', response.access);
        this.decodedToken = this.jwtHelper.decodeToken(response.access);
        console.log(this.decodedToken)
      },
      ),
      catchError(this.handleError)
    );
  }

  handleError(error) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // client-side error
      errorMessage = `Error: ${error.error.message}`;
    } else {
      // server-side error
      switch (error.status) {
        case 0:
          errorMessage = "Ooops, no ha sido posible conectar con el servidor :("
          break;

        case 401:
          errorMessage = "Lo siento, no tiene acceso a realizar esta operacion"
          break;

        default:
          errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
          break;
      }


    }
    return throwError(errorMessage);
  }

}
