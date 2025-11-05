import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth';

@Component({
  selector: 'app-profil-admin',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profil-admin.html',
  styleUrls: ['./profil-admin.css']
})
export class ProfilAdminComponent implements OnInit {

  dataUsers: any[] = [];
  loading = true;

  constructor(
    private router: Router,
    private auth: AuthService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.Readalluser();
  }

  Readalluser(): void {
    this.loading = true;

    this.auth.ReadAllUser().subscribe({
      next: (response: any) => {
        if (response?.status === 'success' && response.users?.length) {
          this.dataUsers = response.users;
        } else {
          this.dataUsers = [];
        }
        this.loading = false;

        // ✅ Force Angular à recalculer après la mise à jour
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('Erreur lors de la récupération des utilisateurs:', err);
        this.loading = false;
        this.dataUsers = [];
        this.cdr.detectChanges();
      }
    });
  }

  Deleteuser(uid: any): void {
    if (confirm('Êtes-vous sûr de vouloir supprimer cet utilisateur ?')) {
      this.auth.DeleteUser(uid).subscribe({
        next: (response: any) => {
          console.log('User deleted successfully:', response);
          this.Readalluser(); // recharge la liste
        },
        error: (error) => {
          console.error('Failed to delete user:', error);
        }
      });
    }
  }
}
