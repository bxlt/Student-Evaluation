import { Component, OnInit, Input } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'sprint',
  templateUrl: './sprint.component.html',
  styleUrls: ['./sprint.component.css']
})
export class SprintComponent {
  @Input() sprintNum = 0;
  @Input() found = true;
  @Input() sprint = {
    user_story: [],
    task_division: {
      Bill: [],
      Vethursan: [],
      Kevin: [],
      Rakin: []
    },
    tasks: [],
    versions: {}
  }
}
