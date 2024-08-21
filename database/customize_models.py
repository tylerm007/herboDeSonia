from database import models
from safrs import jsonapi_attr
from sqlalchemy.orm import relationship, remote, foreign
from sqlalchemy.orm import Mapped
from typing import List
import logging

app_logger = logging.getLogger(__name__)

from database.database_discovery.auto_discovery import discover_models

discover_models()

"""
If you wish to drive models from the database schema,
you can use this file to customize your schema (add relationships, derived attributes),
and preserve customizations over iterations (regenerations of models.py).

Called from models.py (classes describing schema, per introspection).
# add relationship: https://docs.sqlalchemy.org/en/13/orm/join_conditions.html#specifying-alternate-join-conditions
models.Employee.Manager = relationship('Employee', 
    cascade_backrefs=False, backref='Manages',
    primaryjoin=remote(models.Employee.Id) == foreign(models.Employee.ReportsTo))

Your Code Goes Here
"""
# models.ComprasCAB.Manager = relationship(models.ComprasCAB,
#    cascade_backrefs=False, backref='Manages',
#    primaryjoin=remote(models.ComprasLIN.AlbarnCompra) == foreign(models.ComprasCAB.SerieNmero))
#: Mapped[List["VentasLIN"]]

# models.Cliente.Ventas_LIST  = relationship(models.VentasLIN, backref='Cliente')


"""
models.ComprasLIN.Compras_CAB = relationship(
    "ComprasCAB",
    cascade_backrefs=False,
    backref="Compras_LIN_List",
    primaryjoin=remote(models.ComprasCAB.SerieNmero)
    == foreign(models.ComprasLIN.AlbarnCompra),
)
"""
# GENERATED from LAC JSON !!!!
models.VentasLIN.Cliente = relationship(
    "Cliente",
    backref="Ventas_LIN_List",
    primaryjoin=remote(models.Cliente.NCuenta)
    == foreign(models.VentasLIN.NCuentaCliente),
)

models.ComprasLIN.Compras_CAB = relationship(
    "ComprasCAB",
    backref="Compras_LIN_List",
    primaryjoin=remote(models.ComprasCAB.SerieNmero) == foreign(models.ComprasLIN.AlbarnCompra),
)

models.ComprasLIN.Producto = relationship(
    "Producto",
    backref="Compras_LIN_List",
    primaryjoin=remote(models.Producto.Referencia) == foreign(models.ComprasLIN.ReferenciaProducto),
)
models.StockTienda.Producto_1 = relationship(
    "Producto",
    backref="StockTienda_List",
    primaryjoin=remote(models.Producto.Referencia)
    == foreign(models.StockTienda.Referencia),
)
models.TraspasosLIN.Producto_1 = relationship(
    "Producto",
    backref="Traspasos_LIN_List",
    primaryjoin=remote(models.Producto.Referencia)
    == foreign(models.TraspasosLIN.Referencia),
)
models.VentasLIN.Producto_1 = relationship(
    "Producto",
    backref="Ventas_LIN_List",
    primaryjoin=remote(models.Producto.Referencia)
    == foreign(models.VentasLIN.RefProducto),
)
models.ComprasCAB.Proveedor = relationship(
    "Proveedor",
    backref="Compras_CAB_List",
    primaryjoin=remote(models.Proveedor.NCuenta)
    == foreign(models.ComprasCAB.NCuentaProveedor),
)
models.ComprasLIN.Proveedor = relationship(
    "Proveedor",
    backref="Compras_LIN_List",
    primaryjoin=remote(models.Proveedor.NCuenta)
    == foreign(models.ComprasLIN.NCuentaProveedor),
)

models.ComprasLIN.StockTienda = relationship(
    "StockTienda",
    secondary="Compras_LIN",
    primaryjoin=(models.StockTienda.idTienda == models.ComprasLIN.idTienda),
    secondaryjoin=(models.StockTienda.Referencia == models.ComprasLIN.ReferenciaProducto),
    backref="Compras_LIN_List",
)
"""
models.ComprasLIN.StockTienda = relationship(
    "StockTienda",
    backref="Compras_LIN_List",
    primaryjoin=models.StockTienda.idTienda == models.StockTienda.Referencia],
    secondaryJoin=models.StockTienda.idTienda == models.ComprasLIN.ReferenciaProduct
)

models.TraspasosLIN.StockTienda = relationship("StockTienda",
    primaryjoin=remote(models.StockTienda.Referencia) == foreign(models.TraspasosLIN.Referencia),
    secondaryJoin=foreign(models.StockTienda.Referencia == models.TraspasosLIN.Destino),
    backref="Traspasos_LIN_List_DESTINO",
)


models.TraspasosLIN.StockTienda = relationship(
    "StockTienda",
    backref="Traspasos_LIN_List_DESTINO",
    primaryjoin=remote(models.StockTienda.Referencia)
    == foreign(models.TraspasosLIN.Referencia),
)
models.TraspasosLIN.StockTienda_1 = relationship(
    "StockTienda",
    backref="Traspasos_LIN_List_ORIGEN",
    primaryjoin=remote(models.StockTienda.Referencia)
    == foreign(models.TraspasosLIN.Referencia),
)
models.VentasLIN.StockTienda = relationship(
    "StockTienda",
    backref="Ventas_LIN_List",
    primaryjoin=remote(models.StockTienda.Referencia)
    == foreign(models.VentasLIN.RefProducto),
)
"""
models.VentasLIN.Ventas_CAB = relationship(
    "VentasCAB",
    backref="Ventas_LIN_List",
    primaryjoin=remote(models.VentasCAB.Nmero) == foreign(models.VentasLIN.Nmero),
)
