# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': '',
    'sequence': -10,
    'author': 'Manthan',
    'summary': 'Complete hospital management system',
    'description': """Complete hospital management system for all""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/tags.xml',
        'views/setting.xml',
        'wizard/cancel_appointment.xml',
        'wizard/mail_patient.xml',
        'reports/patient_report.xml',
        'reports/report.xml',
        'schedule_action/appointment_cron.xml'
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}
