from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'

    name = fields.Char(required=1)
    description = fields.Text()
    postcode = fields.Char(required=1)
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('North','North'), 
        ('South','South'), 
        ('East','East'),
        ('West', 'West')
        ])

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError('Please add valid number of bedrooms!')

