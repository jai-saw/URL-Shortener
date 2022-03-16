import os

from flask import Flask
from url_shortener.views.main import main
from url_shortener.views.url import url
from url_shortener.db import db

app = Flask(__name__)

# For Heroku
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///database.db")
if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

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
