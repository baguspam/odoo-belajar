from odoo import models, fields, api

class TokoKasir(models.Model):
    _name = 'toko.kasir'

    name = fields.Char(string='Nama Kasir')
    alamat = fields.Text(string='Alamat')
    tahun_masuk = fields.Integer(string='Tahun Masuk')
    indeks_prestasi = fields.Float(string='Indeks Prestasi')
    
    tanggal_lahir = fields.Date(string='Tanggal Lahir', default=fields.Date.today())
    waktu_bangun = fields.Datetime(string='Waktu Bangun Tidur')
    gender = fields.Selection(
        selection=[
            ('l', 'Laki-laki'),
            ('p', 'Perempuan'),
            ],
        string='Gender')
    
    created_at = fields.Date(string='Created at', default=fields.Date.today(), readonly=True)
    is_part_time = fields.Boolean(string='Part Time')