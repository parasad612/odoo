from odoo import api, fields, models

class pkclCustomers(models.Model):
    _name = 'pkcl.customers'
    _description = 'Customers of Hero Solutions'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')