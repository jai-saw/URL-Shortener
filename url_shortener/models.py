from url_shortener.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    user = db.relationship("Url", backref="user", cascade="delete,all")


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    original_url = db.Column(db.String, nullable=False)
    shortened_id = db.Column(db.String, nullable=False)
    created_on = db.Column(db.Date, nullable=False)
    clicks = db.Column(db.Integer, nullable=False, default=0)
