import { Component, Input } from '@angular/core';

@Component({
  selector: 'tpets-footer',
  templateUrl: './tpets-footer.component.html',
  styleUrls: ['./tpets-footer.component.css']
})
export class TPetsFooterComponent {
  @Input() teamLogo = "assets/img/team.logo.jpg";
  @Input() teamName = "tPets";
}
