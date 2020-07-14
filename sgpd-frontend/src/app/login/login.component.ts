import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';

import { NgxUiLoaderService } from 'ngx-ui-loader';
import { AlertService } from '../services/alert.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  authData = {
    username: "",
    password: ''
  }

  logedIn
  isLoading

  constructor(private auth: AuthService,
    private ngxService: NgxUiLoaderService,
    private alertService: AlertService

  ) {
    this.isLoading = false
  }

  ngOnInit() {
    this.auth.$loginStatus.subscribe(status => this.logedIn = status)
    console.log(this.logedIn)

  }

  login() {
    this.isLoading = true
    this.auth.login(this.authData).subscribe((request) => {

    }, error => {
      console.log(error)

      this.alertService.showSnackBar(error)
      this.isLoading = false
    }, () => {
      this.ngxService.stopLoader('loader-01');
      this.isLoading = false

    })
  }

  load() {
    this.isLoading = true
  }

}
