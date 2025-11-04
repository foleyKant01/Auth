import { Injectable, inject } from '@angular/core';
import { Router } from '@angular/router';

export interface User {
  email: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly STORAGE_KEY = 'currentUser';
  private router = inject(Router);

  // Connexion - À REMPLACER par appel API backend
  login(email: string, password: string): boolean {
    // TODO: Remplacer par this.http.post('API_URL/login', {email, password})
    console.log('Login appelé avec:', { email, password });
    
    // Simulation pour le frontend
    localStorage.setItem(this.STORAGE_KEY, JSON.stringify({ email }));
    return true;
  }

  // Inscription - À REMPLACER par appel API backend
  register(email: string, password: string): boolean {
    // TODO: Remplacer par this.http.post('API_URL/register', {email, password})
    console.log('Register appelé avec:', { email, password });
    return true;
  }

  // Mot de passe oublié - À REMPLACER par appel API backend
  forgotPassword(email: string): boolean {
    // TODO: Remplacer par this.http.post('API_URL/forgot-password', {email})
    console.log('Forgot password appelé avec:', { email });
    return true;
  }

  // Déconnexion
  logout(): void {
    localStorage.removeItem(this.STORAGE_KEY);
    this.router.navigate(['/']);
  }

  // Vérifier si l'utilisateur est connecté
  isLoggedIn(): boolean {
    return localStorage.getItem(this.STORAGE_KEY) !== null;
  }

  // Obtenir l'utilisateur actuel
  getCurrentUser(): User | null {
    const userJson = localStorage.getItem(this.STORAGE_KEY);
    return userJson ? JSON.parse(userJson) : null;
  }
}