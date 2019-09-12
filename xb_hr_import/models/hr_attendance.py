from odoo import models, api, fields

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
    
    is_imported = fields.Boolean(string="Is_imported", default=False, readonly=1)
        
    @api.constrains('check_in', 'check_out', 'employee_id')
    def _check_validity(self):
        if self.is_imported:
            return True
        else:
            res = super(HrAttendance, self)._check_validity()
        