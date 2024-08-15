import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductoHomeComponent } from './home/Producto-home.component';
import { ProductoNewComponent } from './new/Producto-new.component';
import { ProductoDetailComponent } from './detail/Producto-detail.component';

const routes: Routes = [
  {path: '', component: ProductoHomeComponent},
  { path: 'new', component: ProductoNewComponent },
  { path: ':Referencia', component: ProductoDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Producto-detail-permissions'
      }
    }
  }
];

export const PRODUCTO_MODULE_DECLARATIONS = [
    ProductoHomeComponent,
    ProductoNewComponent,
    ProductoDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductoRoutingModule { }