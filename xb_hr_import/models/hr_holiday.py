from odoo import fields, models, api

class HrHoliday(models.Model):
    _inherit = 'hr.holiday'

    is_imported = fields.Boolean(string="Is_imported", default=False, readonly=1)

    
