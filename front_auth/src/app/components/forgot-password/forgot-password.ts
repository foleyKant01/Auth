import { Component, inject } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from '../../services/auth';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-forgot-password',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule],
  templateUrl: './forgot-password.html',
  styleUrls: ['./forgot-password.css']
})
export class ForgotPasswordComponent {
  
  constructor(private router: Router, private _activateRouter: ActivatedRoute, private auth: AuthService) { }


  passwordform: FormGroup = new FormGroup(
  {
    email: new FormControl(null, Validators.required),
    password: new FormControl(null, Validators.required),
    newpassword: new FormControl(null, Validators.required),
    confirmpassword: new FormControl(null, Validators.required),
  }
  )

  Savenewpassword(){
    if (!this.passwordform?.valid) {
      alert('Veuillez remplir tous les champs');
      return;
    }
    this.auth.SaveNewPassword(this.passwordform.value).subscribe({
      next: (res: any) => {
        console.log('Réponse du serveur :', res);
        if (res?.status === 'success') {
          console.log("Redirection vers la page profil");
          this.router.navigate(['/user/home']);
        } 
        else {
          console.error('Erreur :', res);
          console.error('Description :', res);
        }
      },
    })
  }
}