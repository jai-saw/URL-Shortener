import random
import string
import validators

from flask import Blueprint, request, redirect, url_for, flash, session
from datetime import date
from url_shortener.db import db
from url_shortener.models import Url
from flask_login import current_user, login_required

url = Blueprint("url", __name__, url_prefix="/urls")


@url.route("/", methods=["POST"])
def create():
    long_url = request.form.get("url")

    if not long_url or not validators.url(long_url):
        flash("A valid URL is required!", "danger")
        return redirect(url_for("main.index"))

    url_id = "".join(random.choice(string.digits + string.ascii_letters) for _ in range(0, 6))

    user_id = current_user.id if current_user.is_authenticated else None
    if not user_id:
        try:
            logged_out_links = session["logged_out_links"]
            logged_out_links.append((long_url, url_id))
        except KeyError:
            session["logged_out_links"] = [(long_url, url_id)]

    created_url = Url(original_url=long_url, shortened_id=url_id, created_on=date.today(), user_id=user_id)
    db.session.add(created_url)
    db.session.commit()

    flash(f"Created URL: {request.url_root + url_id}", "success")
    return redirect(url_for("main.index"))


@url.route("/<string:url_id>/delete/", methods=["POST"])
@login_required
def delete(url_id):
    query = Url.query.filter_by(shortened_id=url_id, user_id=current_user.id)
    url = query.first()
    if not url:
        flash("Invalid short link!", "danger")
        return redirect(url_for("main.index"))

    query.delete()
    db.session.commit()

    flash("Link removed!", "success")
    return redirect(url_for("main.index"))
