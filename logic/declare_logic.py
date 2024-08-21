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
    Rule.sum(derive=models.ComprasCAB.BaseIVAGeneral,
                as_sum_of=models.ComprasLIN.Importe, where=lambda row: row.tpcIVA == 21)
    
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

    Rule.sum(derive=models.ComprasCAB.BaseIVAAceitesPastas, 
        as_sum_of=models.ComprasLIN.Importe,
            where=lambda row: row.tpcIVA==5)
    
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

    Rule.sum(derive=models.ComprasCAB.BaseIVACero, 
        as_sum_of=models.ComprasLIN.Importe,
        where=lambda row: row.tpcIVA==0)

    # RuleType: sum
	# Title: BaseIVAReducido = sum(Compras_LIN_List.Importe where tpcIVA=10)
	# Name: sum_drdjf
	# Entity: ComprasCab
	# Comments: None

    Rule.sum(derive=models.ComprasCAB.BaseIVAReducido, 
        as_sum_of=models.ComprasLIN.Importe,
        where=lambda row: row.tpcIVA==10)
    
    app_logger.debug("..logic/declare_logic.py (logic == rules + code)")

