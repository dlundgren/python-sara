from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .Setting import Setting

"""
These help define a base to extend from so you don't have to set the bind_key on each entity
"""
class MainCustomBase(db.Model):
    __bind_key__ = 'main_custom'
    __abstract__ = True

class MainCoreBase(db.Model):
    __bind_key__ = 'main_core'
    __abstract__ = True

class WarehouseCustomBase(db.Model):
    __bind_key__ = 'warehouse_custom'
    __abstract__ = True

class WarehouseCoreBase(db.Model):
    __bind_key__ = 'warehouse_core'
    __abstract__ = True

"""
Import all of your entities here
"""