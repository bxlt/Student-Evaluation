import { Component, Input, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 't-sidebar',
  templateUrl: './t-sidebar.component.html',
  styleUrls: ['./t-sidebar.component.css']
})
export class TSidebarComponent {
  @Input() teamLogo = "assets/img/team.logo.jpg";
  @Input() teamName = "tPets";
  @Input() selected = "";
  ngOnInit() {
  }
}
