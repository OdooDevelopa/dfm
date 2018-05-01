# -*- coding: utf-8 -*-

{
    'name': "Discuss Facebook Messenger",
    'version': '0.1',
    'author': 'Odoo SA',
    'maintainer': 'Odoo SA',
    'website': "http://www.odoo.com",
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    'sequence': 1,
    'description': """Long description of module's purpose""",
    'summary': """Sample addon for Odoo""",
    'depends': ['base', 'mail'],
    'data': [
        'views/views.xml',
        'views/dfm_config_view.xml',
        'views/dfm_menu_view.xml',
    ],
    'demo': [],
    'qweb': [],
    # 'js': ['static/src/js/first_module.js',],
    # 'css': ['static/src/css/web_example.css',],
    # 'images': ['static/description/icon.png',],
    'auto_install': False,
    'application': True,
    'installable': True,
    'external_dependencies': {'python' : ['fbchat']}
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
}
