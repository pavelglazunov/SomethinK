import datetime
import secrets
import string

from flask import Blueprint, render_template, session, redirect, request, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from zenora import APIClient

from app.forms.user import RegisterForm, LoginForm
from app.data import db_session
from app.data.users import User
from app.utils.auntifications import send_authentication_code

import app.ds_config as api_config

# from SomethinKTelegramBot.api.auth_api import generate_api_token

client = APIClient(api_config.TOKEN, client_secret=api_config.CLIENT_SECRET)

oauth_bp = Blueprint("oauth", __name__, template_folder="templates", static_folder="static", url_prefix="/auth")


@oauth_bp.route("/")
def auth():
    return render_template("auth/select_auth_type.html", redirect_oauth_url=api_config.OAUTH_URL)


@oauth_bp.route("/login", methods=["GET", "POST"])
def login():
    # form = LoginForm()
    # if form.validate_on_submit():
    #     db_sess = db_session.create_session()
    #     user = db_sess.query(User).filter(User.email == form.email.data).first()
    #
    #     if user and user.check_password(form.password.data):
    #         login_user(user, remember=True)
    #
    #         session["is_auth"] = True
    #
    #         return redirect("/../")
    #     return render_template('auth/login.html',
    #                            message="Неправильный логин или пароль",
    #                            form=form)
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

        # user.set_password(''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(30)))
        db_sess.add(user)

    user = db_sess.query(User).filter(User.email == email).first()
    user.discord_token = session["token"]
    user.name = username

    db_sess.commit()
    login_user(user, remember=True, duration=datetime.timedelta(days=7))

    session["auth_with_discord"] = True

    return redirect(f"/user/{current_user.id}")


# @oauth_bp.route("/register", methods=["GET", "POST"])
# def register():
# form = RegisterForm()
# if form.validate_on_submit():
# if form.password.data != form.password_again.data:
#     return render_template('auth/register.html', title='Регистрация',
#                            form=form,
#                            message="Пароли не совпадают")
# db_sess = db_session.create_session()
# if len(form.name.data) > 20:
#     return render_template('auth/register.html', title='Регистрация',
#                            form=form,
#                            message="Имя слишком длинное")
# if db_sess.query(User).filter(User.email == form.email.data).first():
#     return render_template('auth/register.html', title='Регистрация',
#                            form=form,
#                            message="Пользователь с такой почтой уже есть")

# user = User()
# user.name = form.name.data
# user.email = form.email.data
# user.confirm_user = False
# user.premium = False
# user.created_date = datetime.datetime.now()
#
# user.set_password(form.password.data)
#
# db_sess.add(user)
# db_sess.commit()
#
# login_user(user, remember=True, duration=datetime.timedelta(days=7))
# return redirect(f"confirm")
# return render_template('auth/register.html')


# @oauth_bp.route("/confirm")
# @login_required
# def confirm_user():
#     code = generate_api_token(current_user.email)
#     return render_template("/auth/confirm.html", code=code)


@oauth_bp.route("/logout")
@login_required
def logout():
    session["is_auth"] = False
    session["token"] = ""
    session["auth_with_discord"] = False

    session["user_bot_token"] = ""
    session["user_guild_id"] = ""

    session.clear()

    logout_user()
    return redirect("/")
