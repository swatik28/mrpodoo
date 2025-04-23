{
    'name': 'Stock Aging Inventory', 
    'version': '18.0.1', 
    'summary': """Stock Aging Report""",
    'description': """Stock Aging Report""",
    'author': "Swati Khandelwal" ,
    'category': 'Swati Khandelwal',
    'depends': ['point_of_sale', 'stock'],
    'data': [
       'security/ir.model.access.csv', 
       'wizard/stock_wizard.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': True,
}

