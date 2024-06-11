from odoo import fields, models

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Task"

    name =fields.Char('Task Name')
    due_date = fields.Date()
    description = fields.Text()
    assign_to_id = fields.Many2one('res.partner')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='new')


    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_new(self):
        for rec in self:
            rec.state = 'new'

    def action_completed(self):
        for rec in self:
            rec.state = 'completed'