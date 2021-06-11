# -*- coding: utf-8 -*-
from odoo import api, fields, models,  _
from odoo.exceptions import AccessError, UserError, ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    components = fields.Many2one('mrp.bom', compute='compute_components')

    def compute_components(self):
        for rec in self:
            bom = self.env['mrp.bom'].search([('product_tmpl_id', '=', rec.product_id.product_tmpl_id.id)], limit=1)
            rec.components = bom.id

    def calculate_discount(self, price_unit, discount):
        value = int(price_unit * (discount/100))
        return value




class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def calculate_page_total(self):
    	value = 0
    	for index, line in enumerate(self.order_line):
    		if index <= 6:
    			value += line.price_subtotal
    	return value

    def calculate_global_discount(self, untaxed):
        discount = 0
        for line in self.order_line:
            discount += line.calculate_discount(line.price_unit, line.discount)
        print(discount)
        return discount