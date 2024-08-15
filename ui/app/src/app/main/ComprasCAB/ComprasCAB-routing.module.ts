import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ComprasCABHomeComponent } from './home/ComprasCAB-home.component';
import { ComprasCABNewComponent } from './new/ComprasCAB-new.component';
import { ComprasCABDetailComponent } from './detail/ComprasCAB-detail.component';

const routes: Routes = [
  {path: '', component: ComprasCABHomeComponent},
  { path: 'new', component: ComprasCABNewComponent },
  { path: ':idCabCompras', component: ComprasCABDetailComponent,
    data: {
      oPermission: {
        permissionId: 'ComprasCAB-detail-permissions'
      }
    }
  }
];

export const COMPRASCAB_MODULE_DECLARATIONS = [
    ComprasCABHomeComponent,
    ComprasCABNewComponent,
    ComprasCABDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ComprasCABRoutingModule { }