from flask import Blueprint, request, redirect, url_for
from datetime import date
from url_shortener.db import db
from url_shortener.models import Url

url = Blueprint("url", __name__, url_prefix="/urls")


@url.route("/<string:url_id>")
def show(url_id):
    return url_id


@url.route("/", methods=["POST"])
def create():
    # TODO: Add custom form validation (or use WTForms)
    long_url = request.form.get("url")

    # TODO: URL id generation
    id = "random"
    created_url = Url(original_url=long_url, shortened_id=id, created_on=date.today())
    db.session.add(created_url)
    db.session.commit()
    return redirect(url_for("main.index"))
