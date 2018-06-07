from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

from .. import db

class FilterKost (FlaskForm):
    """
    Filter kota berdasar kategori
    """
    Kota = SelectField(choices=[
                                (0, 'Kota'),
                                (1, 'Jakarta Pusat'),
                                (2, 'Jakarta Barat'),
                                (3, 'Jakarta Selatan'),
                                (4, 'Jakarta Timur'),
                                (5, 'Jakarta Utara'),
                                (6, 'Kepulauan Seribu')], coerce=int)
    Harga = SelectField(choices=[
                                (0, 'Harga'),
                                (1, '<= Rp 300.000'),
                                (2, 'Rp 300.001 - Rp 600.000'),
                                (3, 'Rp 600.001 - Rp 900.000'),
                                (4, 'Rp 900.001 - Rp 1.200.000'),
                                (5, '>= Rp 1.200.001')], coerce=int)
    Jenis = SelectField(choices=[
                                ('N', 'Jenis'),
                                ('Kost Laki-Laki', 'Kost Laki-Laki'),
                                ('Kost Perempuan', 'Kost Perempuan'),
                                ('Kost Pasutri', 'Kost Pasutri')])
    submit = SubmitField('Cari')
