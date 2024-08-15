import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'VentasCAB-new',
  templateUrl: './VentasCAB-new.component.html',
  styleUrls: ['./VentasCAB-new.component.scss']
})
export class VentasCABNewComponent {
  @ViewChild("VentasCABForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}