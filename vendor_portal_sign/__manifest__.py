# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'purchase_rfp_online',
    'version' : '1.0',
    'summary': 'Provide a feature for vendor to priview and sign',
    'sequence': 1,
    'description': """
    Gsi Help
    """,
    'category': 'Web',
    'website': '',
    'images' : [],
    'depends' : [
        'base',
        'sale_management',
        'portal',
        'purchase',
        ],
    'data': [
        'views/purchase_order_view.xml',
        'views/portal_templates.xml'
        
    ],
    'demo': [
        
    ],
    'qweb': [],
      
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
