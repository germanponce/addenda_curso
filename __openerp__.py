# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015 http://www.argil.mx/
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@argil.mx)
############################################################################
#    Coded by: german_442 email: (german.ponce@argil.mx)
##############################################################################

{
    'name': 'Addenda Ejemplo Curso',
    'version': '1',
    "author" : "German Ponce Dominguez / Argil Consulting",
    "category" : "TannerMH",
    "summary": "Modulo para manejo de Addendas, Ford, Chrysler y Addenda Manual.",
    'description': """

Proceso
=======

1. Se requiere ingresar el No. Proveedor en la ficha de Cliente.
2. Se requiere añadir el No. Orden de Compra en el Pedido.

    """,
    "website" : "http://www.argil.mx",
    "license" : "AGPL-3",
    "depends" : ["account","sale","stock","l10n_mx_einvoice","sale_stock"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    'partner.xml',
                    'sale.xml',
                    'invoice.xml',
                    ],
    "installable" : True,
    "active" : False,
}
