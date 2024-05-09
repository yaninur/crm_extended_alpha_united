# -*- coding: utf-8 -*-
{
    'name': 'CRM Sales Team Stage Notifier',
    'version': '16.0.0.0',
    'category': '',
    'summary': 'Automatically Notify The Next Responsible Team Upon CRM Stage Change',
    'description': """-----""",
    'license': 'LGPL-3',
    'author': '7D',
    'website': "https://www.7d.com.kw",
    'depends': ['base','crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_team_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 95.00,
    'currency': 'USD',
    'images': ['static/description/cover.png'],
}
