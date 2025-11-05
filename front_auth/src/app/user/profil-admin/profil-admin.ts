import { Component, OnInit, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface User {
  _id: string;
  email: string;
}

@Component({
  selector: 'app-profil-admin',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profil-admin.html',
  styleUrls: ['./profil-admin.css']
})
export class ProfilAdminComponent implements OnInit {
  private http = inject(HttpClient);
  users: User[] = [];
  loading = false;

  ngOnInit(): void {
    this.fetchUsers();
  }

  fetchUsers(): void {
    this.loading = true;
    this.http.get<User[]>('http://127.0.0.1:5000/api/user/').subscribe({
      next: data => {
        this.users = data;
        this.loading = false;
      },
      error: err => {
        console.error(err);
        this.loading = false;
      }
    });
  }

  deleteUser(id: string): void {
    if (confirm('Voulez-vous vraiment supprimer cet utilisateur ?')) {
      this.http.delete(`http://127.0.0.1:5000/api/user/${id}`).subscribe({
        next: () => this.fetchUsers(),
        error: err => console.error(err)
      });
    }
  }
}
