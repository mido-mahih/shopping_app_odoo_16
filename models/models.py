from zeep.xsd import String

from odoo import models , fields ,api
from odoo.tools.populate import compute


class ShoppingApp(models.Model):
    _name = 'shopping.app'
    _description = 'app to small shopping process'
    name = fields.Char(string="Vendor Name")
    sales = fields.Float()
    salary =  fields.Float()
    truefalse = fields.Boolean()
    experience = fields.Text()


class Orders(models.Model):
    _name = 'shopping.app.orders'
    _description = 'app to small shopping process'
    client_name = fields.Char()
    date= fields.Date()
    phone = fields.Char()
    description = fields.Text()
    address = fields.Text()
    discount = fields.Float()
    payment_method = fields.Selection([("1","Cash"),("2","Visa")])
    item_ids = fields.One2many('order.items','order_id')
    total_invoice_price = fields.Float(string="Total Invoice Price",compute="_compute_total_invoice_price",store=1)
    @api.depends("item_ids.total_price")
    def _compute_total_invoice_price(self):
        for record in self:
            record.total_invoice_price = sum(record.item_ids.mapped("total_price"))


class Items(models.Model):
        _name = 'order.items'
        _description = 'app to small shopping process'
        product_name = fields.Char()
        price = fields.Float()
        quantity = fields.Integer()
        description = fields.Text()
        order_id = fields.Many2one('shopping.app.orders')
        total_price = fields.Float(string="Total Price",compute="_compute_total_price",store=1)
        @api.depends("price","quantity")
        def _compute_total_price(self):
            for record in self:
                record.total_price = record.price * record.quantity
        # data from client
        client_name = fields.Char(related="order_id.client_name",string="client name",store=1)
        phone = fields.Char(related="order_id.phone",string="phone",store=1)
        address = fields.Text(related="order_id.address",string="address",store=1)
        date = fields.Date(related="order_id.date",string="date",store=1)





        # total_price = fields.Float(string="Total Price", compute="_compute_total_price", store=1)
        # @api.depends('price','quantity')
        # def _compute_total_price(self):
        #     for record in self:
        #         record.total_price = self.price *self.quantity



