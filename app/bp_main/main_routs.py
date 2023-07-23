import os

from flask import Blueprint, render_template, session, redirect, request, send_from_directory
from flask_login import login_required, login_user, logout_user, current_user

from app.data import db_session
from app.data.users import User
from app import login_manager

main_bp = Blueprint("main", __name__, template_folder="templates", static_folder="static")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@main_bp.route('/')
def to_main():
    return redirect('/home')


@main_bp.route("/home")
def index():
    return render_template("main/index.html")


@main_bp.route("/user/<int:user_id>")
@login_required
def profile(user_id):
    if user_id == current_user.id:
        return render_template("user/profile.html", data=user_id)
    else:
        return "Это не ваша страница, что вы тут забыли???"


@main_bp.route('/favicon.ico')
def favicon():
    print("====>>", os.getcwd())
    return send_from_directory(os.getcwd(), 'static/favicon/favicon.ico', mimetype='image/vnd.microsoft.icon')

# @main_bp.route("/api")
# def apt():
#     print(44444)
#     return {"name": "good"}
