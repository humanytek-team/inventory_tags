from odoo import _, api, fields, models  # noqa: F401


class StockPickingTag(models.Model):
    _name = "stock.picking.tag"
    _description = "Stock Picking Tag"

    name = fields.Char(
        required=True,
        index=True,
    )
    color = fields.Integer()
