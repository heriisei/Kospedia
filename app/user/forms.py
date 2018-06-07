from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, PasswordField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField

from .. import db
from ..models import City

class KostFormUser (FlaskForm):
    """
    Form untuk admin menambah / edit kost
    """

    # def city_query():
    #     return db.session.query(City).all()

    Kname = StringField('Nama Kost', validators=[DataRequired()])
    Kaddress = StringField('Alamat Kost', validators=[DataRequired()])
    # Kota = QuerySelectField('Kota', query_factory=city_query,
    #                         allow_blank=False,
    #                         get_pk=lambda a: a.Cid,
    #                         get_label=lambda a: a.kota)
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
    Kphone = StringField('Nomor Telepon', validators=[DataRequired()])
    submit = SubmitField('Simpan')

class EditProfilUser (FlaskForm):
    """
    Edit profil
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=60)])
    nama_depan = StringField('Nama Depan', validators=[DataRequired(), Length(max=60)])
    nama_belakang = StringField('Nama Belakang', validators=[DataRequired(), Length(max=60)])
    kota = SelectField('Kota Tempat Tinggal', validators=[DataRequired()], choices=[
                                (1, 'Jakarta Pusat'),
                                (2, 'Jakarta Barat'),
                                (3, 'Jakarta Selatan'),
                                (4, 'Jakarta Timur'),
                                (5, 'Jakarta Utara'),
                                (6, 'Kepulauan Seribu')], coerce=int)
    tanggal_lahir = DateField('Tanggal Lahir', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Simpan')
