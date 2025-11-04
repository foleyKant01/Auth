import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-forgot-password',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './forgot-password.html',
  styleUrls: ['./forgot-password.css']
})
export class ForgotPasswordComponent {
  email = '';
  messageSent = false;
  
  private authService = inject(AuthService);
  private router = inject(Router);

  onSubmit(): void {
    if (!this.email) {
      alert('Veuillez entrer votre email');
      return;
    }

    // Le service auth.forgotPassword() appellera l'API backend
    if (this.authService.forgotPassword(this.email)) {
      this.messageSent = true;
    }
  }

  goToLogin(): void {
    this.router.navigate(['/login']);
  }
}