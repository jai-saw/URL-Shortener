from flask import Blueprint, render_template, redirect, url_for
from url_shortener.models import Url
from url_shortener.db import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("main/index.html")


@main.route("/<string:url_id>/")
def redirect_to_url(url_id):
    url = Url.query.filter_by(shortened_id=url_id).first()
    if url:
        url.clicks += 1
        db.session.add(url)
        db.session.commit()

        return redirect(url.original_url)
    return redirect(url_for("main.index"))
