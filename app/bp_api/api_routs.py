import json

from flask import Blueprint, jsonify, session, request, redirect
from flask_login import login_required
from app.utils.discord_api import USER_GET_FUNC

from app import limiter

from app.utils.validation import VALIDATION

api_bp = Blueprint("api", __name__, template_folder="templates", static_folder="static", url_prefix="/api")


@api_bp.route("/discord_login", methods=["GET", "POST"])
@login_required
def discord_login():
    print(4)
    return jsonify({"auth_with_discord": bool(session.get("token"))})


@api_bp.route("/get", methods=["GET", "POST"])
@login_required
def discord_all():
    print("all api connect")
    print(session.get("token"))

    if not session.get("configurator"):
        return redirect("/create/token")
    session.modified = True

    if not request.headers.get("get"):
        return jsonify({
                           "error": "this error could not happen without hijacking requests or trying to create your own request, what are you trying to do?)"})

    print(">>", request.headers.get("configuration_name"))
    print(">>", session.get("configurator"))
    print(">>", session.get("configurator")[request.headers.get("configuration_name")])
    print(">>", session)

    data = {
        "auth_with_discord": bool(session.get("token")),
        "configuration_key": session.get("configurator")[request.headers.get("configuration_name")]
    }
    for i in request.headers.get("get").split("|"):
        if not i:
            continue
        data[i] = USER_GET_FUNC[i](session.get("user_guild_id"), session.get("user_bot_token"))
    # data = {
    #     "channels": get_user_channels(session.get("user_guild_id"), session.get("user_bot_token")),
    #     "roles": get_user_roles(session.get("user_guild_id"), session.get("user_bot_token")),
    #     "status": bool(session.get("user_bot_token")),
    # }
    print(data["configuration_key"])
    return jsonify(data)


@api_bp.route("/save", methods=["POST"])
@login_required
# @limiter.limit("10/minute")
def update_user_bot_config():
    print("connect to save API")
    # print(request.json)
    if not request.json:
        return jsonify({"status": "error"})

    # if code := (VALIDATION[request.headers.get("configuration_name")](request.json)):
    #     return jsonify({"status": "failed", "message": "Произошла ошибка при сохранении данных, пожалуйста,"
    #                                                    f" повторите запрос или обратитесь в поддержку."
    #                                                    f" Код ошибки: {code}"})


    try:
        # session["configurator"][request.headers.get("configuration_name")] = request.json
        session["configurator"][request.headers.get("configuration_name")] = json.dumps(request.json)
        print(session["configurator"])
        print(session)
    except Exception:
        return jsonify({"status": "failed",
                        "message": "Произошла какая-то ошибка, пожалуйста повторите запрос или обратитесь в поддержку"})
    session.modified = True
    return jsonify({"status": "ok", "message": "Обновления сохранены"})


@api_bp.route("/submit_token")
@login_required
def submit_token():
    return jsonify({"status": bool(session.get("user_bot_token"))})
