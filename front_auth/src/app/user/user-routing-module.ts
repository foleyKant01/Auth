import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home';
import { UserComponent } from './user';
import { LoginComponent } from './login/login';
import { RegisterComponent } from './register/register';
import { ForgotPasswordComponent } from './forgot-password/forgot-password';
import { ProfilComponent } from './profil/profil';

const routes: Routes = [
   { path:'', component: UserComponent,
    children: [
      { path:'', redirectTo:'home', pathMatch:'full' },
      { path:'home', component: HomeComponent },
      { path:'profil', component: ProfilComponent },
      { path:'login', component: LoginComponent },
      { path:'register', component: RegisterComponent },
      { path:'forgot-password', component: ForgotPasswordComponent },
      { path:'admin', component: ProfilComponent },
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UserRoutingModule { }
