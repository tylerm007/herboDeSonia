import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StockTiendaHomeComponent } from './home/StockTienda-home.component';
import { StockTiendaNewComponent } from './new/StockTienda-new.component';
import { StockTiendaDetailComponent } from './detail/StockTienda-detail.component';

const routes: Routes = [
  {path: '', component: StockTiendaHomeComponent},
  { path: 'new', component: StockTiendaNewComponent },
  { path: ':Referencia/:idTienda', component: StockTiendaDetailComponent,
    data: {
      oPermission: {
        permissionId: 'StockTienda-detail-permissions'
      }
    }
  }
];

export const STOCKTIENDA_MODULE_DECLARATIONS = [
    StockTiendaHomeComponent,
    StockTiendaNewComponent,
    StockTiendaDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StockTiendaRoutingModule { }