import { Injectable } from '@angular/core';

@Injectable()
export class ConstantsService {
  private constants: any = {
    versions: [{
      code: '0',
      display: '0.0'
    },{
      code: '1',
      display: '1.0'
    },{
      code: '2',
      display: '2.0'
    },{
      code: '3',
      display: '3.0'
    },{
      code: '4',
      display: '4.0'
    }]
  }
  constructor() { }

  get(key) {
    return this.constants[key];
  }
}