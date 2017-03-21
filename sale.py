from openerp import models, fields, api, _
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
from datetime import time, datetime
from openerp import SUPERUSER_ID
from openerp import tools
from openerp.tools.translate import _


class sale_order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    no_compra = fields.Char('No. Compra', size=128)
    requiere_addenda = fields.Boolean('Addenda?', related="partner_id.requiere_addenda")
