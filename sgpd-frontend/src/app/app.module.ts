// Angular Imports
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';

// Angular Material Imports
import { MatSliderModule } from '@angular/material/slider';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatCardModule } from '@angular/material/card';
import { MatMenuModule } from '@angular/material/menu';
import { MatInputModule } from '@angular/material/input'
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { LayoutModule } from '@angular/cdk/layout';
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatSnackBarModule } from '@angular/material/snack-bar';

// App components imports
import { LoginComponent } from './login/login.component';


// App services imports
import { AuthService } from './services/auth.service';
import { AlertService } from './services/alert.service';

// 3rd party packages
import { JwtModule, JwtHelperService } from '@auth0/angular-jwt';






@NgModule({
   declarations: [
      AppComponent,
      LoginComponent

   ],
   imports: [
      JwtModule,
      FormsModule,
      HttpClientModule,
      MatSliderModule,
      BrowserModule,
      AppRoutingModule,
      BrowserAnimationsModule,
      MatGridListModule,
      MatSnackBarModule,
      MatCardModule,
      MatMenuModule,
      MatProgressSpinnerModule,
      MatProgressBarModule,
      MatIconModule,
      MatButtonModule,
      LayoutModule,
      MatToolbarModule,
      MatSidenavModule,
      MatListModule,
      MatInputModule
   ],
   providers: [AuthService, JwtHelperService, AlertService
   ],
   bootstrap: [
      AppComponent
   ]
})
export class AppModule { }
