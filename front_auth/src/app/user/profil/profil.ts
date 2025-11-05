import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { ProfilAdminComponent } from '../profil-admin/profil-admin';

@Component({
  selector: 'app-profil',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule,RouterLink,ProfilAdminComponent],
  templateUrl: './profil.html',
  styleUrl: './profil.css',
})
export class ProfilComponent implements OnInit{

  user_infos: any
  email: any

  ngOnInit(): void {
    const user = sessionStorage.getItem('user_infos');
    this.user_infos = user
    console.log(this.user_infos);
    if (user) {
      this.user_infos = JSON.parse(user); // Convertir en objet
      this.email = this.user_infos.email
      console.log('email:', this.email);
  }

}

logout() {
  localStorage.removeItem('user_infos');
  window.location.href = '/user/home';
}

}

