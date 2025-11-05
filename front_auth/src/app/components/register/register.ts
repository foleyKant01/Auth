import { Component, inject } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from '../../services/auth';
import { CommonModule } from '@angular/common';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule],
  templateUrl: './register.html',
  styleUrls: ['./register.css']
})
export class RegisterComponent {

  constructor(private router: Router, private _activateRouter: ActivatedRoute, private auth: AuthService) { }


  createuser: FormGroup = new FormGroup(
  {
    email: new FormControl(null, Validators.required),
    password: new FormControl(null, Validators.required),
    confirmpassword: new FormControl(null, Validators.required),
  }
  )

  Createuser(){
    if (!this.createuser?.valid) {
      alert('Veuillez remplir tous les champs');
      return;
    }
    this.auth.CreateUser(this.createuser.value).subscribe({
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
