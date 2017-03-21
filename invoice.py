from openerp import models, fields, api, _
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
from datetime import time, datetime
from openerp import SUPERUSER_ID
from openerp import tools
from openerp.tools.translate import _
from openerp.exceptions import UserError, RedirectWarning, ValidationError

import sys
reload(sys)  
sys.setdefaultencoding('utf8')

import logging
_logger = logging.getLogger(__name__)
try:
    from SOAPpy import WSDL
except:
    _logger.warning('Install Package SOAPpy with the command "sudo apt-get install python-soappy".')

from pytz import timezone
import pytz
from datetime import timedelta

from xml.dom.minidom import Document , parse , parseString
from xml.dom import minidom

_logger = logging.getLogger(__name__)

import hashlib
import tempfile
import base64
import os
import codecs
from datetime import datetime, timedelta
from openerp.modules import module

class account_invoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    requiere_addenda = fields.Boolean('Addenda?', related="partner_id.requiere_addenda")

    @api.one
    def _get_facturae_invoice_xml_data(self):
        xml_data = super(account_invoice, self)._get_facturae_invoice_xml_data()
        if self.partner_id.requiere_addenda and self.type == 'out_invoice':
            addenda = self.insert_addenda_prueba()
            if type(addenda) == list:
                addenda = addenda[0]
            addenda = addenda.replace('<cfdi>','').replace('</cfdi>','')
            original =  ("</cfdi:Comprobante>").encode('utf8')
            replacement = (addenda + "</cfdi:Comprobante>").encode('utf8')
            xml_data_cadena = xml_data[0][1]
            xml_data_2 =(xml_data[0][0],xml_data_cadena.replace(original, replacement))
            return xml_data_2
        return xml_data

    @api.multi
    def insert_addenda_prueba(self):
        account_browse = self

        ####################### IMPORTANTE  ########################
        dom = parseString("<cfdi></cfdi>")
        root = dom.getElementsByTagNameNS('*', 'cfdi')[0]
        #nodelines = root.getElementsByTagName('cfdi:Conceptos')
        addenda = dom.createElement('cfdi:Addenda') # creas el elemento addenda
        root.appendChild(addenda)

        self.env.cr.execute("""select id from sale_order 
            where name like '%s' """ % ('%'+self.origin+'%',))

        cr_res = self.env.cr.fetchall()
        order_ids = [x[0] for x in cr_res if x]

        orden_compra = ""
        if order_ids:
            sale_br = self.env['sale.order'].browse(order_ids)
            orden_compra = sale_br[0].no_compra

        factura = dom.createElement('factura')
        serie =  ""

        if self.journal_id:
            if self.journal_id.sequence_id and self.journal_id.sequence_id.approval_ids:
                serie = self.journal_id.sequence_id.approval_ids[-1].serie

        factura.setAttribute('serie', serie)
        factura.setAttribute('folio', self.number)
        factura.setAttribute('noproveedor', self.partner_id.no_proveedor)

        if not orden_compra:
            raise UserError(_("Error\nLa factura debe provenir de un Pedido de Venta."))
        factura.setAttribute('ordencompra', orden_compra)

        addenda.appendChild(factura)


        data_xml = base64.encodestring(root.toxml('UTF-8'))
        xml_string = base64.decodestring(data_xml)
        return xml_string