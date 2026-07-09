    # -*- coding: utf-8 -*-
{
    'name': "Phone Call Notes",

    'summary': "Phone call logging module for Contacts",

    'description': 
    """
    Logs customer phone calls from Odoo Contacts.

    Features:
    - Customer
    - Phone Number
    - Call Status
    - Notes
    - User
    - Date

    """,

    'author': "Deepak Gulani",
    'website': "https://github.com/Devgulani/odoo-phone-call-notes",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'category': 'Sales',
    'version': '18.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 
                'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/phone_call_log_views.xml',
        'views/res_partner_views.xml',
    ],

    'installable': True,

    'application': False,
}

