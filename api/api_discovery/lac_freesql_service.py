from flask import request, jsonify
import logging

from flask_cors import cross_origin
from flask import request, jsonify
from flask_jwt_extended import get_jwt, jwt_required, verify_jwt_in_request
from safrs import jsonapi_rpc
from sqlalchemy import and_, or_
from sqlalchemy.sql import text
from database import models
from security.system.authorization import Security
from api.system.free_sql import FreeSQL
import json
import safrs


app_logger = logging.getLogger(__name__)

db = safrs.DB  # valid only after is initialized, above
session = db.session


def add_service(app, api, project_dir, swagger_host: str, PORT: str, method_decorators = []):
    pass

    @app.route('/hello_service')
    def hello_service():
        """        
        Illustrates:
        * Use standard Flask, here for non-database endpoints.

        Test it with:
        
                http://localhost:5656/hello_service?user=ApiLogicServer
        """
        user = request.args.get('user')
        app_logger.info(f'{user}')
        return jsonify({"result": f'hello from new_service! from {user}'})



    #FreeSQL resource: Count_Ventas_CAB ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_ventas_cab', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_ventas_cab():
        sql = get_Count_Ventas_CAB(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Ventas_CAB(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Ventas_CAB` WHERE :WHERE ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Traspasos_LIN__Rivas_Vaciamadrid_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_traspasos_lin__rivas_vaciamadrid_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_traspasos_lin__rivas_vaciamadrid_sf():
        sql = get_Count_Traspasos_LIN__Rivas_Vaciamadrid_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Traspasos_LIN__Rivas_Vaciamadrid_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Traspasos_LIN` WHERE :WHERE AND (`Origen` = 'RIVAS VACIAMADRID' OR `Destino` = 'RIVAS VACIAMADRID')  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Compras_LIN__Rivas_Vaciamadrid_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_compras_lin__rivas_vaciamadrid_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_compras_lin__rivas_vaciamadrid_sf():
        sql = get_Count_Compras_LIN__Rivas_Vaciamadrid_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Compras_LIN__Rivas_Vaciamadrid_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Compras_LIN` WHERE :WHERE AND `Tienda` = 'RIVAS VACIAMADRID' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Compras_CAB ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_compras_cab', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_compras_cab():
        sql = get_Count_Compras_CAB(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Compras_CAB(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Compras_CAB` WHERE :WHERE  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Compras_LIN__Santa_Eugenia_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_compras_lin__santa_eugenia_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_compras_lin__santa_eugenia_sf():
        sql = get_Count_Compras_LIN__Santa_Eugenia_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Compras_LIN__Santa_Eugenia_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Compras_LIN` WHERE :WHERE AND `Tienda` = 'Santa Eugenia' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Compras_LIN__Barajas_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_compras_lin__barajas_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_compras_lin__barajas_sf():
        sql = get_Count_Compras_LIN__Barajas_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Compras_LIN__Barajas_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Compras_LIN` WHERE :WHERE AND `Tienda` = 'Barajas' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Producto ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_producto', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_producto():
        sql = get_Count_Producto(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Producto(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Producto` WHERE :WHERE  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Ventas_LIN__Palomeras_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_ventas_lin__palomeras_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_ventas_lin__palomeras_sf():
        sql = get_Count_Ventas_LIN__Palomeras_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Ventas_LIN__Palomeras_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Ventas_LIN` WHERE :WHERE AND `Tienda` = 'Palomeras' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Tienda ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_tienda', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_tienda():
        sql = get_Count_Tienda(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Tienda(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Tienda` WHERE :WHERE  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Compras_LIN__Palomeras_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_compras_lin__palomeras_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_compras_lin__palomeras_sf():
        sql = get_Count_Compras_LIN__Palomeras_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Compras_LIN__Palomeras_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Compras_LIN` WHERE :WHERE AND `Tienda` = 'Palomeras' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Compras_LIN__CComercial_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_compras_lin__ccomercial_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_compras_lin__ccomercial_sf():
        sql = get_Count_Compras_LIN__CComercial_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Compras_LIN__CComercial_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Compras_LIN` WHERE :WHERE AND `Tienda` = 'Centro Comercial' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Traspasos_LIN__Palomeras_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_traspasos_lin__palomeras_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_traspasos_lin__palomeras_sf():
        sql = get_count_traspasos_lin__palomeras_sf(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_count_traspasos_lin__palomeras_sf(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Traspasos_LIN` WHERE :WHERE AND (`Origen` = 'Palomeras' OR `Destino` = 'Palomeras')  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Ventas_LIN__Santa_Eugenia_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_ventas_lin__santa_eugenia_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_ventas_lin__santa_eugenia_sf():
        sql = get_Count_Ventas_LIN__Santa_Eugenia_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Ventas_LIN__Santa_Eugenia_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Ventas_LIN` WHERE :WHERE AND `Tienda` ='Santa Eugenia' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Cliente ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_cliente', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_cliente():
        sql = get_Count_Cliente(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Cliente(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Cliente` WHERE :WHERE  ".replace(":WHERE", argValue )


    #FreeSQL resource: Count_Ventas_LIN__CComercial_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_ventas_lin__ccomercial_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_ventas_lin__ccomercial_sf():
        sql = get_Count_Ventas_LIN__CComercial_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Ventas_LIN__CComercial_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Ventas_LIN` WHERE :WHERE AND `Tienda` = 'Centro Comercial' ".replace(":WHERE", argValue )


    #FreeSQL resource: Count_Traspasos_LIN__CComercial_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_traspasos_lin__ccomercial_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_traspasos_lin__ccomercial_sf():
        sql = get_Count_Traspasos_LIN__CComercial_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Traspasos_LIN__CComercial_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Traspasos_LIN` WHERE :WHERE AND (`Origen` = 'Centro Comercial' OR `Destino` = 'Centro Comercial')  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Ventas_LIN__Barajas_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_ventas_lin__barajas_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_ventas_lin__barajas_sf():
        sql = get_Count_Ventas_LIN__Barajas_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Ventas_LIN__Barajas_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Ventas_LIN` WHERE :WHERE AND `Tienda` = 'Barajas' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Proveedor ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_proveedor', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_proveedor():
        sql = get_Count_Proveedor(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Proveedor(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Proveedor` WHERE :WHERE  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Ventas_LIN__Ensanche_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_ventas_lin__ensanche_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_ventas_lin__ensanche_sf():
        sql = get_Count_Ventas_LIN__Ensanche_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Ventas_LIN__Ensanche_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Ventas_LIN` WHERE :WHERE AND `Tienda` = 'Ensanche' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Traspasos_LIN ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_traspasos_lin', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_traspasos_lin():
        sql = get_Count_Traspasos_LIN(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Traspasos_LIN(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Traspasos_LIN` WHERE :WHERE  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Ventas_LIN ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_ventas_lin', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_ventas_lin():
        sql = get_Count_Ventas_LIN(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Ventas_LIN(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Ventas_LIN` WHERE :WHERE  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Compras_LIN__Ensanche_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_compras_lin__ensanche_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_compras_lin__ensanche_sf():
        sql = get_Count_Compras_LIN__Ensanche_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Compras_LIN__Ensanche_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Compras_LIN` WHERE :WHERE AND `Tienda` = 'Ensanche' ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Compras_LIN ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_compras_lin', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_compras_lin():
        sql = get_Count_Compras_LIN(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Compras_LIN(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Compras_LIN` WHERE :WHERE  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Traspasos_LIN__Barajas_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_traspasos_lin__barajas_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_traspasos_lin__barajas_sf():
        sql = get_Count_Traspasos_LIN__Barajas_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Traspasos_LIN__Barajas_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Traspasos_LIN` WHERE :WHERE AND (`Origen` = 'Barajas' OR `Destino` = 'Barajas')  ".replace(":WHERE", argValue )


    #FreeSQL resource: Count_Traspasos_LIN__Ensanche_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_traspasos_lin__ensanche_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_traspasos_lin__ensanche_sf():
        sql = get_Count_Traspasos_LIN__Ensanche_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Traspasos_LIN__Ensanche_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Traspasos_LIN` WHERE :WHERE AND (`Origen` = 'Ensanche' OR `Destino` = 'Ensanche')  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Traspasos_LIN__Santa_Eugenia_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_traspasos_lin__santa_eugenia_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_traspasos_lin__santa_eugenia_sf():
        sql = get_Count_Traspasos_LIN__Santa_Eugenia_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Traspasos_LIN__Santa_Eugenia_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Traspasos_LIN` WHERE :WHERE AND (`Origen` = 'Santa Eugenia' OR `Destino` = 'Santa Eugenia')  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_StockTienda ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_stocktienda', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_stocktienda():
        sql = get_Count_StockTienda(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_StockTienda(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `StockTienda` WHERE :WHERE  ".replace(":WHERE", argValue )

    #FreeSQL resource: Count_Ventas_LIN__Rivas_Vaciamadrid_SF ResourceType: FreeSQL isActive: True
    @app.route('/rest/default/herboDeSonia/v1/count_ventas_lin__rivas_vaciamadrid_sf', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def count_ventas_lin__rivas_vaciamadrid_sf():
        sql = get_Count_Ventas_LIN__Rivas_Vaciamadrid_SF(request)
        return FreeSQL(sqlExpression=sql).execute(request)

    def get_Count_Ventas_LIN__Rivas_Vaciamadrid_SF(request):
        args = request.args
        argValue = args.get("filter", "1=1")
        return "SELECT count(*) FROM `Ventas_LIN` WHERE :WHERE AND `Tienda` = 'RIVAS VACIAMADRID' ".replace(":WHERE", argValue )
