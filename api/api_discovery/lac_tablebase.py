
from functools import wraps
import logging

from flask_cors import cross_origin
from flask import request, jsonify
from flask_jwt_extended import get_jwt, jwt_required, verify_jwt_in_request
from safrs import jsonapi_rpc
from sqlalchemy import and_, or_
from sqlalchemy.sql import text
from database import models
from api.system.custom_endpoint import CustomEndpoint, DotDict
from security.system.authorization import Security
from api.system.javascript import JavaScript
import json
import safrs

app_logger = logging.getLogger(__name__)

db = safrs.DB  # valid only after is initialized, above
session = db.session

def add_service(app, api, project_dir, swagger_host: str, PORT: str, method_decorators ):
    pass


    @app.route('/rest/default/herboDeSonia/v1/CRTienda_pick', methods=['GET','POST','PUT','OPTIONS'])
    #@admin_required()
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def CRTiendaPICK():
        root = CustomEndpoint(model_class=models.Tienda,alias="CR-Tienda__PICK"
            ,fields=[ (models.Tienda.STOREDVALUE, "STOREDVALUE"), (models.Tienda.DISPLAYVALUE, "DISPLAYVALUE")]
        )
        result = root.execute(request)
        return root.transform('LAC', 'CR-Tienda__PICK', result)

    @app.route('/rest/default/herboDeSonia/v1/CRProducto', methods=['GET','POST','PUT','OPTIONS'])
    #@admin_required()
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def Producto():
        root = CustomEndpoint(model_class=models.Producto,alias="CR-Producto"
            ,fields=[ (models.Producto.Referencia, "Referencia"), (models.Producto.Descripcion, "Descripcion"), (models.Producto.DescripcionBreve, "DescripcionBreve"), (models.Producto.CodBarras, "CodBarras"), (models.Producto.CodGenerico, "CodGenerico"), (models.Producto.FechaCreacion, "FechaCreacion"), (models.Producto.PrecioCoste, "PrecioCoste"), (models.Producto.SubFam, "SubFam"), (models.Producto.Ubicacion, "Ubicacion"), (models.Producto.PublicarWeb, "PublicarWeb"), (models.Producto.OfertaWeb, "OfertaWeb"), (models.Producto.NovedadWeb, "NovedadWeb"), (models.Producto.PVP, "PVP"), (models.Producto.FechaUltPVP, "FechaUltPVP"), (models.Producto.Familia, "Familia"), (models.Producto.Stock, "Stock"), (models.Producto.IVA, "IVA"), (models.Producto.Marca, "Marca"), (models.Producto.Proveedor, "Proveedor"), (models.Producto.Descatalogado, "Descatalogado"), (models.Producto.tipoIVA, "tipoIVA")]
        )

        """
            ,children=CustomEndpoint[(model_class=models.02ListFormextProductoTraspasos,alias="02List-FormExt__Producto__Traspasos" ,join_on=models.02ListFormextProductoTraspasos.Referencia
            )
            ,CustomEndpoint(model_class=models.00ListFormextProductoVentas,alias="00List-FormExt__Producto__Ventas" ,join_on=models.00ListFormextProductoVentas.Referencia
            )
            ,CustomEndpoint(model_class=models.01ListFormextProductoCompras,alias="01List-FormExt__Producto__Compras" ,join_on=models.01ListFormextProductoCompras.Referencia
            )
            ,CustomEndpoint(model_class=models.03ListFormextStocktienda,alias="03List-FormExt__StockTienda" ,join_on=models.03ListFormextStocktienda.Referencia
            )
            ]
        """
        
        result = root.execute(request)
        return root.transform('LAC', 'CR-Producto', result)
    
    @app.route('/rest/default/herboDeSonia/v1/CR-Cliente', methods=['GET','POST','PUT','OPTIONS'])
    #@admin_required()
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def Cliente():
        root = CustomEndpoint(model_class=models.Cliente,alias="CR-Cliente"
            ,fields=[ (models.Cliente.Tipo, "Tipo"), (models.Cliente.FechaAlta, "FechaAlta"), (models.Cliente.TipoCliente, "TipoCliente"), (models.Cliente.DNI_CIF, "DNI_CIF"), (models.Cliente.BIC, "BIC"), (models.Cliente.IBAN, "IBAN"), (models.Cliente.NCuenta, "NCuenta"), (models.Cliente.NombreCorto, "NombreCorto"), (models.Cliente.NombreCompleto, "NombreCompleto"), (models.Cliente.Calle, "Calle"), (models.Cliente.ExtCalle, "ExtCalle"), (models.Cliente.Localidad, "Localidad"), (models.Cliente.Provincia, "Provincia"), (models.Cliente.CodPostal, "CodPostal"), (models.Cliente.Tlf, "Tlf"), (models.Cliente.Email, "Email"), (models.Cliente.Web, "Web"), (models.Cliente.FPago, "FPago"), (models.Cliente.CC, "CC"), (models.Cliente.DtoGl, "DtoGl"), (models.Cliente.NCopFact, "NCopFact"), (models.Cliente.Contacto, "Contacto"), (models.Cliente.Recomendado, "Recomendado"), (models.Cliente.Comentarios, "Comentarios"), (models.Cliente.Notific, "Notific"), (models.Cliente.DeBaja, "DeBaja"), (models.Cliente.FechaBaja, "FechaBaja"), (models.Cliente.CreadorPor, "CreadorPor")]
            #,children=CustomEndpoint(model_class=models.00ListVentasLin,alias="00List-Ventas_LIN" ,join_on=models.00ListVentasLin.NCuentaCliente
            #)
        )
        result = root.execute(request)
        return root.transform('LAC', 'CR-Cliente', result)

    @app.route('/rest/default/herboDeSonia/v1/CR-Compras_CAB', methods=['GET','POST','PUT','OPTIONS'])
    #@admin_required()
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def CRComprasCAB():
        root = CustomEndpoint(model_class=models.ComprasCAB,alias="CR-Compras_CAB"
            ,fields=[ (models.ComprasCAB.NCuentaProveedor, "NºCuentaProveedor"), (models.ComprasCAB.Tienda, "Tienda"), (models.ComprasCAB.idTienda, "idTienda"), (models.ComprasCAB.SerieNmero, "SerieNúmero"), (models.ComprasCAB.Fecha, "Fecha"), (models.ComprasCAB.RaznSocial, "RazónSocial"), (models.ComprasCAB.BaseImponible, "BaseImponible"), (models.ComprasCAB.ImporteIVA, "ImporteIVA"), (models.ComprasCAB.ImporteRecargoEq, "ImporteRecargoEq"), (models.ComprasCAB.TotalAlbCompra, "TotalAlbCompra"), (models.ComprasCAB.idCabCompras, "idCabCompras"), (models.ComprasCAB.ImporteIVAReducido, "ImporteIVAReducido"), (models.ComprasCAB.ImporteIVASuperReducido, "ImporteIVASuperReducido"), (models.ComprasCAB.ImporteIVAAceitesPastas, "ImporteIVAAceitesPastas"), (models.ComprasCAB.BaseIVAReducido, "BaseIVAReducido"), (models.ComprasCAB.BaseIVASuperReducido, "BaseIVASuperReducido"), (models.ComprasCAB.BaseIVAAceitesPastas, "BaseIVAAceitesPastas"), (models.ComprasCAB.BaseIVACero, "BaseIVACero"), (models.ComprasCAB.ImporteIVAGeneral, "ImporteIVAGeneral"), (models.ComprasCAB.BaseIVAGeneral, "BaseIVAGeneral"), (models.ComprasCAB.TotalAlbCalculado, "TotalAlbCalculado"), (models.ComprasCAB.tpcDtoProntoPago, "tpcDtoProntoPago"), (models.ComprasCAB.tpcDtoGlobal, "tpcDtoGlobal")]
            ,order_by=(models.ComprasCAB.Fecha)
            #,children=CustomEndpoint(model_class=models.ListComprasLin,alias="List-Compras_LIN" ,join_on=models.ListComprasLin.AlbaránCompra
            #)
        )
        result = root.execute(request)
        return root.transform('LAC', 'CR-Compras_CAB', result)

    @app.route('/rest/default/herboDeSonia/v1/CR-Producto__PICK', methods=['GET','POST','PUT','OPTIONS'])
    #@admin_required()
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def CRProductPICK():
        root = CustomEndpoint(model_class=models.Producto,alias="CR-Producto__PICK"
            ,fields=[ (models.Producto.Referencia, "Referencia"), (models.Producto.Descripcion, "Descripcion"), (models.Producto.DescripcionBreve, "DescripcionBreve"), (models.Producto.CodBarras, "CodBarras"), (models.Producto.FechaCreacion, "FechaCreacion"), (models.Producto.PVP, "PVP"), (models.Producto.PrecioCoste, "PrecioCoste"), (models.Producto.IVA, "IVA"), (models.Producto.tipoIVA, "tipoIVA")]
        )
        result = root.execute(request)
        return root.transform('LAC', 'CR-Producto__PICK', result)


    @app.route('/rest/default/herboDeSonia/v1/CR-Proveedor', methods=['GET','POST','PUT','OPTIONS'])
    #@admin_required()
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def Proveedor():
        root = CustomEndpoint(model_class=models.Proveedor,alias="CR-Proveedor"
            ,fields=[ (models.Proveedor.DNICIF, "DNICIF"), (models.Proveedor.RSocial, "RSocial"), (models.Proveedor.TipoProv, "TipoProv"), (models.Proveedor.FPago, "FPago"), (models.Proveedor.Facturacin, "Facturación"), (models.Proveedor.Provincia, "Provincia"), (models.Proveedor.NCuenta, "NºCuenta"), (models.Proveedor.Calle, "Calle"), (models.Proveedor.ExtCalle, "ExtCalle"), (models.Proveedor.Localidad, "Localidad"), (models.Proveedor.CPost, "CPost"), (models.Proveedor.E_mail, "E-mail"), (models.Proveedor.Web, "Web"), (models.Proveedor.BIC, "BIC"), (models.Proveedor.IBAN, "IBAN"), (models.Proveedor.CC, "CC"), (models.Proveedor.Tlf1, "Tlf1"), (models.Proveedor.Tlf2, "Tlf2"), (models.Proveedor.Mvil, "Móvil"), (models.Proveedor.Fax, "Fax"), (models.Proveedor.Contacto, "Contacto"), (models.Proveedor.Comentarios, "Comentarios"), (models.Proveedor.Notific, "Notific"), (models.Proveedor.Debaja, "Debaja")]
            #,children=CustomEndpoint(model_class=models.00ListComprasLin,alias="00List-Compras_LIN" ,join_on=models.00ListComprasLin.NºCuentaProveedor
            #)
        )
        result = root.execute(request)
        return root.transform('LAC', 'CR-Proveedor', result)
    
    
    @app.route('/rest/default/herboDeSonia/v1/CR-Proveedor__PICK', methods=['GET','POST','PUT','OPTIONS'])
    #@admin_required()
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def CRProveedor__PICK():
        root = CustomEndpoint(model_class=models.Proveedor,alias="CR-Proveedor__PICK"
            ,fields=[ (models.Proveedor.DNICIF, "DNICIF"), (models.Proveedor.RSocial, "RSocial"), (models.Proveedor.TipoProv, "TipoProv"), (models.Proveedor.FPago, "FPago"), (models.Proveedor.NCuenta, "NºCuenta"), (models.Proveedor.Provincia, "Provincia")]
        )
        result = root.execute(request)
        return root.transform('LAC', 'CR-Proveedor__PICK', result)

    @app.route('/rest/default/herboDeSonia/v1/CR-Ventas_CAB', methods=['GET','POST','PUT','OPTIONS'])
    #@admin_required()
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def VentasCAB():
        root = CustomEndpoint(model_class=models.VentasCAB,alias="CR-Ventas_CAB"
            ,fields=[ (models.VentasCAB.Usuario, "Usuario"), (models.VentasCAB.Tienda, "Tienda"), (models.VentasCAB.Serie, "Serie"), (models.VentasCAB.Nmero, "Número"), (models.VentasCAB.VentaMostrador, "VentaMostrador"), (models.VentasCAB.FechaVenta, "FechaVenta"), (models.VentasCAB.ImporteTotal, "ImporteTotal"), (models.VentasCAB.PrecioLnea, "PrecioLínea"), (models.VentasCAB.NombreOferta, "NombreOferta"), (models.VentasCAB.tpcDtoGlobal, "tpcDtoGlobal"), (models.VentasCAB.tpcDtoPP, "tpcDtoPP"), (models.VentasCAB.ImporteBruto, "ImporteBruto"), (models.VentasCAB.FacturaSN, "FacturaSN"), (models.VentasCAB.FechaFactura, "FechaFactura"), (models.VentasCAB.NombreRaznSocialCliente, "NombreRazónSocialCliente"), (models.VentasCAB.NombreComercialCliente, "NombreComercialCliente"), (models.VentasCAB.NCuentaCliente, "NCuentaCliente"), (models.VentasCAB.TipoCliente, "TipoCliente"), (models.VentasCAB.NIFCliente, "NIFCliente"), (models.VentasCAB.Telfono, "Teléfono"), (models.VentasCAB.ImporteIVASuperReducido, "ImporteIVASuperReducido"), (models.VentasCAB.ImporteIVAReducido, "ImporteIVAReducido"), (models.VentasCAB.ImporteIVAAceitesPastas, "ImporteIVAAceitesPastas"), (models.VentasCAB.ImporteIVAGeneral, "ImporteIVAGeneral"), (models.VentasCAB.BaseIVACero, "BaseIVACero"), (models.VentasCAB.BaseIVASuperReducido, "BaseIVASuperReducido"), (models.VentasCAB.BaseIVAReducido, "BaseIVAReducido"), (models.VentasCAB.BaseIVAAceitesPastas, "BaseIVAAceitesPastas"), (models.VentasCAB.BaseIVAGeneral, "BaseIVAGeneral"), (models.VentasCAB.NumeroLineas, "NumeroLineas"), (models.VentasCAB.TieneValesDto, "TieneValesDto"), (models.VentasCAB.Puntos, "Puntos")]
            ,calling=(fn_CR_Ventas_CAB_cr_ventas_cab_crventascab_event)
            #,children=CustomEndpoint(model_class=models.ListVentasLin,alias="List-Ventas_LIN" ,join_on=models.ListVentasLin.Número
            #)
        )
        result = root.execute(request)
        return root.transform('LAC', 'CR-Ventas_CAB', result)


