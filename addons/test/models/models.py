from odoo import fields, models

class TestModel(models.Model):
    _name = "test.model"
    _description = "This is Test Model."

    name = fields.Char("Name")
    name1 = fields.Char("Name1")
    name2 = fields.Char("Name2")
    name3 = fields.Char("Name3")
    name4 = fields.Char("Name4")