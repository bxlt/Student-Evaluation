import { Component, Input } from '@angular/core';

@Component({
  selector: 't-notfound-item',
  templateUrl: './t-notfound-item.component.html',
  styleUrls: ['./t-notfound-item.component.css']
})
export class TNotFoundItemComponent {
  @Input() msg = "The item you are looking for does not exist.";
}
