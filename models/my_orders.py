from email.policy import default

from odoo import models , fields ,api
from odoo.exceptions import ValidationError


class Orders(models.Model):
    _name = 'shopping.app.orders'
    _description = 'app to small shopping process'
    _inherit = ["mail.thread","mail.activity.mixin"]
    client_name = fields.Char(required=1 , tracking=1)
    date= fields.Date(string="Date",default=fields.Date.today)
    phone = fields.Char(required=1)
    description = fields.Text()
    address = fields.Text()
    discount = fields.Float()
    payment_method = fields.Selection([("1","Cash"),("2","Visa")],default='1')
    item_ids = fields.One2many('order.items','order_id')
    total_invoice_price = fields.Float(string="Total Invoice Price",compute="_compute_total_invoice_price",store=1)
    num1 = fields.Float()
    num2 = fields.Float()
    num3 = fields.Float(string="Result",readonly=1)
    status = fields.Selection([("new", "New"), ("review", "Review"), ("approve", "Approve"), ("refuse", "Refuse")],
                              default="new")

    # _sql_constraints = [
    #     ("unique_name","unique(client_name)","Name IS Exist"  )
    # ]
    _sql_constraints = [
        ("unique_name","unique(client_name)","Name IS Exist")
    ]
    @api.constrains("phone")
    def _check_phone_is_eleven_characters(self):
        for record in self:
            if len(record.phone) != 11:
                raise ValidationError("Phone Must Be Eleven Characters")

    # will not store in database
    num_percent = fields.Float(string="Num Percent" , compute="_compute_num_percent")
    @api.onchange("num3")
    def _compute_num_percent(self):
        for record in self:
            record.num_percent = record.num3 / 100

    @api.depends("item_ids.total_price")
    def _compute_total_invoice_price(self):
        for record in self:
            record.total_invoice_price = sum(record.item_ids.mapped("total_price"))
    @api.onchange('num1','num2')
    def _calculate_result(self):
        self.num3 = self.num2 + self.num1




    def review_event(self):
        for r in self:
            r.status = "review"

    def approve_event(self):
        for r in self:
            r.status = "approve"

    def refuse_event(self):
        for r in self:
            r.status = "refuse"

    def clear_event(self):
        for r in self:
            r.status = "new"

    def back_event(self):
        for r in self:
            status = {
                "approve": "review",
                "refuse": "review",
                "review": "new",
            }
            r.status = status[r.status]


class Items(models.Model):
        _name = 'order.items'
        _description = 'app to small shopping process'
        _inherit = ["mail.thread","mail.activity.mixin"]
        product_name = fields.Char(required=1 , tracking=1)
        price = fields.Float(require=1,tracking=1)
        quantity = fields.Integer(require=1)
        description = fields.Text()
        order_id = fields.Many2one('shopping.app.orders')
        total_price = fields.Float(string="Total Price",compute="_compute_total_price",store=1)
        status = fields.Selection([("new","New"),("review","Review"),("approve","Approve"),("refuse","Refuse")],default="new")
        @api.depends("price","quantity")
        def _compute_total_price(self):
            for record in self:
                record.total_price = record.price * record.quantity
        # data from client

        client_name = fields.Char(related="order_id.client_name",string="client name")
        phone = fields.Char(related="order_id.phone",string="phone")
        address = fields.Text(related="order_id.address",string="address")
        date = fields.Date(related="order_id.date",string="date")


        _sql_constraints = [
            ("check_price_bigger_than_ten","check(price > 10)","price must be bigger than 10")
        ]


        def review_event(self):
            for r in self:
                r.status = "review"
        def approve_event(self):
            for r in self:
                r.status = "approve"
        def refuse_event(self):
            for r in self:
                r.status = "refuse"
        def clear_event(self):
            for r in self:
                r.status = "new"
        def back_event(self):
            for r in self:
                status = {
                    "approve":"review",
                    "refuse":"review",
                    "review":"new",
                }
                r.status = status[r.status]




