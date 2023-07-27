import datetime
import json
import os
import string
import requests

from flask import Blueprint, jsonify, session, request, redirect
from flask import send_file
from flask_login import login_required, current_user
from app.utils.discord_api import USER_GET_FUNC

from app.data import db_session
from app.data.users import User, Projects

from app import limiter

from app.utils.validation import validation
from app.generator.generator import progres, generate

api_bp = Blueprint("api", __name__, template_folder="templates", static_folder="static", url_prefix="/api")


@api_bp.route("/discord_login", methods=["GET", "POST"])
@login_required
def discord_login():
    return jsonify({"auth_with_discord": bool(session.get("token"))})


@api_bp.route("/get", methods=["GET", "POST"])
@login_required
def discord_all():
    print("all api connect")

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

    print(data)
    return jsonify(data)


@api_bp.route("/save", methods=["POST"])
@login_required
def update_user_bot_config():
    print("connect to save API")

    if not request.json:
        return jsonify({"status": "error"})

    # if code := (VALIDATION[request.headers.get("configuration_name")](request.json)):
    #     return jsonify({"status": "failed", "message": "Произошла ошибка при сохранении данных, пожалуйста,"
    #                                                    f" повторите запрос или обратитесь в поддержку."
    #                                                    f" Код ошибки: {code}"})

    try:
        # session["configurator"][request.headers.get("configuration_name")] = request.json
        session["configurator"][request.headers.get("configuration_name")] = request.json

    except Exception:
        return jsonify({"status": "failed",
                        "message": "Произошла какая-то ошибка, пожалуйста повторите запрос или обратитесь в поддержку"})
    session.modified = True
    print(session["configurator"][request.headers.get("configuration_name")])
    return jsonify({"status": "ok", "message": "Обновления сохранены"})


@api_bp.route("/submit_token")
@login_required
def submit_token():
    return jsonify({"status": bool(session.get("user_bot_token"))})


@api_bp.route("/edit", methods=["GET", "POST"])
@login_required
def start_editing():
    project_id = request.headers.get("project_id", "-1")
    try:
        project_id = int(project_id.split("_")[-1])
    except ValueError:
        return jsonify({"status": "error", "message": f"Код ошибки: Hack attack? Stop please"})

    if project_id < 0:
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
    print(project_id)
    try:
        project_id = int(project_id.split("_")[-1])
    except ValueError:
        return jsonify({"status": "error", "message": f"Код ошибки: Hack attack? Stop please"})

    if project_id < 0:
        return jsonify({"status": "error", "message": f"Код ошибки: Hack attack? Stop please"})

    print(f"WARNING: user DELETE bot: {project_id}")

    db_sess = db_session.create_session()

    project = db_sess.query(Projects).filter(Projects.id == project_id).first()
    print(project)
    db_sess.delete(project)
    db_sess.commit()

    # db_sess = db_session.create_session()
    # project_config_json = db_sess.query(Projects).filter(Projects.id == project_id).first().config_json
    # print(project_config_json)
    #
    # session["configurator"] = project_config_json
    # session["bot_is_editing"] = True
    #
    # session["user_bot_token"] = project_config_json.get("bot_metadata", {}).get("bot_token")
    #
    # print(session["user_bot_token"])
    # session["user_guild_id"] = requests.get(f"https://discord.com/api/v8/users/@me/guilds",
    #                                         headers={"Authorization": f"Bot {session['user_bot_token']}"}).json()[
    #     0]["id"]

    return jsonify({"status": "ok", "url": "/create/moderation"})


@api_bp.route("/start_creating", methods=["POST"])
@login_required
def start_creating():
    print(55555555)
    # print(session['configurator']['messages'])
    # print(session.get("configurator"))
    print(dict(session.get("configurator")))

    # print(json.dumps(dict(session.get("configurator")), ensure_ascii=False))
    # if not request.json:
    #     return jsonify({"status": "error"})
    # if not _json(request.json):
    #     return jsonify({"status": "error"})
    #

    if error_code := validation(dict(session.get("configurator"))):
        return jsonify({"status": "error", "message": f"Код ошибки: {error_code}"})

    # print(request.json)
    # for cfg_name, cfg_json in session.get("configurator").items():
    #     if code := (VALIDATION[cfg_name](json.loads(cfg_json))):
    #         return jsonify({"status": "failed", "message": "Произошла ошибка при сохранении данных, пожалуйста,"
    #                                                        f" повторите запрос или обратитесь в поддержку."
    #                                                        f" Код ошибки: {code}"})
    #     print(cfg_name, cfg_json)
    project_name = request.json["project_name"]
    for i in project_name:
        if not (i.lower() in string.ascii_lowercase):
            return jsonify({"status": "error", "message": f"Некорректное имя"})

    print(project_name)
    session["configurator"]["bot_metadata"] = {
        "bot_token": session.get("user_bot_token"),
        "project_name": project_name,
        "everyone_id": session["everyone_id"]
    }

    print(session["configurator"]["bot_metadata"])
    # generate(dict(session.get("configurator")))

    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == current_user.email).first()
    # print(user.id, current_user.id)

    project = Projects()
    project.author_id = user.id
    project.bot_name = project_name
    project.config_json = session["configurator"]
    project.create_datetime = datetime.datetime.now()

    db_sess.add(project)
    db_sess.commit()

    # print(session.get("configurator"))
    # print(dict(session.get("configurator")))
    # print(json.dumps(dict(session.get("configurator")), ensure_ascii=False))
    # print()
    return send_file(f"{os.getcwd()}\\app\\generator\\{project_name}.zip", as_attachment=True)


@api_bp.route("/progres")
def get_progres():
    return jsonify({"progres": progres})
