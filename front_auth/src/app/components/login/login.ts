import { Component, inject, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from '../../services/auth';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';

declare var bootstrap: any;


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class LoginComponent implements OnInit{

  constructor(private router: Router, private _activateRouter: ActivatedRoute, private auth: AuthService) { }
  
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }

  login_form: FormGroup = new FormGroup({
    email: new FormControl(null, Validators.required),
    password: new FormControl(null, Validators.required),
  });
  
  Loginuser(): void {
    if (!this.login_form?.valid) {
      alert('Veuillez remplir tous les champs');
      return;
    }
    const credentials = this.login_form.value;

    this.auth.LoginUser(credentials).subscribe({
      next: (res: any) => {
        console.log('Réponse du serveur :', res);
        if (res?.status === 'success') {
          console.log("Redirection vers la page profil");
          this.router.navigate(['/user/home']);
          this.showSuccessToast('Connexion réussie !');

        } 
        else {
          console.error('Données incorrecte, la réponse :', res);
          this.showErrorToast("Informations d'utilisateur incorrecte. Veuillez réessayer.");

        }
      },
      error: (err) => {
        console.error('Erreur lors de la requête :', err);
        const errorMessage =
          err?.error?.message ||
          err?.message ||
          'Une erreur est survenue lors de la connexion. Veuillez réessayer.';
        this.showErrorToast(errorMessage);
      },

    });
  }

  goToRegister(): void {
    this.router.navigate(['/register']);
  }

  goToForgotPassword(): void {
    this.router.navigate(['/forgot-password']);
  }

    showSuccessToast(message: string) {
    const toastBody = document.getElementById('successToastBody');
    if (toastBody) {
      toastBody.textContent = message;
    } else {
      console.warn('Success toast body element not found.');
    }
    const toastElement = document.getElementById('successToast');
    const toast = new bootstrap.Toast(toastElement, { delay: 2000 });
    toast.show();
  }

  showErrorToast(message: string) {
    const toastBody = document.getElementById('errorToastBody');
    if (toastBody) {
      toastBody.textContent = message;
    } else {
      console.warn('Error toast body element not found.');
    }
    const toastElement = document.getElementById('errorToast');
    const toast = new bootstrap.Toast(toastElement, { delay: 2000 });
    toast.show();
  }
}