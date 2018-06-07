from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField

from ..models import User, City

class RegistrationForm(FlaskForm):
    """
    Form pembuatan akun baru
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
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
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField('Buat Akun')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email sudah digunakan')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username sudah digunakan')

class LoginForm(FlaskForm):
    """
    Form login user
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