def fn_CR_Ventas_CAB_cr_ventas_cab_crventascab_event(row: dict, tableRow: dict, parentRow: dict):
    pass         
    '''
        row.cabLin1 = "RACRISSON S.L. - HERBOLARIO"
    row.cabLin2 = "SONIA"
    row.cabLin3 = "AVDA PABLO NERUDA 91-97"
    row.cabLin4 = row.Tienda
    row.cabLin5 = " "
    row.cabLin6 = "CIF else B87472486"
    row.cabLin7 = "Código del cliente else " + row.NCuentaCliente
    row.cabLin8 = "Factura simplif. " + row.VentaMostrador
    row.fecha = row.FechaVenta
    row.footerLin1 = "IVA"
    space = "                      "
    lineasIvas = ""

    if row.BaseIVACero != 0):
        row.footerLin2 = space + "0 x " + row.BaseIVACero.toFixed(2) + "    " + "0,00"
        lineasIvas += ",footerLin2"


    if row.BaseIVASuperReducido != 0):
        row.footerLin3 = space + "4 x " + row.BaseIVASuperReducido.toFixed(2) + "    " + row.ImporteIVASuperReducido.toFixed(2)
        lineasIvas += ",footerLin3"


    if row.BaseIVAAceitesPastas != 0):
        row.footerLin4 = space + "5 x " + row.BaseIVAAceitesPastas.toFixed(2) + "    " + row.ImporteIVAAceitesPastas.toFixed(2)
        lineasIvas += ",footerLin4"


    if row.BaseIVAReducido != 0):
        row.footerLin5 = space + "10 x " + row.BaseIVAReducido.toFixed(2) + "    " + row.ImporteIVAReducido.toFixed(2)
        lineasIvas += ",footerLin5"


    if row.BaseIVAGeneral != 0):
        row.footerLin6 = space + "21 x " + row.BaseIVAGeneral.toFixed(2) + "    " + row.ImporteIVAGeneral.toFixed(2)
        lineasIvas += ",footerLin6"


    lineasIvas = lineasIvas.substring(1) # elimina la coma inicial


    row.footerLin7 = "TOTAL                              " + row.ImporteTotal.toFixed(2)

    row.MapPrintFields='#CAB#cabLin1,cabLin2,cabLin3,cabLin4,cabLin5,cabLin6,cabLin7,fecha,cabLin7#LIN#List-Ventas_LIN#HEADER#PROD/SERV     UND/H               TOTAL#L1#Producto#L2#SPACE(15),CantidadXPrecio,ImporteBruto#sizes#46,15,20,15#FOOT#footerLin1,'+lineasIvas+',footerLin7'
    '''