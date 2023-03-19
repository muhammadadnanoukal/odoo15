#
# @Author: KSOLVES India Private Limited
# @Email: sales@ksolves.com
#


from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    display_stock = fields.Boolean(string='Display Stock of products in POS', default=True)
    minimum_stock_alert = fields.Integer(string='Minimum Limit to change the stock color for the product', default=0)
    allow_order_when_product_out_of_stock = fields.Boolean(string='Allow Order when Product is Out Of Stock',
                                                           default=True)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_display_stock = fields.Boolean(related='pos_config_id.display_stock', readonly=False)
    pos_minimum_stock_alert = fields.Integer(related='pos_config_id.minimum_stock_alert', readonly=False)
    pos_allow_order_when_product_out_of_stock = fields.Boolean(related='pos_config_id.allow_order_when_product_out_of_stock', readonly=False)
