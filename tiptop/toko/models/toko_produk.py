from odoo import models, fields, api

class TokoProduk(models.Model):
    _name = 'toko.produk'

    name = fields.Char(string='Nama Produk')