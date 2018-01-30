import { Component, OnInit, HostListener, Input } from '@angular/core';
import { Router } from '@angular/router';
declare var $: any;

@Component({
  selector: 'homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomePageComponent {
  @Input() teamName = "tPets";
  @Input() teamLogo = "assets/img/team.logo.jpg";
  openMenu = true;
  selectedAgreement = 0;

  constructor(private router: Router) {}
  @HostListener('window:scroll', ['$event'])
  menuWatch(event) {
    this.openMenu = window.pageYOffset === 0;
  }

  ngOnInit() {
    $('.home_menu.sidebar').sidebar({
      transition: 'overlay',
      duration: 300,
      silent: true
    });
    console.log(this.router);
  }

  toggleSidebar() {
    $('.home_menu.sidebar').sidebar('toggle');
  }
  navigateTo(url) {
    window.location.href = window.location.origin + url;
  }
}
