#=============================================================================================
#    als command line tests for each table endpoint ?page[limit]=10&page[offset]=00&filter[key]=value
#=============================================================================================

#
#als login http://localhost:5656 -u admin -p p

# als calling endpoint: Cliente?page[limit]=1
als curl   "http://localhost:5656/api/Cliente?page%5Blimit%5D=1" 


# als calling endpoint: Compras_CAB?page[limit]=1
als curl   "http://localhost:5656/api/ComprasCAB?page%5Blimit%5D=1" 


# als calling endpoint: Compras_LIN?page[limit]=1
als curl   "http://localhost:5656/api/ComprasLIN?page%5Blimit%5D=1" 


# als calling endpoint: Producto?page[limit]=1
als curl   "http://localhost:5656/api/Producto?page%5Blimit%5D=1" 


# als calling endpoint: Proveedor?page[limit]=1
als curl   "http://localhost:5656/api/Proveedor?page%5Blimit%5D=1" 


# als calling endpoint: StockTienda?page[limit]=1
als curl   "http://localhost:5656/api/StockTienda?page%5Blimit%5D=1" 


# als calling endpoint: Tienda?page[limit]=1
als curl   "http://localhost:5656/api/Tienda?page%5Blimit%5D=1" 


# als calling endpoint: Traspasos_LIN?page[limit]=1
als curl   "http://localhost:5656/api/TraspasosLIN?page%5Blimit%5D=1" 


# als calling endpoint: Ventas_CAB?page[limit]=1
als curl "http://localhost:5656/api/VentasCAB?page%5Blimit%5D=1" 


# als calling endpoint: Ventas_LIN?page[limit]=1
als curl   "http://localhost:5656/api/VentasLIN?page%5Blimit%5D=1" 


