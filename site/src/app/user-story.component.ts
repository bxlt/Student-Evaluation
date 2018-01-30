import { Component, OnInit } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { ConstantsService } from './constants.service';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
declare var $: any;

@Component({
  selector: 'user-story',
  templateUrl: './user-story.component.html',
  styleUrls: ['./user-story.component.css']
})
export class UserStoryComponent {
  showLegend = false;
  versions = [];
  selectedVersion;
  found = true;
  userStories;
  statusClass = {
    "Epic": "violet",
    "Pending": "blue",
    "New": "yellow",
    "In-Progress": "olive",
    "On-hold": "orange",
    "Deleted": "grey",
    "Completed": "green"
  };
  sorted = 'asc';
  constructor(private _http: Http,
    private _const: ConstantsService,
    private _route: ActivatedRoute,
    private _router: Router) {}

  ngOnInit() {
    this.selectedVersion = this._route.snapshot.params['version'];
    if (isNaN(this.selectedVersion)) {
      this.found = false;
    } else {
      this.switchVersion(this.selectedVersion);
      this.versions = this._const.get('versions');
    }
  }


  switchVersion(vers) {
    this._router.navigate( ['/user_story/' + vers]);
    this.found = true;
    this._http.get('assets/json/user_story/user_story_v'+vers+'.json', {})
      .map((res) => res.json())
      .subscribe((res) => {
          this.userStories = res.map((s) => {
            if (s.priority >= 80) {
              s.class = "one";
            } else if (s.priority >= 60) {
              s.class = "two";
            } else if (s.priority >= 40) {
              s.class = "three";
            } else if (s.priority >= 20) {
              s.class = "four";
            } else if (s.priority >= 0) {
              s.class = "five";
            }
            return s;
          }).sort((a, b) => b.priority - a.priority);
          this.sorted = 'asc';
          this.selectedVersion = vers;
        },
        (err) =>  {
          this.found = false
        });
  }

  sortUserStories() {
    if (this.sorted == 'asc') {
      this.userStories.sort((a, b) => a.priority - b.priority);
      this.sorted = 'desc';
    } else {
      this.userStories.sort((a, b) => b.priority - a.priority);
      this.sorted = 'asc';
    }
  }

}
