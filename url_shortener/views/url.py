import random
import string

from flask import Blueprint, request, redirect, url_for, flash
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

    url_id = "".join(random.choice(string.digits + string.ascii_letters) for _ in range(0, 6))
    created_url = Url(original_url=long_url, shortened_id=url_id, created_on=date.today())
    db.session.add(created_url)
    db.session.commit()

    flash(f"Created URL: {request.url_root + url_id}", "success")
    return redirect(url_for("main.index"))
