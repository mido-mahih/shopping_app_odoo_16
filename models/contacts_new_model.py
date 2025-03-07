from odoo import fields , models , api


class  NewContacts(models.Model):
    _inherit = "res.partner"
    my_note = fields.Text()
    my_sales_team_phone = fields.Char()