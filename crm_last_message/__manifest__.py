{
    'name': 'CRM Last Message',
    'version': '1.0.0',
    'summary': 'Display the latest email message on CRM opportunities',
    'description': """

CRM Last Message
================
Show the most recent email message on the CRM opportunity form and list views.
""",
    'category': 'CRM',
    'author': 'Francisco Toro',
    'email': 'ftc.odoo.test@gmail.com',
    'license': 'LGPL-3',
    'price': 19.0,
    'currency': 'USD',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_view.xml',
    ],
    'images': [
        'static/description/icon.png',
        'static/description/screenshot.png',
        'static/description/screenshot2.png',
        'static/description/thumbnail.png',
        'static/description/banner2.png',
	'static/images/banner.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
