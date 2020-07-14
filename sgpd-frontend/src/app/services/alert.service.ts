import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class AlertService {

  constructor(private snack: MatSnackBar) { }

  showSnackBar(message) {
    this.snack.open(message, "Cerrar", {
      duration: 2000,
    });
  }

}
