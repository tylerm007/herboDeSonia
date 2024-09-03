import datetime
from decimal import Decimal
from logic_bank.exec_row_logic.logic_row import LogicRow
from logic_bank.extensions.rule_extensions import RuleExtension
from logic_bank.logic_bank import Rule
from database import models
import api.system.opt_locking.opt_locking as opt_locking
from security.system.authorization import Grant, Security
import logging

app_logger = logging.getLogger(__name__)

declare_logic_message = "ALERT:  *** No Rules Yet ***"  # printed in api_logic_server.py

def declare_logic():
    ''' Declarative multi-table derivations and constraints, extensible with Python.

    Brief background: see readme_declare_logic.md
    
    Your Code Goes Here - Use code completion (Rule.) to declare rules
    '''

    #from logic.logic_discovery.auto_discovery import discover_logic
    #discover_logic()

    def handle_all(logic_row: LogicRow):  # #als: TIME / DATE STAMPING, OPTIMISTIC LOCKING
        """
        This is generic - executed for all classes.

        Invokes optimistic locking, and checks Grant permissions.

        Also provides user/date stamping.

        Args:
            logic_row (LogicRow): from LogicBank - old/new row, state
        """
        if logic_row.is_updated() and logic_row.old_row is not None and logic_row.nest_level == 0:
            opt_locking.opt_lock_patch(logic_row=logic_row)

        Grant.process_updates(logic_row=logic_row)

        did_stamping = False
        if enable_stamping := False:  # #als:  DATE / USER STAMPING
            row = logic_row.row
            if logic_row.ins_upd_dlt == "ins" and hasattr(row, "CreatedOn"):
                row.CreatedOn = datetime.datetime.now()
                did_stamping = True
            if logic_row.ins_upd_dlt == "ins" and hasattr(row, "CreatedBy"):
                row.CreatedBy = Security.current_user().id
                #    if Config.SECURITY_ENABLED == True else 'public'
                did_stamping = True
            if logic_row.ins_upd_dlt == "upd" and hasattr(row, "UpdatedOn"):
                row.UpdatedOn = datetime.datetime.now()
                did_stamping = True
            if logic_row.ins_upd_dlt == "upd" and hasattr(row, "UpdatedBy"):
                row.UpdatedBy = Security.current_user().id  \
                    if Config.SECURITY_ENABLED == True else 'public'
                did_stamping = True
            if did_stamping:
                logic_row.log("early_row_event_all_classes - handle_all did stamping")     
    Rule.early_row_event_all_classes(early_row_event_all_classes=handle_all)


    # ENTITY: ComprasCab
    # RuleType: formula
    # Title: ImporteIVA = return row.ImporteIVAGeneral + row.ImporteIVAReducido + row.ImporteIVAAceitesPastas + row.ImporteIVASuperReducido;
    # Name: formula_rjsgy
    # Entity: ComprasCab
    # Comments: None

    def fn_comprascab_formula_formula_rjsgy(row: models.ComprasCAB, old_row: models.ComprasCAB, logic_row: LogicRow):
        return row.ImporteIVAGeneral + row.ImporteIVAReducido + row.ImporteIVAAceitesPastas + row.ImporteIVASuperReducido

    Rule.formula(derive=models.ComprasCAB.ImporteIVA,
        calling=fn_comprascab_formula_formula_rjsgy)

    # RuleType: formula
	# Title: TotalAlbCompra = return row.ImporteIVA + row.BaseImponible;
	# Name: formula_bouar
	# Entity: ComprasCab
	# Comments: None

    Rule.formula(derive=models.ComprasCAB.TotalAlbCompra,
		as_expression=lambda row:  row.ImporteIVA + row.BaseImponible)
    
    # RuleType: sum
	# Title: BaseIVAGeneral = sum(Compras_LIN_List.Importe where tpcIVA==21)
	# Name: sum_glfeh
	# Entity: ComprasCab
	# Comments: None

    # TODO - no relationship to: ComprasCAB in Derive ComprasCAB.BaseIVAGeneral
    #Rule.sum(derive=models.ComprasCAB.BaseIVAGeneral,
    #            as_sum_of=models.ComprasLIN.Importe, where=lambda row: row.tpcIVA == 21)
    
    # RuleType: sum
	# Title: BaseIVASuperReducido = sum(Compras_LIN_List.Importe where tpcIVA=4)
	# Name: sum_vvqti
	# Entity: ComprasCab
	# Comments: None

    # TODO no relationship to: ComprasCAB in Derive ComprasCAB.BaseIVASuperReducido a
    #Rule.sum(derive=models.ComprasCAB.BaseIVASuperReducido, 
    #    as_sum_of=models.ComprasLIN.Importe,
    #    where=lambda row: row.tpcIVA==4)
    
    # RuleType: sum
	# Title: BaseIVAAceitesPastas = sum(Compras_LIN_List.Importe where tpcIVA=5)
	# Name: sum_dqles
	# Entity: ComprasCab
	# Comments: None

    #Rule.sum(derive=models.ComprasCAB.BaseIVAAceitesPastas, 
    #    as_sum_of=models.ComprasLIN.Importe,
    #        where=lambda row: row.tpcIVA==5)
    
    # RuleType: formula
	# Title: ImporteIVAReducido = var dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100;
	# Name: formula_luvit
	# Entity: ComprasCab
	# Comments: None

    def fn_comprascab_formula_formula_luvit(row: models.ComprasCAB, old_row: models.ComprasCAB, logic_row: LogicRow):
        dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100
        dtoGlobal = (100 - row.tpcDtoGlobal) / 100
        logic_row.log(f'dtoProntoPago: {dtoProntoPago} , dtoGlobal: {dtoGlobal}')
        baseIVAReducido = row.BaseIVAReducido * dtoProntoPago
        logic_row.log('row.baseIVAReducido '+ row.baseIVAReducido + ' baseIVAReducido '+ baseIVAReducido)
        baseIVAReducido = baseIVAReducido * dtoGlobal
        logic_row.log(' baseIVAReducido ' + baseIVAReducido)
        return baseIVAReducido * 10 /100

    Rule.formula(derive=models.ComprasCAB.ImporteIVAReducido,
		calling=fn_comprascab_formula_formula_luvit)
    
    
	# RuleType: sum
	# Title: BaseIVACero = sum(Compras_LIN_List.Importe where tpcIVA=0)
	# Name: sum_pielg
	# Entity: ComprasCab
	# Comments: None

    #Rule.sum(derive=models.ComprasCAB.BaseIVACero, 
    #    as_sum_of=models.ComprasLIN.Importe,
    #    where=lambda row: row.tpcIVA==0)

    # RuleType: sum
	# Title: BaseIVAReducido = sum(Compras_LIN_List.Importe where tpcIVA=10)
	# Name: sum_drdjf
	# Entity: ComprasCab
	# Comments: None

    #Rule.sum(derive=models.ComprasCAB.BaseIVAReducido, 
    #    as_sum_of=models.ComprasLIN.Importe,
    #    where=lambda row: row.tpcIVA==10)
    
	# RuleType: formula
	# Title: ImporteIVAGeneral = var dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100;
	# Name: formula_umdvr
	# Entity: ComprasCab
	# Comments: None

    def fn_comprascab_formula_formula_umdvr(row: models.ComprasCAB, old_row: models.ComprasCAB, logic_row: LogicRow):
        dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100
        dtoGlobal = (100 - row.tpcDtoGlobal) / 100
        baseIVAGeneral = row.BaseIVAGeneral * dtoProntoPago
        baseIVAGeneral = baseIVAGeneral * dtoGlobal
        return baseIVAGeneral *21 /100

    Rule.formula(derive=models.ComprasCAB.ImporteIVAGeneral,
        calling=fn_comprascab_formula_formula_umdvr)

    # RuleType: formula
	# Title: BaseImponible = var dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100;
	# Name: formula_phvqk
	# Entity:  ComprasCAB
	# Comments: None

    def fn_comprascab_formula_formula_phvqk(row: models. ComprasCAB, old_row: models. ComprasCAB, logic_row: LogicRow):
        dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100
        dtoGlobal = (100 - row.tpcDtoGlobal) / 100

        baseIVAGeneral = row.BaseIVAGeneral * dtoProntoPago
        baseIVAGeneral = baseIVAGeneral * dtoGlobal

        baseIVAReducido = row.BaseIVAReducido * dtoProntoPago
        baseIVAReducido = baseIVAReducido * dtoGlobal

        baseIVAAceitesPastas = row.BaseIVAAceitesPastas * dtoProntoPago
        baseIVAAceitesPastas = baseIVAAceitesPastas * dtoGlobal

        baseIVASuperReducido = row.BaseIVASuperReducido * dtoProntoPago
        baseIVASuperReducido = baseIVASuperReducido * dtoGlobal

        baseIVACero = row.BaseIVACero * dtoProntoPago
        baseIVACero = baseIVACero * dtoGlobal

        return baseIVAGeneral + baseIVAReducido + baseIVAAceitesPastas + baseIVASuperReducido + baseIVACero

    Rule.formula(derive=models. ComprasCAB.BaseImponible,
        calling=fn_comprascab_formula_formula_phvqk)
    
    
	# RuleType: formula
	# Title: ImporteIVAAceitesPastas = var dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100;
	# Name: formula_umsgu
	# Entity:  ComprasCAB
	# Comments: None

    def fn_comprascab_formula_formula_umsgu(row: models. ComprasCAB, old_row: models. ComprasCAB, logic_row: LogicRow):
        dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100
        dtoGlobal = (100 - row.tpcDtoGlobal) / 100
        baseIVAAceitesPastas = row.BaseIVAAceitesPastas * dtoProntoPago
        baseIVAAceitesPastas = baseIVAAceitesPastas * dtoGlobal
        return baseIVAAceitesPastas * 5 /100

    Rule.formula(derive=models. ComprasCAB.ImporteIVAAceitesPastas,
        calling=fn_comprascab_formula_formula_umsgu)

    # ENTITY: StockTienda
	# RuleType: formula
	# Title: Stock = return row.StockInicial + row.Entradas - row.Salidas;
	# Name: formula_aycut
	# Entity: StockTienda
	# Comments: None

    Rule.formula(derive=models.StockTienda.Stock,
        as_expression=lambda row: row.StockInicial + row.Entradas - row.Salidas
    )
    
    
	# RuleType: sum
	# Title: Entradas = sum(Compras_LIN_List.Cantidad where NºCuentaProveedor>0 AND FechaAlbarán >=)
	# Name: sum_sqfwp
	# Entity: StockTienda
	# Comments: None

    #Rule.sum(derive=models.StockTienda.Entradas, 
    #        as_sum_of=models.ComprasLIN.Cantidad,
    #        where=lambda row: row.NCuentaProveedor>0)


    # ENTITY: ComprasLin
	# RuleType: event
	# Title: Event: PonStockIncial
	# Name: event_dinpp
	# Entity: ComprasLin
	# Comments: None

    def fn_compraslin_event_event_dinpp(row: models.ComprasLIN, old_row: models.ComprasLIN, logic_row: LogicRow):
        #AppliesTo: {'insert': True, 'update': True, 'delete': True}
        logic_row.log('>>>>>>>>>>>>>>>>>> Event else  PonStockIncial >>>>>>>>>>>>>>>>>>')
        if logic_row.is_updated or logic_row.is_inserted and row.FechaAlbarán >= row.FechaInventario: 
            parentRow = row.StockTienda
            logic_row.log(row.Cantidad+ " logic_row.getLogicNestLevel() "+ logic_row.getLogicNestLevel())
            if parentRow and logic_row.getLogicNestLevel() == 0:
                logic_row.log(' TIENE PADRE ' + parentRow)
                if row.NCuentaProveedor == 0:
                    logic_row.log(' es el proveedor Inventario ' + parentRow)
                    #logic_row.touch(parentRow)
                    parentRow.StockInicial = row.Cantidad
                    parentRow.FechaInventario = row.FechaAlbarán
                    if logic_row.is_inserted:
                        parentRow.Entradas = 0
                        parentRow.Salidas = 0
                            
                    logic_row.update(parentRow)


    Rule.row_event(on_class=models.ComprasLIN,
        calling=fn_compraslin_event_event_dinpp)
    
    # RuleType: validation
	# Title: Validation: //log.debug(logicContext.getLogicNestLevel() + 'row.StockTienda.FechaInventario > row.FechaAlbarán '+ row.StockTienda.FechaInventario  + " "+ row.FechaAlbarán);
	# Name: validation_vfwmg
	# Entity: ComprasLin
	# Comments: None

    def fn_compraslin_validation_validation_vfwmg(row: models.ComprasLIN, old_row: models.ComprasLIN, logic_row: LogicRow):
        #logic_row.log(logic_row.getLogicNestLevel() + 'row.StockTienda.FechaInventario > row.FechaAlbarán '+ row.StockTienda.FechaInventario  + " "+ row.FechaAlbarán)
        if row.StockTienda and logic_row.getLogicNestLevel()== 0:
            if row.StockTienda.FechaInventario > row.FechaAlbarán:
                return False
            else:
                return True

        return True

    Rule.constraint(validate=models.ComprasLIN,
        calling=fn_compraslin_validation_validation_vfwmg,
        error_msg="No se puede modifica una entrada si su fecha es anterior a inventario")


	# RuleType: managedParent
	# Title: Create parent using role StockTienda if it does not exist.
	# Name: managedParent_evxaf
	# Entity: ComprasLin
	# Comments: None

	#Rule.managedParent(...TODO...) 

    # RuleType: parentCopy
	# Title: NºCuentaProveedor = parentcopy(Compras_CAB.NºCuentaProveedor)
	# Name: parentCopy_kfpkd
	# Entity: ComprasLin
	# Comments: None

    #Rule.copy(derive=models.ComprasLIN.NCuentaProveedor,
    #		from_parent=models. ComprasCAB.NCuentaProveedor)
    
    # RuleType: parentCopy
    # Title: FechaAlbarán = parentcopy(Compras_CAB.Fecha)
    # Name: parentCopy_rvpxv
    # Entity:  ComprasLIN
    # Comments: None

    #Rule.copy(derive=models. ComprasLIN.FechaAlbarn,
    #    from_parent=models. ComprasCAB.Fecha)

    # RuleType: formula
	# Title: Importe = var dto1 = (100 - row.tpcDescuento1) / 100;
	# Name: formula_tgojc
	# Entity:  ComprasLIN
	# Comments: None

    def fn_compraslin_formula_formula_tgojc(row: models. ComprasLIN, old_row: models. ComprasLIN, logic_row: LogicRow):
        dto1 = (100 - row.tpcDescuento1) / 100
        dto2 = (100 - row.tpcDescuento2) / 100
        importe = row.CantidadConCoste * row.PrecioCoste
        importe = importe * dto1
        importe = importe * dto2
        return importe

    Rule.formula(derive=models. ComprasLIN.Importe,
		calling=fn_compraslin_formula_formula_tgojc)

    # RuleType: formula
	# Title: Cantidad = return row.CantidadConCoste + row.CantidadGratis;
	# Name: formula_ilmjy
	# Entity:  ComprasLIN
	# Comments: None

    Rule.formula(derive=models. ComprasLIN.Cantidad,
		as_expression=lambda row: row.CantidadConCoste + row.CantidadGratis
    )
    
    # RuleType: event
	# Title: Event: keepLastPVP
	# Name: event_nzgws
	# Entity:  ComprasLIN
	# Comments: None

    def 	fn_compraslin_event_event_nzgws(row: models. ComprasLIN, old_row: models. ComprasLIN, logic_row: LogicRow):
        #AppliesTo: {'insert': True, 'update': True, 'delete': True}
        logic_row.log('>>>>>>>>>>>>>>>>>> Event else  keepLastPVP >>>>>>>>>>>>>>>>>>')
        if (logic_row.is_updated and row.PVPProducto != old_row.PVPProducto) or logic_row.is_inserted:
            parentRow = row.Producto
            logic_row.log(row.Cantidad+ " logic_row.getLogicNestLevel() "+ logic_row.getLogicNestLevel())
            if parentRow and logic_row.getLogicNestLevel() == 0:
                logic_row.log(' TIENE PADRE ' + parentRow)
                if parentRow.FechaUltPVP == None or ( row.FechaAlbarán >= parentRow.FechaUltPVP):
                    logic_row.log(' la fecha de Ult PVP ' + row.Producto.FechaUltPVP)
                    logic_row.touch(parentRow)
                    parentRow.FechaUltPVP = row.FechaAlbarán
                    parentRow.PVP = row.PVPProducto
                    logic_row.update(parentRow)
                

    Rule.row_event(on_class=models.ComprasLIN,
		calling=fn_compraslin_event_event_nzgws)

	# RuleType: formula
	# Title: Formula PrecioLinea
	# Name: formula_olhjv
	# Entity:  ComprasLIN
	# Comments: None

    def fn_compraslin_formula_formula_olhjv(row: models.ComprasLIN, old_row: models.ComprasLIN, logic_row: LogicRow):
        return (row.CantidadConCoste * row.PrecioCoste) / (row.CantidadConCoste + row.CantidadGratis)

    Rule.formula(derive=models.ComprasLIN.PrecioLnea,
		calling=fn_compraslin_formula_formula_olhjv)

    # RuleType: parentCopy
	# Title: FechaInventario = parentcopy(StockTienda.FechaInventario)
	# Name: parentCopy_qpovr
	# Entity:  ComprasLIN
	# Comments: None

    #Rule.copy(derive=models.ComprasLIN.FechaInventario,
    #		from_parent=models.StockTienda.FechaInventario)


    app_logger.debug("..logic/declare_logic.py (logic == rules + code)")

