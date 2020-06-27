from odoo import models, fields, api

class Toko(models.Model):
    _name = 'toko.struk'

    name = fields.Char(string='No. Struk')
    harga = fields.Float(string='Harga')