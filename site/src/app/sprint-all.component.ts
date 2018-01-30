import { Component, OnInit, AfterViewChecked, ViewChild } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { SprintComponent } from './sprint.component';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'sprint-all',
  templateUrl: './sprint-all.component.html',
  styleUrls: ['./sprint-all.component.css']
})
export class SprintAllComponent {
  sprintNum = 0;
  sprint = {
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
  found = true;
  constructor(private _route: ActivatedRoute,
    private _router: Router,
    private _http: Http,
    private _sanitizer: DomSanitizer) {
    this.getSprint(this._route.snapshot.params['num']);
  }

  getSidebarSelection() {
    return 'sprint_' + this.sprintNum;
  }

  ngAfterViewChecked() {
    
    if (this.sprintNum != this._route.snapshot.params['num']) {
      setTimeout(_=>this.getSprint(this._route.snapshot.params['num']));
    }
  }

  getSprint(id) {
    this.sprintNum = id;
    this.found = true;
    let url = 'assets/json/sprints/sprint_'+ this.sprintNum + '.json';
    this._http.get(url, {})
      .map((res) => res.json())
      .subscribe((res) => {
          console.log(res);
          if (res.code_review) {
            res.code_review.link = this._sanitizer.bypassSecurityTrustResourceUrl(res.code_review.link);
          }
          this.sprint = res;
        },
        (err) => {
            this.found = false
          });
  }
}
