from database import models
from safrs import jsonapi_attr
from sqlalchemy.orm import relationship, remote, foreign
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
#models.ComprasCAB.Manager = relationship(models.ComprasCAB, 
#    cascade_backrefs=False, backref='Manages',
#    primaryjoin=remote(models.ComprasLIN.AlbarnCompra) == foreign(models.ComprasCAB.SerieNmero))
