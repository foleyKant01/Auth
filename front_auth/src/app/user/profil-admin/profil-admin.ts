import { Component, OnInit, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';
import { AuthService } from '../../services/auth';

@Component({
  selector: 'app-profil-admin',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profil-admin.html',
  styleUrls: ['./profil-admin.css']
})
export class ProfilAdminComponent implements OnInit {

  allUsers: string[] = [];
  dataUsers: any[] = [];
  loading = false;

  ngOnInit(): void {
    this.Readalluser()
  }

  constructor(private router: Router, private auth: AuthService) { }


Readalluser(): void {
  this.loading = true;

  this.auth.ReadAllUser().subscribe({
    next: (response: { status: string; users?: any[]; [key: string]: any }) => {
      this.loading = false;

      if (response?.status === 'success' && response.users?.length) {
        this.dataUsers = response.users;
        console.log('Users loaded:', this.dataUsers);
      } else {
        this.dataUsers = [];
        console.warn('Aucun utilisateur trouvé ou réponse invalide:', response);
      }
    },
    error: (err) => {
      this.loading = false;
      this.dataUsers = [];
      console.error('Erreur lors de la récupération des utilisateurs:', err);
    }
  });
}

  Deleteuser(uid: any): void {
    if (confirm('Êtes-vous sûr de vouloir supprimer cet utilisateur ?')) {
      this.auth.DeleteUser(uid).subscribe({
        next: (response: any) => {
          console.log('User deleted successfully:', response);
          // Retirer l’utilisateur de la liste affichée sans recharger la page
          this.dataUsers = this.dataUsers.filter(user => user.uid !== uid);
        },
        error: (error) => {
          console.error('Failed to delete user:', error);
        }
      });
    }
  }

}
