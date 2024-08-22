#/bin/bash
# Test FreeSQL (no where clause)
# filter[key]=value
als login --user admin --password p
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_ventas_cab
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_traspasos_lin__rivas_vaciamadrid_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_compras_lin__rivas_vaciamadrid_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_compras_cab
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_compras_lin__santa_eugenia_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_compras_lin__barajas_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_producto
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_ventas_lin__palomeras_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_tienda
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_compras_lin__palomeras_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_compras_lin__ccomercial_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_traspasos_lin__palomeras_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_ventas_lin__santa_eugenia_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_cliente
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_ventas_lin__ccomercial_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_traspasos_lin__ccomercial_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_ventas_lin__barajas_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_proveedor
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_ventas_lin__ensanche_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_traspasos_lin
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_ventas_lin
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_compras_lin__ensanche_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_compras_lin
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_traspasos_lin__barajas_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_traspasos_lin__ensanche_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_traspasos_lin__santa_eugenia_sf
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_stocktienda
als curl http://localhost:5656/rest/default/herboDeSonia/v1/count_ventas_lin__rivas_vaciamadrid_sf
