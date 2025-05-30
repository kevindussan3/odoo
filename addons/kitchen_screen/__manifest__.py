# -*- coding: utf-8 -*-
{
    'name': "kitchen_screen",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web','pos_restaurant'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        'security/pos_kitchen_screen_groups.xml',
        'views/pos_kitchen_screen_odoo_menus.xml',
        'security/kitchen_screen_model.xml',
        # 'data/ir_sequence.xml',
        'data/kitchen_screen_data.xml',
        # "data/sequence_data.xml",
        # "views/kitchen_screen_views.xml",
        "views/pos_order_views.xml",
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'kitchen_screen/static/src/js/fields_load.js',
            'kitchen_screen/static/src/js/order_pay.js',
            'kitchen_screen/static/src/js/order_button.js',
        ],
        'web.assets_backend': [
            'kitchen_screen/static/src/css/kitchen_screen.css',
            'kitchen_screen/static/src/js/kitchen_screen.js',
            # 'kitchen_screen/static/src/js/kitchen_screen_dashboard.js',
            'kitchen_screen/static/src/xml/kitchen_screen_templates.xml',
            'https://code.jquery.com/jquery-1.10.2.min.js',
            'https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js',
            'https://fonts.googleapis.com',
            'https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js',
            'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

