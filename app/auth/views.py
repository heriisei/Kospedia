from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import User

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Menangani request route /register
    Menambah user ke database melalui from registerasi
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                        username=form.username.data,
                        nama_depan=form.nama_depan.data,
                        nama_belakang=form.nama_belakang.data,
                        kota_Cid=form.kota.data,
                        tanggal_lahir=form.tanggal_lahir.data,
                        password=form.password.data)

        #tambah user ke database
        db.session.add(user)
        db.session.commit()
        flash('Akun kamu sudah berhasil didaftarkan! Silakan login sekarang')

        #redirect ke halaman login
        return redirect(url_for('auth.login'))

    #load template registerasi
    return render_template('auth/register.html', form=form, title='Register - Kospedia')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login form untuk user
    """
    form = LoginForm()
    if form.validate_on_submit():

        #cek apakah user terdaftar dan mencocokkan password
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            #user dapat login
            login_user(user)

            #redirect ke profil setelah login
            if user.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('user.profil', username=current_user.username))

        #apabila form login tidak sesuai
        else:
            flash('Username atau Password salah')

    #load template login
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """
    Menangani permintaan route /logout
    Log out user dengan link
    """
    logout_user()
    flash('Kamu berhasil keluar')

    #redirect ke halaman home
    return redirect(url_for('auth.login'))
