from flask import abort, render_template, Flask, redirect, url_for
from flask_login import current_user, login_required
from flask_googlemaps import Map, icons, GoogleMaps
from sqlalchemy import asc

from . import home
from .. import db
from forms import FilterKost
from ..models import Kost, City

@home.route('/', methods=['GET', 'POST'])
def welcome():
    """
    buat tampilan map
    """
    query = db.session.query(Kost).filter(Kost.Kverified==True).all()

    form = FilterKost()
    f_p = form.Harga.data #form price

    result = db.session.query(Kost).order_by(asc(Kost.Kprice))
    if form.validate_on_submit():
        if form.Kota.data is not 0 and form.Harga.data is not 0 and form.Jenis.data != 'N':
            result = db.session.query(Kost).filter(Kost.city_Cid==form.Kota.data,
                                                    Kost.Kprice_range==f_p,
                                                    Kost.Ktype==form.Jenis.data,
                                                    Kost.Kverified==True).order_by(asc(
                                                    Kost.Kprice))
            query = db.session.query(Kost).filter(Kost.city_Cid==form.Kota.data,
                                                    Kost.Kprice_range==f_p,
                                                    Kost.Ktype==form.Jenis.data,
                                                    Kost.Kverified==True)
        elif form.Kota.data is not 0 and form.Harga.data is not 0 and form.Jenis.data == 'N':
            result = db.session.query(Kost).filter(Kost.city_Cid==form.Kota.data,
                                                    Kost.Kprice_range==f_p,
                                                    Kost.Kverified==True).order_by(asc(
                                                    Kost.Kprice))
            query = db.session.query(Kost).filter(Kost.city_Cid==form.Kota.data,
                                                    Kost.Kprice_range==f_p,
                                                    Kost.Kverified==True)
        elif form.Kota.data is not 0 and form.Jenis.data != 'N':
            result = db.session.query(Kost).filter(Kost.city_Cid==form.Kota.data,
                                                    Kost.Ktype==form.Jenis.data,
                                                    Kost.Kverified==True).order_by(asc(
                                                    Kost.Kprice))
            query = db.session.query(Kost).filter(Kost.city_Cid==form.Kota.data,
                                                    Kost.Ktype==form.Jenis.data,
                                                    Kost.Kverified==True)
        elif form.Harga.data is not 0 and form.Jenis.data != 'N':
            result = db.session.query(Kost).filter(Kost.Kprice_range==f_p,
                                                    Kost.Ktype==form.Jenis.data,
                                                    Kost.Kverified==True).order_by(asc(
                                                    Kost.Kprice))
            query = db.session.query(Kost).filter(Kost.Kprice_range==f_p,
                                                    Kost.Ktype==form.Jenis.data,
                                                    Kost.Kverified==True)
        elif form.Kota.data is not 0 and form.Jenis.data == 'N':
            result = db.session.query(Kost).filter(Kost.city_Cid==form.Kota.data,
                                                    Kost.Kverified==True).order_by(asc(
                                                    Kost.Kprice))
            query = db.session.query(Kost).filter(Kost.city_Cid==form.Kota.data,
                                                    Kost.Kverified==True)
        elif form.Harga.data is not 0 and form.Jenis.data == 'N':
            result = db.session.query(Kost).filter(Kost.Kprice_range==f_p,
                                                    Kost.Kverified==True).order_by(asc(
                                                    Kost.Kprice))
            query = db.session.query(Kost).filter(Kost.Kprice_range==f_p,
                                                    Kost.Kverified==True)
        elif form.Jenis.data != 'N':
            result = db.session.query(Kost).filter(Kost.Ktype==form.Jenis.data,
                                                    Kost.Kverified==True).order_by(asc(
                                                    Kost.Kprice))
            query = db.session.query(Kost).filter(Kost.Ktype==form.Jenis.data,
                                                    Kost.Kverified==True)

    return render_template('home/index.html', query=query, form=form, result=result, title="Home")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    #mencegah akses dari non-admin user
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Admin Dashboard")

@home.route('/filter_button', methods=['GET', 'POST'])
def dropdown():
    button_kota = City.query.get(kota)


    return render_template('home/index.html', button_kota=button_kota)
