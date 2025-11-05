import { Component, inject, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { AuthService } from '../../services/auth';
import { CommonModule } from '@angular/common';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';

declare var bootstrap: any;


@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule, RouterModule],
  templateUrl: './register.html',
  styleUrls: ['./register.css']
})
export class RegisterComponent implements OnInit{


  constructor(private router: Router, private _activateRouter: ActivatedRoute, private auth: AuthService) { }
  
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }


  createuser: FormGroup = new FormGroup(
  {
    email: new FormControl(null, Validators.required),
    password: new FormControl(null, Validators.required),
    motpreferer: new FormControl(null, Validators.required),
    role: new FormControl(null, Validators.required),
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
          this.router.navigate(['/user/login']);
        } 
        else {
          console.error('Erreur :', res);
          console.error('Description :', res);
      
        }
      },
    })
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
