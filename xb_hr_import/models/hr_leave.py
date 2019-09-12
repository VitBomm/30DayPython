from odoo import models, api, fields

class HrLeave(models.Model):
    _inherit = 'hr.leave'
    
    is_imported = fields.Boolean(string="Is_imported", default=False, readonly=1)
        
    