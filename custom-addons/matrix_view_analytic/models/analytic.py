from odoo import api, fields, models


class AnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    account_id = fields.Many2one(
        'account.analytic.account',
        'Project Account',
        ondelete='restrict',
        index=True,
        check_company=True,default=4
    )

class ProductProduct(models.Model):
    _inherit = "product.product"
    _order = 'sequence, default_code, name, id'
    
    sequence = fields.Integer(
        string='Sequence',
        help="Gives the sequence order when displaying a list of products.",
        default=10,
    )