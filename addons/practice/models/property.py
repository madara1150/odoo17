from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'

    name = fields.Char(required=1, default='New', size=12)
    description = fields.Text()
    postcode = fields.Char(required=1)
    date_availability = fields.Date()
    expected_price = fields.Float(digits=(0,5))
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'), 
        ('south','South'), 
        ('east','East'),
        ('west', 'West')
        ],default='north')
    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
    ], default='draft')

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exist!')
    ]

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError('Please add valid number of bedrooms!')
            
    def action_draft(self):
        for rec in self:
            print("enside draft action")
            rec.state = 'draft'
            # rec.write({
            #     'state' : 'draft'
            # })

    def action_sold(self):
        for rec in self:
            print("enside sold action")
            rec.state = 'sold'
            rec.write({
                'state' : 'sold'
            })


    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(Property, self).create(vals)
    #     print("inside create method")
    #     return res
    
    # @api.model
    # def _search(self,domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super(Property, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     print("inside search method")
    #     return res
    
    # def write(self, vals):
    #     res = super(Property, self).write(vals)
    #     print("inside write method")
    #     return res
    
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print("inside unlink method")
    #     return res
