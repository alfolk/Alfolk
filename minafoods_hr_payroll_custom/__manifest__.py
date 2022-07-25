# -*- coding: utf-8 -*-
{
    'name': 'Mina Foods Payroll Custom',
    'version': '15.1',
    'author': 'Muhammad Nasser',
    'category': 'Localization',
    'depends': ['base',
                'hr_payroll',
                'rm_hr_attendance_sheet'],
    'description': """ Mina Foods Payroll Custom """,
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/add_deduct_wizard_view.xml',
        'views/hr_contract_view.xml',
    ],
}
