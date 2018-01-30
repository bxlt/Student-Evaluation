import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RoutingModule } from './routing.module';
import { SmoothScrollToDirective, SmoothScrollDirective } from "ng2-smooth-scroll";

import { AppComponent } from './app.component';
import { HomePageComponent } from './homepage.component';
import { TeamAgreementComponent } from './team-agreement.component';
import { TSidebarComponent } from './t-sidebar.component';
import { DeliverablesComponent } from './deliverables.component';
import { PersonasComponent } from './personas.component';
import { UserStoryComponent } from './user-story.component';
import { TPetsFooterComponent } from './tpets-footer.component';
import { TNotFoundItemComponent } from './t-notfound-item.component';
import { SprintComponent } from './sprint.component';
import { SprintAllComponent } from './sprint-all.component';
import { ValidationComponent } from './validation.component';
import { ConstantsService } from './constants.service';

@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    TeamAgreementComponent,
    DeliverablesComponent,
    TSidebarComponent,
    PersonasComponent,
    UserStoryComponent,
    TPetsFooterComponent,
    TNotFoundItemComponent,
    SprintComponent,
    SprintAllComponent,
    SmoothScrollToDirective,
    SmoothScrollDirective,
    ValidationComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RoutingModule
  ],
  providers: [
    ConstantsService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
