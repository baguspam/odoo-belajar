from odoo import models, fields, api
from . import toko_kasir

class Toko(models.Model):
    _name = 'toko.struk'

    name = fields.Char(string='No. Struk')
    harga = fields.Float(string='Harga')
    kasir_id = fields.Many2one(
        comodel_name='toko.kasir',
        string='Kasir'
        )