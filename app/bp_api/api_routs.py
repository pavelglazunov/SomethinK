import datetime
import json
import os
import smtplib
import string
import requests

from flask import Blueprint, jsonify, session, request, redirect
from flask import send_file
from flask_login import login_required, current_user, logout_user

from app.utils.discord_api import USER_GET_FUNC
from app.data import db_session
from app.data.users import User, Projects
from app.utils.validation import validation
from app.generator.generator import progres, generate
from app import limiter

api_bp = Blueprint("api", __name__, template_folder="templates", static_folder="static", url_prefix="/api")


def validate_project_id(project_id):
    try:
        project_id = int(project_id.split("_")[-1])
    except ValueError:
        return True

    if project_id < 0:
        return True

    return False


@api_bp.route("/discord_login", methods=["GET", "POST"])
@login_required
def discord_login():
    return jsonify({"auth_with_discord": bool(session.get("token"))})


@api_bp.route("/get", methods=["GET", "POST"])
@login_required
def discord_all():
    if not session.get("configurator"):
        return redirect("/create/token")
    session.modified = True

    if not request.headers.get("get"):
        return jsonify({
            "error": "this error could not happen without hijacking requests or trying to create your own request, what are you trying to do?)"})

    data = {
        "auth_with_discord": bool(session.get("token")),
        "configuration_key": json.dumps(session.get("configurator")[request.headers.get("configuration_name")])
    }

    for i in request.headers.get("get").split("|"):
        if not i:
            continue
        data[i] = USER_GET_FUNC[i](session.get("user_guild_id"), session.get("user_bot_token"))

    return jsonify(data)


@api_bp.route("/save", methods=["POST"])
@login_required
def update_user_bot_config():
    if not request.json:
        return jsonify({"status": "error"})

    try:
        session["configurator"][request.headers.get("configuration_name")] = request.json

    except Exception:
        return jsonify({"status": "failed",
                        "message": "Произошла какая-то ошибка, пожалуйста повторите запрос или обратитесь в поддержку"})
    session.modified = True
    return jsonify({"status": "ok", "message": "Обновления сохранены"})


@api_bp.route("/submit_token")
@login_required
def submit_token():
    return jsonify({"status": bool(session.get("user_bot_token"))})


@api_bp.route("/edit", methods=["GET", "POST"])
@login_required
def start_editing():
    project_id = request.headers.get("project_id", "-1")
    if validate_project_id(project_id):
        return jsonify({"status": "error", "message": f"Код ошибки: Hack attack? Stop please"})

    db_sess = db_session.create_session()
    project_config_json = db_sess.query(Projects).filter(Projects.id == project_id).first().config_json

    session["configurator"] = project_config_json
    session["bot_is_editing"] = True

    session["user_bot_token"] = project_config_json.get("bot_metadata", {}).get("bot_token")

    session["user_guild_id"] = requests.get(f"https://discord.com/api/v8/users/@me/guilds",
                                            headers={"Authorization": f"Bot {session['user_bot_token']}"}).json()[
        0]["id"]

    return jsonify({"status": "ok", "url": "/create/moderation"})


@api_bp.route("/remove", methods=["GET", "POST"])
@login_required
def remove_bot():
    project_id = request.headers.get("project_id", "-1")
    if validate_project_id(project_id):
        return jsonify({"status": "error", "message": f"Код ошибки: Hack attack? Stop please"})

    db_sess = db_session.create_session()

    project = db_sess.query(Projects).filter(Projects.id == project_id).first()

    db_sess.delete(project)
    db_sess.commit()

    return jsonify({"status": "ok", "message": "Бот успешно удален"})


@api_bp.route("/download", methods=["GET", "POST"])
def download_bot():
    project_id = request.headers.get("project_id")

    if validate_project_id(project_id):
        return jsonify({"status": "error", "message": f"Код ошибки: Hack attack? Stop please"})

    db_sess = db_session.create_session()

    project_configurator = db_sess.query(Projects).filter(
        Projects.id == int(project_id.split("_")[-1])).first().config_json

    generate(dict(project_configurator))
    return send_file(
        f"{os.getcwd()}\\app\\generator\\{project_configurator.get('bot_metadata', {}).get('project_name', 'Unknown')}.zip",
        as_attachment=True)


@api_bp.route("/remove_account", methods=["GET", "POST"])
@login_required
def remove_account():
    user_password = request.headers.get("password")

    db_sess = db_session.create_session()

    user = db_sess.query(User).filter(User.email == current_user.email).first()

    if not user.check_password(user_password):
        print("incorrect password")
        return jsonify({"status": "error", "message": "Неверный пароль"})

    user_projects = db_sess.query(Projects).filter(Projects.author_id == user.id).all()
    logout_user()
    session.clear()

    db_sess.delete(user)
    for pr in user_projects:
        db_sess.delete(pr)
    db_sess.commit()

    return jsonify({"status": "ok", "message": "Аккаунт удален"})


@api_bp.route("/start_creating", methods=["POST"])
@login_required
def start_creating():
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == current_user.email).first()
    user_projects = db_sess.query(Projects).filter(Projects.author_id == user.id).all()

    if len(user_projects) >= 5:
        return jsonify({"status": "error", "message": f"Достигнул лимит в 5 ботов"})

    if error_code := validation(dict(session.get("configurator"))):
        return jsonify({"status": "error", "message": f"Код ошибки: {error_code}"})

    project_name = request.json["project_name"]
    for i in project_name:
        if not (i.lower() in string.ascii_lowercase):
            return jsonify({"status": "error", "message": f"Некорректное имя"})

    session["configurator"]["bot_metadata"] = {
        "bot_token": session.get("user_bot_token"),
        "project_name": project_name,
        "everyone_id": session["everyone_id"]
    }

    generate(dict(session.get("configurator")))

    project = Projects()
    project.author_id = user.id
    project.bot_name = project_name
    project.config_json = session["configurator"]
    project.create_datetime = datetime.datetime.now()

    db_sess.add(project)
    db_sess.commit()

    return send_file(f"{os.getcwd()}\\app\\generator\\{project_name}.zip", as_attachment=True)


@api_bp.route("/progres")
def get_progres():
    return jsonify({"progres": progres})


@api_bp.route("/login", methods=["GET", "POST"])
# @limiter.limit("1/minute") #  <----- IT WORK, I'M FROM THE FUTURE, DON'T TOUCH
def login_user():
    email = request.headers.get("email")
    if not email:
        return jsonify({"status": "error", "message": "Укажите почту"})

    message = "Код для входа"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("somethinkbots@gmail.com", "")

    # print("send mail")
    return jsonify({"status": "ok"})
    pass
