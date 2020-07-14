import { Component } from '@angular/core';
import { Observable } from 'rxjs';

import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { map, shareReplay } from 'rxjs/operators';
import { AuthService } from './services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  loginMode = true

  isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

  isLoggedIn

  constructor(private breakpointObserver: BreakpointObserver, private auth: AuthService) {
    this.auth.loginStatusObs.subscribe(status => this.isLoggedIn = status)
  }

  title = 'sgpd-frontend';
}
