import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './homepage.component';
import { TeamAgreementComponent } from './team-agreement.component';
import { DeliverablesComponent } from './deliverables.component';
import { PersonasComponent } from './personas.component';
import { UserStoryComponent } from './user-story.component';
import { SprintAllComponent } from './sprint-all.component';
import { ValidationComponent } from './validation.component';

const routes: Routes = [{
    path: 'home',
    component: HomePageComponent
  },{
    path: 'deliverables',
    component: DeliverablesComponent
  },{    
    path: 'agreement',
    component: TeamAgreementComponent
  },{
    path: 'user_story/:version',
    component: UserStoryComponent
  },{
    path: 'user_story',
    redirectTo: '/user_story/0'
  },{
    path: 'persona/:version',
    component: PersonasComponent
  },{
    path: 'persona',
    redirectTo: '/persona/0'
  },{
    path: 'sprint/:num',
    component: SprintAllComponent
  },{
    path: 'code_review',
    component: ValidationComponent
  },{    
    path: '**',
    redirectTo: '/home'
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(
      routes
    )
  ],
  exports: [
    RouterModule
  ],
  providers: []
})
export class RoutingModule { }