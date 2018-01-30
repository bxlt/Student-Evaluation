import { Component, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 'team-agreement',
  templateUrl: './team-agreement.component.html',
  styleUrls: ['./team-agreement.component.css']
})
export class TeamAgreementComponent {
  sideSelected = "";
  ngOnInit() {
    $('#agreement_menu').sticky({
      context: '#agreement_content'
    });
    $('#phone_call').popup();
  }
}
