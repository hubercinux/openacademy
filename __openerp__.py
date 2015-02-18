# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Modulo de prueba""",

    'description': """
        Modulo de prueba
    """,

    'author': "Jhonny Martínez Espinoza",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/openacademy.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}