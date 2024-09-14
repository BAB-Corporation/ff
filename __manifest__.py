{
    'name': 'Sales KPI Management',
    'version': '1.0',
    'summary': 'Manage Sales KPIs, Charts, Calculations, and Dashboards',
    'category': 'Sales',
    'author': 'Abdulkaraim Osman',  # Your name is correctly placed
    'depends': ['base'],  # Add more module dependencies if needed
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/sales_kpi_views.xml',
        'views/sales_kpi_menus.xml',
        'data/sales_kpi_data.xml',  # Optional if you have data to preload
    ],
    'installable': True,
    'application': True,
}
