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

declare_logic_message = "LAC 5.x migrated Logic"  # printed in api_logic_server.py

def declare_logic():
    pass