from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Buat table User
    """

    #nama tabel dalam bentuk plural karena singular
    #sudah dipakai di Model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    nama_depan = db.Column(db.String(60), index=True)
    nama_belakang = db.Column(db.String(60), index=True)
    kota_Cid = db.Column(db.Integer, db.ForeignKey('cities.Cid'))
    tanggal_lahir = db.Column(db.Date, index=True)
    password_hash = db.Column(db.String(128))
    #kost_id = db.Column(db.Integer, db.ForeignKey('kosts.id'))
    kosts = db.relationship('Kost', backref='user', lazy='dynamic')
    is_admin = db.Column(db.Boolean, default=False)
    is_kost_owner = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Mencegah password untuk diakses
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Merubah password ke dalam bentuk hash
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Cek hash sesuai dengan password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Kost(db.Model):
    """
    Buat table Kost
    """

    __tablename__ = 'kosts'

    Kid = db.Column(db.Integer, primary_key=True)
    Kname = db.Column(db.String(60), index=True)
    Kaddress = db.Column(db.String(100), index=True)
    city_Cid = db.Column(db.Integer, db.ForeignKey('cities.Cid'))
    Kphone = db.Column(db.String(20))
    Kprice = db.Column(db.Integer, index=True)
    Kprice_range = db.Column(db.Integer, index=True)
    Ktype = db.Column(db.String(20), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    Kverified = db.Column(db.Boolean, default=False)
    Klat = db.Column(db.DECIMAL(10, 8))
    Klng = db.Column(db.DECIMAL(11,8))

    def __repr__(self):
        return '<Kost: {}>'.format(self.Kname)

class City(db.Model):
    """
    Buat table City
    """

    __tablename__ = 'cities'

    Cid = db.Column(db.Integer, primary_key=True)
    kota = db.Column(db.String(60), index=True)
    provinsi = db.Column(db.String(60), index=True)
    kosts = db.relationship('Kost', backref='city', lazy='dynamic')
    users = db.relationship('User', backref='city', lazy='dynamic')

    def __repr__(self):
        return '<City: {}>'.format(self.kota)
