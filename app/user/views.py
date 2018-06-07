from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
import jsonpickle

from . import user
from forms import KostFormUser, EditProfilUser
from .. import db
from ..models import User, Kost, City

def check_admin():
    """
    Hanya untuk user biasa
    """
    if current_user.is_admin:
        abort(403)

@user.route('/profil/<username>')
@login_required
def profil(username):
    """
    Render template profil pada route /profil
    """
    # users = User.query.with_entities(User.username)
    punyakost = db.session.query(Kost).filter(Kost.user_id==current_user.id, Kost.Kverified==True)
    # punyakost = db.session.query(Kost.Kname, Kost.Kaddress, Kost.city_Cid,
    #                             Kost.Kphone).filter(Kost.user_id==current_user.id, Kost.Kverified==True)
    result = punyakost.all()

    query = db.session.query(Kost).filter(Kost.Kverified==True).all()

    return render_template('user/profil.html', punyakost=punyakost, result=result, query=query, title='Profil')

@user.route('/profil/<username>/inputkost', methods=['GET', 'POST'])
@login_required
def user_add_kost(username):
    """
    Tambah kost ke database
    """
    check_admin()

    user_add_kost = True

    form = KostFormUser()
    if form.validate_on_submit():
        p_d = form.Kprice.data
        if p_d <= 300000:
            p_r = 1
        elif p_d >= 300001 and p_d <= 600000:
            p_r = 2
        elif p_d >= 600001 and p_d <= 900000:
            p_r = 3
        elif p_d >= 900001 and p_d <= 1200000:
            p_r = 4
        elif p_d >= 1200001:
            p_r = 5

        kost = Kost(Kname=form.Kname.data,
                    Kaddress=form.Kaddress.data,
                    city_Cid=form.Kota.data,
                    Kprice=form.Kprice.data,
                    Kprice_range=p_r,
                    Ktype=form.Ktype.data,
                    Kphone=form.Kphone.data,
                    user_id=current_user.id)
        try:
            # tambah kost ke database
            db.session.add(kost)
            db.session.commit()
            flash('Kost menunggu verifikasi Admin, Setelah itu akan muncul di halaman ini')
        except:
            #Apabila kost sudah pernah didaftarkan
            flash('Error: kost sudah didaftarkan')

        #redirect ke halaman kosts
        return redirect(url_for('user.profil', username=current_user.username))

    #load kost template
    return render_template('user/kosts/kost.html', action="Add",
                            user_add_kost=user_add_kost, form=form, title="Tambah Kost")

@user.route('/profil/<id>/editprofil', methods=['GET', 'POST'])
@login_required
def user_edit_profil(id):
    """
    edit profil
    """
    check_admin()

    user = User.query.get_or_404(id)
    form = EditProfilUser(obj=user)
    if form.validate_on_submit():
        user.username=form.username.data,
        user.nama_depan=form.nama_depan.data,
        user.nama_belakang=form.nama_belakang.data,
        user.kota_Cid=form.kota.data,
        user.tanggal_lahir=form.tanggal_lahir.data,
        db.session.commit()
        flash('Profil sudah berhasil diedit')

        return redirect(url_for('user.profil', username=current_user.username))

    form.tanggal_lahir.data = user.tanggal_lahir
    form.kota.data = user.kota_Cid
    form.nama_belakang.data = user.nama_belakang
    form.nama_depan = user.nama_depan
    form.username.data = user.username
    return render_template('user/edit_profil.html', action="Edit",
                            form=form, user=user, title="Edit Profil")

@user.route('/kost/<Kname>', methods=['GET', 'POST'])
@login_required
def kost_profil(Kname):

    kost = db.session.query(Kost).filter(Kost.Kname==Kname)

    return render_template('user/kosts/kost_profil.html', kost=kost, title='Profil Kost')
