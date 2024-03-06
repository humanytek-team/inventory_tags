from odoo import _, api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    tag_ids = fields.Many2many(
        comodel_name="stock.picking.tag",
    )
