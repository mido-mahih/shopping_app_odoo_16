from email.policy import default

from zeep.xsd import String

from odoo import models , fields ,api
from odoo.tools.populate import compute


class ShoppingApp(models.Model):
    _name = 'shopping.app'
    _description = 'app to small shopping process'
    _inherit = ['mail.thread',"mail.activity.mixin"]
    # _inherit = ['mail.thread',"mail.activity.mixin"]
    name = fields.Char(string="Vendor Name",required=1 , tracking=1)
    sales = fields.Float(tracking=1)
    salary =  fields.Float()
    truefalse = fields.Boolean()
    experience = fields.Text()
    states = fields.Selection([("new","New"),("reviewed","Reviewed"),("approved","Approved"),("refused","Refused")] , default="new")

    def event_reviewed(self):
        self.states = "reviewed"
    def event_approved(self):
        self.states = "approved"
    def event_refused(self):
        self.states = "refused"
    def event_go_back(self):
        for r in self:
            states = {
                'reviewed':'new',
                'approved':'reviewed',
                'refused':'reviewed'
            }
            r.states = states[r.states]
    def event_clear(self):
        for r in self:

            r.states = 'new'



