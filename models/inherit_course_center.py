from odoo import api, fields, models, _


class AmalCenter(models.Model):
    _inherit = "res.partner"

    is_student = fields.Boolean(string="Is Student")
    is_teacher = fields.Boolean(string="Is Teacher")
