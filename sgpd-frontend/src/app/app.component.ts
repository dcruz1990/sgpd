import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { map, shareReplay } from 'rxjs/operators';
import { AuthService } from './services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  loginMode = true

  isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

  isLoggedIn

  constructor(private breakpointObserver: BreakpointObserver, private auth: AuthService) {

  }

  title = 'sgpd-frontend';

  ngOnInit() {
    this.isLoggedIn = this.auth.getCurrentLoginStatus()
  }


}
