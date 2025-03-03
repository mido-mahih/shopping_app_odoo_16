from email.policy import default

from zeep.xsd import String

from odoo import models , fields ,api
from odoo.tools.populate import compute


class ShoppingApp(models.Model):
    _name = 'shopping.app'
    _description = 'app to small shopping process'
    # _inherit = ['mail.thread',"mail.activity.mixin"]
    _inherit = ['mail.thread',"mail.activity.mixin"]
    name = fields.Char(string="Vendor Name",required=1 , tracking=1)
    sales = fields.Float(tracking=1)
    salary =  fields.Float()
    truefalse = fields.Boolean()
    experience = fields.Text()







