# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, DECIMAL, Date, DateTime, Float, Index, Integer, SmallInteger, String, Text
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  September 03, 2024 09:29:48
# Database: mysql+pymysql://root:p@localhost:3306/herboDeSonia?charset=utf8mb4
# Dialect:  mysql
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.mysql import *



class Cliente(SAFRSBaseX, Base):
    __tablename__ = 'Cliente'
    _s_collection_name = 'Cliente'  # type: ignore
    __bind_key__ = 'None'

    Tipo = Column('Tipo', Text(collation='utf8mb4_general_ci'), quote = True)
    FechaAlta = Column('FechaAlta', Date, quote = True)
    TipoCliente = Column('TipoCliente', Text(collation='utf8mb4_general_ci'), quote = True)
    DNI_CIF = Column('DNI_CIF', Text(collation='utf8mb4_general_ci'), quote = True)
    BIC = Column('BIC', Text(collation='utf8mb4_general_ci'), quote = True)
    IBAN = Column('IBAN', Text(collation='utf8mb4_general_ci'), quote = True)
    NCuenta = Column('NCuenta', Integer, primary_key=True, quote = True)
    NombreCorto = Column('NombreCorto', Text(collation='utf8mb4_general_ci'), quote = True)
    NombreCompleto = Column('NombreCompleto', Text(collation='utf8mb4_general_ci'), quote = True)
    Calle = Column('Calle', Text(collation='utf8mb4_general_ci'), quote = True)
    ExtCalle = Column('ExtCalle', Text(collation='utf8mb4_general_ci'), quote = True)
    Localidad = Column('Localidad', Text(collation='utf8mb4_general_ci'), quote = True)
    Provincia = Column('Provincia', Text(collation='utf8mb4_general_ci'), quote = True)
    CodPostal = Column('CodPostal', Text(collation='utf8mb4_general_ci'), quote = True)
    Tlf = Column('Tlf', Text(collation='utf8mb4_general_ci'), quote = True)
    Email = Column('Email', Text(collation='utf8mb4_general_ci'), quote = True)
    Web = Column('Web', Text(collation='utf8mb4_general_ci'), quote = True)
    FPago = Column('FPago', Text(collation='utf8mb4_general_ci'), quote = True)
    CC = Column('CC', Text(collation='utf8mb4_general_ci'), quote = True)
    DtoGl = Column('DtoGl', Text(collation='utf8mb4_general_ci'), quote = True)
    NCopFact = Column('NCopFact', Text(collation='utf8mb4_general_ci'), quote = True)
    Contacto = Column('Contacto', Text(collation='utf8mb4_general_ci'), quote = True)
    Recomendado = Column('Recomendado', Text(collation='utf8mb4_general_ci'), quote = True)
    Comentarios = Column('Comentarios', Text(collation='utf8mb4_general_ci'), quote = True)
    Notific = Column('Notific', Text(collation='utf8mb4_general_ci'), quote = True)
    DeBaja = Column('DeBaja', Text(collation='utf8mb4_general_ci'), quote = True)
    FechaBaja = Column('FechaBaja', Date, quote = True)
    CreadorPor = Column('CreadorPor', Text(collation='utf8mb4_general_ci'), quote = True)
    SumaVentas = Column('SumaVentas', DECIMAL(11, 2), quote = True)
    PuntosGenerados = Column('PuntosGenerados', Integer, quote = True)
    PuntosUsados = Column('PuntosUsados', Integer, quote = True)
    SaldoParaPuntos = Column('SaldoParaPuntos', DECIMAL(11, 2), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class ComprasCAB(SAFRSBaseX, Base):
    __tablename__ = 'Compras_CAB'
    _s_collection_name = 'ComprasCAB'  # type: ignore
    __bind_key__ = 'None'

    SerieNmero = Column('SerieNmero', String(11, 'utf8mb4_general_ci'), unique=True, quote = True)
    Fecha = Column('Fecha', DateTime, index=True, quote = True)
    RaznSocial = Column('RaznSocial', Text(collation='utf8mb4_general_ci'), quote = True)
    BaseImponible = Column('BaseImponible', DECIMAL(11, 2), quote = True)
    ImporteIVA = Column('ImporteIVA', DECIMAL(11, 2), quote = True)
    ImporteRecargoEq = Column('ImporteRecargoEq', DECIMAL(11, 2), quote = True)
    TotalAlbCompra = Column('TotalAlbCompra', DECIMAL(11, 2), quote = True)
    idCabCompras = Column('idCabCompras', Integer, primary_key=True, quote = True)
    ImporteIVAReducido = Column('ImporteIVAReducido', DECIMAL(11, 2), quote = True)
    ImporteIVASuperReducido = Column('ImporteIVASuperReducido', DECIMAL(11, 2), quote = True)
    ImporteIVAAceitesPastas = Column('ImporteIVAAceitesPastas', DECIMAL(11, 2), quote = True)
    BaseIVAReducido = Column('BaseIVAReducido', DECIMAL(11, 2), quote = True)
    BaseIVASuperReducido = Column('BaseIVASuperReducido', DECIMAL(11, 2), quote = True)
    BaseIVAAceitesPastas = Column('BaseIVAAceitesPastas', DECIMAL(11, 2), quote = True)
    BaseIVACero = Column('BaseIVACero', DECIMAL(11, 2), quote = True)
    ImporteIVAGeneral = Column('ImporteIVAGeneral', DECIMAL(11, 2), quote = True)
    BaseIVAGeneral = Column('BaseIVAGeneral', DECIMAL(11, 2), quote = True)
    TotalAlbCalculado = Column('TotalAlbCalculado', DECIMAL(11, 2), quote = True)
    tpcDtoProntoPago = Column('tpcDtoProntoPago', DECIMAL(5, 2), quote = True)
    tpcDtoGlobal = Column('tpcDtoGlobal', DECIMAL(5, 2), quote = True)
    Tienda = Column('Tienda', Text(collation='utf8mb4_general_ci'), quote = True)
    NCuentaProveedor = Column('NCuentaProveedor', Integer, quote = True)
    idTienda = Column('idTienda', SmallInteger, quote = True)

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class ComprasLIN(SAFRSBaseX, Base):
    __tablename__ = 'Compras_LIN'
    _s_collection_name = 'ComprasLIN'  # type: ignore
    __bind_key__ = 'None'
    __table_args__ = (
        Index('Fk_Producto', 'idTienda', 'ReferenciaProducto'),
    )

    Tienda = Column('Tienda', Text(collation='utf8mb4_general_ci'), quote = True)
    NmeroAlbarn = Column('NmeroAlbarn', Integer, quote = True)
    AlbarnCompra = Column('AlbarnCompra', String(11, 'utf8mb4_general_ci'), index=True, quote = True)
    NombreProveedor = Column('NombreProveedor', Text(collation='utf8mb4_general_ci'), quote = True)
    FechaAlbarn = Column('FechaAlbarn', DateTime, quote = True)
    ImporteAlbarn = Column('ImporteAlbarn', DECIMAL(11, 2), quote = True)
    ReferenciaProducto = Column('ReferenciaProducto', Integer, quote = True)
    OLDReferenciaProducto = Column('OLDReferenciaProducto', Text(collation='utf8mb4_general_ci'), quote = True)
    DescripciondelProducto = Column('DescripciondelProducto', Text(collation='utf8mb4_general_ci'), quote = True)
    CdigodeBarras = Column('CdigodeBarras', BigInteger, quote = True)
    Cantidad = Column('Cantidad', Integer, quote = True)
    PVPProducto = Column('PVPProducto', DECIMAL(11, 2), quote = True)
    PrecioLnea = Column('PrecioLnea', DECIMAL(11, 2), quote = True)
    tpcIVA = Column('tpcIVA', DECIMAL(11, 2), quote = True)
    tpcDescuento1 = Column('tpcDescuento1', DECIMAL(5, 2), quote = True)
    tpcDescuento2 = Column('tpcDescuento2', DECIMAL(5, 2), quote = True)
    tpcDescuento3 = Column('tpcDescuento3', DECIMAL(5, 2), quote = True)
    tpcDescuento4 = Column('tpcDescuento4', DECIMAL(5, 2), quote = True)
    tpcDtoGlobal = Column('tpcDtoGlobal', DECIMAL(5, 2), quote = True)
    tpcDtoProntoPago = Column('tpcDtoProntoPago', DECIMAL(5, 2), quote = True)
    Id = Column('id', Integer, primary_key=True, quote = True)
    Importe = Column('Importe', DECIMAL(11, 2), quote = True)
    NCuentaProveedor = Column('NCuentaProveedor', Integer, quote = True)
    CantidadConCoste = Column('CantidadConCoste', Integer, quote = True)
    CantidadGratis = Column('CantidadGratis', Integer, quote = True)
    PrecioCoste = Column('PrecioCoste', DECIMAL(11, 2), quote = True)
    Lote = Column('Lote', String(20, 'utf8mb4_general_ci'), quote = True)
    idTienda = Column('idTienda', SmallInteger, quote = True)
    FechaInventario = Column('FechaInventario', DateTime, quote = True)

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Producto(SAFRSBaseX, Base):
    __tablename__ = 'Producto'
    _s_collection_name = 'Producto'  # type: ignore
    __bind_key__ = 'None'

    Referencia = Column('Referencia', Integer, primary_key=True, quote = True)
    Descripcion = Column('Descripcion', Text(collation='utf8mb4_general_ci'), quote = True)
    DescripcionBreve = Column('DescripcionBreve', Text(collation='utf8mb4_general_ci'), quote = True)
    CodBarras = Column('CodBarras', Text(collation='utf8mb4_general_ci'), quote = True)
    CodGenerico = Column('CodGenerico', Text(collation='utf8mb4_general_ci'), quote = True)
    FechaCreacion = Column('FechaCreacion', Text(collation='utf8mb4_general_ci'), quote = True)
    PVP = Column('PVP', Float, quote = True)
    PrecioCoste = Column('PrecioCoste', Float, quote = True)
    Familia = Column('Familia', Text(collation='utf8mb4_general_ci'), quote = True)
    SubFam = Column('SubFam', Text(collation='utf8mb4_general_ci'), quote = True)
    Stock = Column('Stock', Float, quote = True)
    Ubicacion = Column('Ubicacion', Text(collation='utf8mb4_general_ci'), quote = True)
    IVA = Column('IVA', Text(collation='utf8mb4_general_ci'), quote = True)
    Marca = Column('Marca', Text(collation='utf8mb4_general_ci'), quote = True)
    Proveedor = Column('Proveedor', Text(collation='utf8mb4_general_ci'), quote = True)
    Descatalogado = Column('Descatalogado', Text(collation='utf8mb4_general_ci'), quote = True)
    PublicarWeb = Column('PublicarWeb', Text(collation='utf8mb4_general_ci'), quote = True)
    OfertaWeb = Column('OfertaWeb', Text(collation='utf8mb4_general_ci'), quote = True)
    NovedadWeb = Column('NovedadWeb', Text(collation='utf8mb4_general_ci'), quote = True)
    tipoIVA = Column('tipoIVA', SmallInteger, quote = True)
    FechaUltPVP = Column('FechaUltPVP', DateTime, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Proveedor(SAFRSBaseX, Base):
    __tablename__ = 'Proveedor'
    _s_collection_name = 'Proveedor'  # type: ignore
    __bind_key__ = 'None'

    DNICIF = Column('DNICIF', Text(collation='utf8mb4_general_ci'), quote = True)
    RSocial = Column('RSocial', Text(collation='utf8mb4_general_ci'), quote = True)
    TipoProv = Column('TipoProv', Text(collation='utf8mb4_general_ci'), quote = True)
    FPago = Column('FPago', Text(collation='utf8mb4_general_ci'), quote = True)
    Facturacin = Column('Facturación', Text(collation='utf8mb4_general_ci'), quote = True)
    Provincia = Column('Provincia', Text(collation='utf8mb4_general_ci'), quote = True)
    NCuenta = Column('NºCuenta', Integer, primary_key=True, quote = True)
    Calle = Column('Calle', Text(collation='utf8mb4_general_ci'), quote = True)
    ExtCalle = Column('ExtCalle', Text(collation='utf8mb4_general_ci'), quote = True)
    Localidad = Column('Localidad', Text(collation='utf8mb4_general_ci'), quote = True)
    CPost = Column('CPost', Integer, quote = True)
    E_mail = Column('E-mail', Text(collation='utf8mb4_general_ci'), quote = True)
    Web = Column('Web', Text(collation='utf8mb4_general_ci'), quote = True)
    BIC = Column('BIC', Text(collation='utf8mb4_general_ci'), quote = True)
    IBAN = Column('IBAN', Text(collation='utf8mb4_general_ci'), quote = True)
    CC = Column('CC', Text(collation='utf8mb4_general_ci'), quote = True)
    Tlf1 = Column('Tlf1', Text(collation='utf8mb4_general_ci'), quote = True)
    Tlf2 = Column('Tlf2', Text(collation='utf8mb4_general_ci'), quote = True)
    Mvil = Column('Móvil', Integer, quote = True)
    Fax = Column('Fax', Text(collation='utf8mb4_general_ci'), quote = True)
    Contacto = Column('Contacto', Text(collation='utf8mb4_general_ci'), quote = True)
    Comentarios = Column('Comentarios', Text(collation='utf8mb4_general_ci'), quote = True)
    Notific = Column('Notific', Text(collation='utf8mb4_general_ci'), quote = True)
    Debaja = Column('Debaja', Text(collation='utf8mb4_general_ci'), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class StockTienda(SAFRSBaseX, Base):
    __tablename__ = 'StockTienda'
    _s_collection_name = 'StockTienda'  # type: ignore
    __bind_key__ = 'None'

    ID = Column('ID', Integer, nullable=False, unique=True, quote = True)
    Tienda = Column('Tienda', String(20, 'utf8mb4_general_ci'), nullable=False, quote = True)
    Referencia = Column('Referencia', Integer, primary_key=True, nullable=False, index=True, quote = True)
    Marca = Column('Marca', Text(collation='utf8mb4_general_ci'), quote = True)
    Producto = Column('Producto', Text(collation='utf8mb4_general_ci'), quote = True)
    ltimaVenta = Column('ÚltimaVenta', Date, quote = True)
    ltimaCompra = Column('ÚltimaCompra', Date, quote = True)
    Unidades = Column('Unidades', Float, quote = True)
    PrecioCoste = Column('PrecioCoste', Float, quote = True)
    PrecioCosteConIVA = Column('PrecioCosteConIVA', Float, quote = True)
    PrecioCosteConIVA_Recargo = Column('PrecioCosteConIVA-Recargo', Float, quote = True)
    PCM = Column('PCM', Float, quote = True)
    PCMconIVA = Column('PCMconIVA', Float, quote = True)
    PCMconIVA_Recargo = Column('PCMconIVA-Recargo', Float, quote = True)
    PVP = Column('PVP', Float, quote = True)
    PVPsinIVA = Column('PVPsinIVA', Float, quote = True)
    idTienda = Column('idTienda', SmallInteger, primary_key=True, nullable=False, quote = True)
    StockInicial = Column('StockInicial', Integer, quote = True)
    Entradas = Column('Entradas', Integer, quote = True)
    Salidas = Column('Salidas', Integer, quote = True)
    Stock = Column('Stock', Integer, quote = True)
    FechaInventario = Column('FechaInventario', DateTime, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Tienda(SAFRSBaseX, Base):
    __tablename__ = 'Tienda'
    _s_collection_name = 'Tienda'  # type: ignore
    __bind_key__ = 'None'

    STOREDVALUE = Column('STOREDVALUE', Integer, primary_key=True, quote = True)
    DISPLAYVALUE = Column('DISPLAYVALUE', String(20, 'utf8mb4_general_ci'), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class TraspasosLIN(SAFRSBaseX, Base):
    __tablename__ = 'Traspasos_LIN'
    _s_collection_name = 'TraspasosLIN'  # type: ignore
    __bind_key__ = 'None'

    Origen = Column('Origen', Text(collation='utf8mb4_general_ci'), quote = True)
    Destino = Column('Destino', Text(collation='utf8mb4_general_ci'), quote = True)
    Nmero = Column('Nmero', Integer, primary_key=True, unique=True, quote = True)
    Producto = Column('Producto', Text(collation='utf8mb4_general_ci'), quote = True)
    Cantidad = Column('Cantidad', Integer, quote = True)
    FechaTraspaso = Column('FechaTraspaso', DateTime, quote = True)
    PedidoProveedor = Column('PedidoProveedor', Text(collation='utf8mb4_general_ci'), quote = True)
    Referencia = Column('Referencia', Integer, quote = True)

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class VentasCAB(SAFRSBaseX, Base):
    __tablename__ = 'Ventas_CAB'
    _s_collection_name = 'VentasCAB'  # type: ignore
    __bind_key__ = 'None'

    Usuario = Column('Usuario', Text(collation='utf8mb4_general_ci'), quote = True)
    Tienda = Column('Tienda', Text(collation='utf8mb4_general_ci'), quote = True)
    Serie = Column('Serie', Text(collation='utf8mb4_general_ci'), quote = True)
    Nmero = Column('Número', Integer, primary_key=True, quote = True)
    VentaMostrador = Column('VentaMostrador', Text(collation='utf8mb4_general_ci'), quote = True)
    FechaVenta = Column('FechaVenta', DateTime, quote = True)
    ImporteTotal = Column('ImporteTotal', Float, quote = True)
    PrecioLnea = Column('PrecioLínea', Float, quote = True)
    NombreOferta = Column('NombreOferta', Text(collation='utf8mb4_general_ci'), quote = True)
    tpcDtoGlobal = Column('tpcDtoGlobal', Float, quote = True)
    tpcDtoPP = Column('tpcDtoPP', Float, quote = True)
    ImporteBruto = Column('ImporteBruto', Float, quote = True)
    FacturaSN = Column('FacturaSN', Text(collation='utf8mb4_general_ci'), quote = True)
    FechaFactura = Column('FechaFactura', Text(collation='utf8mb4_general_ci'), quote = True)
    NombreRaznSocialCliente = Column('NombreRazónSocialCliente', Text(collation='utf8mb4_general_ci'), quote = True)
    NombreComercialCliente = Column('NombreComercialCliente', Text(collation='utf8mb4_general_ci'), quote = True)
    NCuentaCliente = Column('NCuentaCliente', Integer, index=True, quote = True)
    TipoCliente = Column('TipoCliente', Text(collation='utf8mb4_general_ci'), quote = True)
    NIFCliente = Column('NIFCliente', Text(collation='utf8mb4_general_ci'), quote = True)
    Telfono = Column('Teléfono', Text(collation='utf8mb4_general_ci'), quote = True)
    ImporteIVASuperReducido = Column('ImporteIVASuperReducido', Float, quote = True)
    ImporteIVAReducido = Column('ImporteIVAReducido', Float, quote = True)
    ImporteIVAAceitesPastas = Column('ImporteIVAAceitesPastas', Float, quote = True)
    ImporteIVAGeneral = Column('ImporteIVAGeneral', Float, quote = True)
    BaseIVACero = Column('BaseIVACero', Float, quote = True)
    BaseIVASuperReducido = Column('BaseIVASuperReducido', Float, quote = True)
    BaseIVAReducido = Column('BaseIVAReducido', Float, quote = True)
    BaseIVAAceitesPastas = Column('BaseIVAAceitesPastas', Float, quote = True)
    BaseIVAGeneral = Column('BaseIVAGeneral', Float, quote = True)
    NumeroLineas = Column('NumeroLineas', Integer, quote = True)
    TieneValesDto = Column('TieneValesDto', BIT(1), quote = True)
    Puntos = Column('Puntos', Integer, quote = True)

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class VentasLIN(SAFRSBaseX, Base):
    __tablename__ = 'Ventas_LIN'
    _s_collection_name = 'VentasLIN'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('id', Integer, primary_key=True, quote = True)
    Usuario = Column('Usuario', Text(collation='utf8mb4_general_ci'), quote = True)
    Tienda = Column('Tienda', Text(collation='utf8mb4_general_ci'), quote = True)
    Serie = Column('Serie', Text(collation='utf8mb4_general_ci'), quote = True)
    Nmero = Column('Número', Integer, quote = True)
    VentaMostrador = Column('VentaMostrador', Text(collation='utf8mb4_general_ci'), quote = True)
    FechaVenta = Column('FechaVenta', DateTime, quote = True)
    Producto = Column('Producto', Text(collation='utf8mb4_general_ci'), quote = True)
    CdigoBarras = Column('CódigoBarras', Text(collation='utf8mb4_general_ci'), quote = True)
    RefProducto = Column('RefProducto', Integer, index=True, quote = True)
    OLDRefProducto = Column('OLDRefProducto', Text(collation='utf8mb4_general_ci'), quote = True)
    StockCantidad = Column('StockCantidad', Float, quote = True)
    FamiliaComercial = Column('FamiliaComercial', Text(collation='utf8mb4_general_ci'), quote = True)
    SubFamiliaComercial = Column('SubFamiliaComercial', Text(collation='utf8mb4_general_ci'), quote = True)
    Marca = Column('Marca', Text(collation='utf8mb4_general_ci'), quote = True)
    CantidadVendida = Column('CantidadVendida', Float, quote = True)
    LoteVendido = Column('LoteVendido', Text(collation='utf8mb4_general_ci'), quote = True)
    FechaCaducidad = Column('FechaCaducidad', Text(collation='utf8mb4_general_ci'), quote = True)
    ImporteTotal = Column('ImporteTotal', Float, quote = True)
    PrecioLnea = Column('PrecioLínea', Float, quote = True)
    tpcIVA = Column('tpcIVA', Float, quote = True)
    NombreOferta = Column('NombreOferta', Text(collation='utf8mb4_general_ci'), quote = True)
    tpcDtoLnea = Column('tpcDtoLínea', Float, quote = True)
    tpcDtoGlobal = Column('tpcDtoGlobal', Float, quote = True)
    tpcDtoPP = Column('tpcDtoPP', Float, quote = True)
    ImporteBruto = Column('ImporteBruto', Float, quote = True)
    FacturaSN = Column('FacturaSN', Text(collation='utf8mb4_general_ci'), quote = True)
    FechaFactura = Column('FechaFactura', Text(collation='utf8mb4_general_ci'), quote = True)
    NombreRaznSocialCliente = Column('NombreRazónSocialCliente', Text(collation='utf8mb4_general_ci'), quote = True)
    NombreComercialCliente = Column('NombreComercialCliente', Text(collation='utf8mb4_general_ci'), quote = True)
    NCuentaCliente = Column('NCuentaCliente', Integer, index=True, quote = True)
    TipoCliente = Column('TipoCliente', Text(collation='utf8mb4_general_ci'), quote = True)
    NIFCliente = Column('NIFCliente', Text(collation='utf8mb4_general_ci'), quote = True)
    Telfono = Column('Teléfono', Text(collation='utf8mb4_general_ci'), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_
