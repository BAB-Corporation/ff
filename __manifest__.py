{
    'name': 'Sales KPI Management',
    'version': '1.0',
    'summary': 'Manage Sales KPIs, Charts, Calculations, and Dashboards',
    'category': 'Sales',
    'author': 'Abdulkaraim Osman',
    'depends': ['base'],  # 'base' is available in both Community and Enterprise. Add more dependencies as required.
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/sales_kpi_views.xml',
        'views/sales_kpi_menus.xml',
        'data/sales_kpi_data.xml',  # Optional if you have demo data
    ],
    'license': 'OEEL-1',  # Enterprise license for compatibility, use LGPL-3 for Community modules
    'installable': True,
    'application': True,
    'auto_install': False,  # Set to True if you want it installed automatically when dependencies are met
}
