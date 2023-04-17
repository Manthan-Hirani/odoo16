{
    'name': 'Human Resource Management',
    'version': '1.0.0',
    'category': '',
    'sequence': -100,
    'author': 'Manthan',
    'summary': 'Complete human resource management system',
    'description': """Complete human resource management system for all""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/employee_detail_view.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
