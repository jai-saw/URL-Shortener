import os

from flask import Flask
from url_shortener.views.main import main
from url_shortener.views.url import url
from url_shortener.views.auth import auth
from url_shortener.db import db
from url_shortener.models import User
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app=app)
login_manager.login_view = "auth.login"
login_manager.login_message_category = "danger"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


SQLALCHEMY_DATABASE_URI = "postgresql://db:5432/url_shortener"  # os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///database.db")

app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", os.urandom(6)),
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(app)
app.app_context().push()
db.create_all()

app.register_blueprint(main)
app.register_blueprint(url)
app.register_blueprint(auth)
