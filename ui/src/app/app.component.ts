import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <app-home></app-home>
    <router-outlet></router-outlet>
  `,
  styles: []
})
export class AppComponent {

  constructor() {}
  title = 'ui';

  ngOnInit() {}
}
