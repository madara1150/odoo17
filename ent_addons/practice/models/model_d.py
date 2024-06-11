from odoo import models
class ModelD(models.Model):
    _name = 'model.d'
    # จะไม่สร้าง record write edit create เพื่อมาเก็บ log
    _log_access = False