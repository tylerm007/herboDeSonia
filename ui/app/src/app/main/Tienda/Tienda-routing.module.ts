import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TiendaHomeComponent } from './home/Tienda-home.component';
import { TiendaNewComponent } from './new/Tienda-new.component';
import { TiendaDetailComponent } from './detail/Tienda-detail.component';

const routes: Routes = [
  {path: '', component: TiendaHomeComponent},
  { path: 'new', component: TiendaNewComponent },
  { path: ':STOREDVALUE', component: TiendaDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Tienda-detail-permissions'
      }
    }
  }
];

export const TIENDA_MODULE_DECLARATIONS = [
    TiendaHomeComponent,
    TiendaNewComponent,
    TiendaDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TiendaRoutingModule { }