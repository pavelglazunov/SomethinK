import datetime

from flask import Blueprint, render_template, session, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from zenora import APIClient

from app.data import db_session
from app.data.users import User

import app.ds_config as api_config

client = APIClient(api_config.TOKEN, client_secret=api_config.CLIENT_SECRET)

oauth_bp = Blueprint("oauth", __name__, template_folder="templates", static_folder="static", url_prefix="/auth")


@oauth_bp.route("/")
def auth():
    return render_template("auth/select_auth_type.html", redirect_oauth_url=api_config.OAUTH_URL)


@oauth_bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template('auth/login.html', title='Авторизация')


@oauth_bp.route("/discord")
def login_discord():
    code = request.args["code"]
    access_token = client.oauth.get_access_token(code, api_config.REDIRECT_URL).access_token

    session["token"] = access_token

    bearer_client = APIClient(access_token, bearer=True)

    discord_user = bearer_client.users.get_current_user()
    username, email, discriminator = discord_user.username, discord_user.email, discord_user.discriminator

    db_sess = db_session.create_session()

    user = db_sess.query(User).filter(User.email == email).first()
    if not user:
        user = User()
        user.name = username
        user.email = email

        db_sess.add(user)

    user = db_sess.query(User).filter(User.email == email).first()
    user.discord_token = session["token"]
    user.name = username

    db_sess.commit()
    login_user(user, remember=True, duration=datetime.timedelta(days=7))

    session["auth_with_discord"] = True

    return redirect(f"/user/{current_user.id}")


@oauth_bp.route("/logout")
@login_required
def logout():
    session.clear()

    logout_user()
    return redirect("/")
