# sales_kpi.py
from odoo import models, fields

class SalesKPI(models.Model):
    _name = 'sales.kpi'
    _description = 'Sales KPI Data'

    name = fields.Char(string='KPI Name', required=True)
    jan = fields.Float(string='January')
    feb = fields.Float(string='February')
    mar = fields.Float(string='March')
    apr = fields.Float(string='April')
    may = fields.Float(string='May')
    jun = fields.Float(string='June')
    jul = fields.Float(string='July')
    aug = fields.Float(string='August')
    sep = fields.Float(string='September')
    oct = fields.Float(string='October')
    nov = fields.Float(string='November')
    dec = fields.Float(string='December')
    total = fields.Float(string='Total')
    average_deal_size = fields.Float(string='Average Deal Size')
    required_deals = fields.Integer(string='Required Deals')
