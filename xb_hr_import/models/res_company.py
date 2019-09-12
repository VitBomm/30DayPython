from odoo import fields, models, api, _


class Company(models.Model):
    _inherit = 'res.company'

    legal_leave = fields.Many2one('hr.leave.type', string="Legal Leave")
    unpaid_leave = fields.Many2one('hr.leave.type', string="Unpaid leave")
