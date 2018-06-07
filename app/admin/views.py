from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import KostFormAdmin
from .. import db
from ..models import Kost

def check_admin():
    """
    Mencegah non-admin user untuk masuk
    """
    if not current_user.is_admin:
        abort(403)

#Kosts Views
@admin.route('/kosts', methods=['GET', 'POST'])
@login_required
def list_kosts():
    """
    List semua kost
    """
    check_admin()

    kosts = Kost.query.all()

    return render_template('admin/kosts/kosts.html', kosts=kosts, title="Kosts")

@admin.route('/kosts/add', methods=['GET', 'POST'])
@login_required
def add_kost():
    """
    Tambah kost ke database
    """
    check_admin()

    add_kost = True

    form = KostFormAdmin()
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
                    Kphone=form.Kphone.data,
                    city_Cid=form.Kota.data,
                    Kprice=form.Kprice.data,
                    Kprice_range=p_r,
                    Ktype=form.Ktype.data,
                    user_id=current_user.id,
                    Kverified=True,
                    Klat=form.Klat.data,
                    Klng=form.Klng.data)
        try:
            #tambah kost ke database
            db.session.add(kost)
            db.session.commit()
            flash('Kost sudah berhasil ditambahkan')
        except:
            #Apabila kost sudah pernah didaftarkan
            flash('Error: kost sudah didaftarkan')

        #redirect ke halaman kosts
        return redirect(url_for('admin.list_kosts'))

    #load kost template
    return render_template('admin/kosts/kost.html', action="Add",
                            add_kost=add_kost, form=form, title="Tambah Kost")

@admin.route('/kosts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_kost(id):
    """
    Edit detail kost
    """
    check_admin()

    add_kost = False

    kost = Kost.query.get_or_404(id)
    form = KostFormAdmin(obj=kost)
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

        kost.Kname = form.Kname.data
        kost.Kaddress = form.Kaddress.data
        kost.Kphone = form.Kphone.data
        kost.city_Cid = form.Kota.data
        kost.Kprice = form.Kprice.data
        kost.Kprice_range = p_r
        kost.Ktype = form.Ktype.data
        kost.Klat = form.Klat.data
        kost.Klng = form.Klng.data
        db.session.commit()
        flash('Kost sudah berhasil diedit')

        #redirect ke halaman kosts
        return redirect(url_for('admin.list_kosts'))

    form.Klng.data = kost.Klng
    form.Klat.data = kost.Klat
    form.Ktype.data = kost.Ktype
    form.Kprice.data = kost.Kprice
    form.Kota.data = kost.city_Cid
    form.Kphone.data = kost.Kphone
    form.Kaddress.data = kost.Kaddress
    form.Kname.data = kost.Kname
    return render_template('admin/kosts/kost.html', action="Edit",
                            add_kost=add_kost, form=form,
                            kost=kost, title="Edit Kost")

@admin.route('kosts/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_kost(id):
    """
    Hapus kost dari database
    """
    check_admin()

    kost = Kost.query.get_or_404(id)
    db.session.delete(kost)
    db.session.commit()
    flash("Kost sudah berhasil dihapus")

    #redirect ke halaman kosts
    return redirect(url_for('admin.list_kosts'))

    return render_template(title="Hapus Kost")

@admin.route('/kosts/verify/<int:id>', methods=['GET', 'POST'])
@login_required
def verifikasi_kost(id):
    """
    Verifikasi detail kost
    """
    check_admin()

    kost = Kost.query.get_or_404(id)
    if kost.Kverified == True:
        kost.Kverified=False
        flash("Kost Ditangguhkan")
    else:
        kost.Kverified=True
        flash("Kost Disetujui")
    db.session.commit()

    return redirect(url_for('admin.list_kosts'))

    return render_template(title="Verifikasi Kost")
