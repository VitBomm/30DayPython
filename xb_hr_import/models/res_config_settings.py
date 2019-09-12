from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    legal_leave = fields.Many2one('hr.leave.type', string="Legal Leave", related="company_id.legal_leave", readonly=False)
    unpaid_leave = fields.Many2one('hr.leave.type', string="Unpaid Leave", related="company_id.unpaid_leave", readonly=False)
