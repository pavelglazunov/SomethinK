import os

from flask import Blueprint, render_template, redirect, send_from_directory
from flask_login import login_required, current_user

from app.data import db_session
from app.data.users import User, Projects
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


@main_bp.route('/robots.txt')
def static_from_root():
    return send_from_directory(main_bp.static_folder, "robots.txt")


@main_bp.route("/user/<int:user_id>")
@login_required
def profile(user_id):
    if user_id == current_user.id:
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        user_projects = db_sess.query(Projects).filter(Projects.author_id == user.id).all()

        return render_template("user/profile.html", data={
            "username": user.name,
            "user_project": [{"name": project.bot_name, "id": project.id} for project in user_projects]
        })
    else:
        return render_template("errors/404.html", error_code="404"), 404


@main_bp.route("/privacy")
def privacy_page():
    return render_template("policy/main_policy.html")


@main_bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(main_bp.root_path, "static"), "favicon.ico",
                               mimetype='image/vnd.microsoft.icon')
