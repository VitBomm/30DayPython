{
    'name': 'HR Import',
    'author': 'xboss',
    'category': 'Human Resources',
    'website': 'xboss.com',
    'depends': [
        'base',
        'hr',
        'xb_hr_time_mngt',
    ],
    'data': [
        'wizard/hr_import.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
