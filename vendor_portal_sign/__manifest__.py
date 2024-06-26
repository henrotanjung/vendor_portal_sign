# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'purchase_rfp_online',
    'version' : '1.0',
    'summary': 'Provide a feature for vendor to priview and sign',
    'sequence': 1,
    'description': """
    Enable vendor to sign purchase quotation by their own side
    """,
    'category': 'Web',
    'website': '',
    'images' : ['images/purchase_form.png','images/portal_purchase.png','images/sign.png'],
    'price': 40,
    'currency': 'USD',
    'author': 'Henro S Tanjung',
    'maintainer': 'Henro Tanjung',
    'depends' : [
        # 'base',
        # 'sale_management',
        # 'portal',
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
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
}
