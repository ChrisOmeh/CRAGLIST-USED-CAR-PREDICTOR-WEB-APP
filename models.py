from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))