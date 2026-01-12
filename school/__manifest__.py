# -*- coding: utf-8 -*-
{
    'name': "School Management",

    'summary': "School Event Manager",

    'description': """
        School Management Module
        ========================
        
        This module allows managing:
        * Students and their personal data
        * Classes and tutor assignments
        * School events (absences, delays, congratulations, behavior)
        
        Main features:
        * Student control by class
        * Event registration related to students
        * Management of tutors linked to the HR module
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

