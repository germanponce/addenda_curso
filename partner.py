from openerp import models, fields, api, _
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
from datetime import time, datetime
from openerp import SUPERUSER_ID
from openerp import tools
from openerp.tools.translate import _


class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    no_proveedor = fields.Char("No. Proveedor")
    requiere_addenda = fields.Boolean('Addenda?')
