import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProveedorHomeComponent } from './home/Proveedor-home.component';
import { ProveedorNewComponent } from './new/Proveedor-new.component';
import { ProveedorDetailComponent } from './detail/Proveedor-detail.component';

const routes: Routes = [
  {path: '', component: ProveedorHomeComponent},
  { path: 'new', component: ProveedorNewComponent },
  { path: ':NCuenta', component: ProveedorDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Proveedor-detail-permissions'
      }
    }
  }
];

export const PROVEEDOR_MODULE_DECLARATIONS = [
    ProveedorHomeComponent,
    ProveedorNewComponent,
    ProveedorDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProveedorRoutingModule { }