# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today: GRAP (<http://www.grap.coop>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product - EAN13 Image',
    'summary': 'Generate EAN13 images for products',
    'version': '8.0.1.0.0',
    'category': 'Product',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'product',
    ],
    'data': [
        'views/view_product_product.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/product_product.xml',
    ],
    'external_dependencies': {
        'python': [
            'cairosvg',
            # 'barcode',
        ],
    },
}
