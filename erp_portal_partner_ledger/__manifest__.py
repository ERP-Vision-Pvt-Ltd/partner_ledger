{
    'name': 'Portal Partner Ledger',
    'author': "ERP VISION",
    'version': '16.0.0.2',
    'summary': """This application empowers your customers to take control of their financial interactions with your business. Designed with user-friendliness and transparency in mind, this innovative tool seamlessly integrates with your Odoo ERP system, offering your customers a hassle-free way to access, track, and manage their ledger information.""",
    'description': """This application empowers your customers to take control of their financial interactions with your business. Designed with user-friendliness and transparency in mind, this innovative tool seamlessly integrates with your Odoo ERP system, offering your customers a hassle-free way to access, track, and manage their ledger information.""",
    'category': 'portal',
    'website': 'https://www.erpvision.pk',
    'license': 'LGPL-3',
    'depends': ['account_accountant', 'website'],
    'data': [
        'views/partner_ledger.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': '99.0',
    'currency': 'USD',
    'images': ['static/description/cover/main.gif'],
    'maintainer':'ERP VISION',
    'sequence': 1,
}
