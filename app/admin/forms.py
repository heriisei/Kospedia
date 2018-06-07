from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import City

class KostFormAdmin (FlaskForm):
    """
    Form untuk admin menambah / edit kost
    """
    Kname = StringField('Nama Kost', validators=[DataRequired()])
    Kaddress = StringField('Alamat Kost', validators=[DataRequired()])
    Kphone = StringField('Nomor Telepon', validators=[DataRequired()])
    Kota = SelectField('Kota Tempat Tinggal', validators=[DataRequired()], choices=[
                                (1, 'Jakarta Pusat'),
                                (2, 'Jakarta Barat'),
                                (3, 'Jakarta Selatan'),
                                (4, 'Jakarta Timur'),
                                (5, 'Jakarta Utara'),
                                (6, 'Kepulauan Seribu')], coerce=int)
    Kprice = IntegerField('Harga per-Bulan', validators=[DataRequired()])
    Ktype = SelectField('Jenis Kost', validators=[DataRequired()], choices=[
                                ('Kost Laki-Laki', 'Kost Laki-Laki'),
                                ('Kost Perempuan', 'Kost Perempuan'),
                                ('Kost Pasutri', 'Kost Pasutri')])
    Klat = DecimalField('Latitude Map', validators=[DataRequired()])
    Klng = DecimalField('Longtitude Map', validators=[DataRequired()])
    submit = SubmitField('Simpan')
