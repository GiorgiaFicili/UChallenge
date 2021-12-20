from flask import session

from __init__ import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    if session.get('user_type') == 'school':
        return Schools.query.get(user_id)
    elif session.get('user_type') == 'student':
        return Students.query.get(user_id)


class Students(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(25), unique=True)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    img_file = db.Column(db.String(25), nullable=False, default="default.jpg")
    degrees = db.Column(db.String(60), nullable=False) # string or other type?

    def __repr__(self):
        return "User: {}, {}".format(Students.username, Students.email)


class Schools(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(25), unique=True)
    name = db.Column(db.String(25), nullable=False)
    img_file = db.Column(db.String(25), nullable=False, default="default.jpg")
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    degrees = db.Column(db.String(60), nullable=False) # string or other type?
    majors = db.Column(db.String(1000), nullable=False) # string or other type?
    address = db.Column(db.String(120), nullable=False)
    district = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return "User: {}, {}".format(Schools.username, Schools.email)



