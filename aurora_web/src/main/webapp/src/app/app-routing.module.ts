import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

import { PredictorComponent } from './predictor/predictor.component';
import { AdminComponent } from './admin/admin.component';
import { StatasticsComponent } from './statastics/statastics.component'

const routes: Routes = [
  { path: '', redirectTo: 'predict', pathMatch: 'full' },
  { path: 'predict', component: PredictorComponent },
  { path: 'statastics', component: StatasticsComponent }
  // { path: '', component: '' }
  // {path:'',component:'AdminComponent'}
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
