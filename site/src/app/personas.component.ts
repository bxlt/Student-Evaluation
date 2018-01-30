import { Component, OnInit } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { ActivatedRoute } from '@angular/router';
import { ConstantsService } from './constants.service';
import { Router } from '@angular/router';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
declare var $: any;

@Component({
  selector: 'personas',
  templateUrl: './personas.component.html',
  styleUrls: ['./personas.component.css']
})
export class PersonasComponent {
  sideSelected = "";
  personas:any[] = [];
  versions = [];
  found = true;
  selectedVersion;

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
    this._router.navigate( ['/persona/' + vers]);
    this.found = true;
    this._http.get('assets/json/personas/persona_v'+vers+'.json', {})
      .map((res) => res.json())
      .subscribe((res) => {
          this.personas = res;
          this.selectedVersion = vers;
          $('#persona_menu').sticky({
            context: '#persona_content',
            observeChanges: true
          });
        },
        (err) =>  this.found = false);
  }
}
