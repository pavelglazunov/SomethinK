import json

from flask import Blueprint, jsonify, session, request, redirect
from flask_login import login_required
from app.utils.discord_api import USER_GET_FUNC

from app import limiter

from app.utils.validation import VALIDATION, validation
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


@api_bp.route("/start_creating", methods=["POST"])
@login_required
def start_creating():
    print(55555555)
    print(session['configurator']['messages'])
    print(session.get("configurator"))
    print(dict(session.get("configurator")))
    print(json.dumps(dict(session.get("configurator")), ensure_ascii=False))
    # if not request.json:
    #     return jsonify({"status": "error"})
    # if not _json(request.json):
    #     return jsonify({"status": "error"})

    if not (error_code := validation(dict(session.get("configurator")))):
        return jsonify({"status": "error", "message": f"Код ошибки: {error_code}"})

    # print(request.json)
    # for cfg_name, cfg_json in session.get("configurator").items():
    #     if code := (VALIDATION[cfg_name](json.loads(cfg_json))):
    #         return jsonify({"status": "failed", "message": "Произошла ошибка при сохранении данных, пожалуйста,"
    #                                                        f" повторите запрос или обратитесь в поддержку."
    #                                                        f" Код ошибки: {code}"})
    #     print(cfg_name, cfg_json)

    generate(dict(session.get("configurator")))
    print(session.get("configurator"))
    print(dict(session.get("configurator")))
    print(json.dumps(dict(session.get("configurator")), ensure_ascii=False))

    return jsonify({"status": "ok"})


@api_bp.route("/progres")
def get_progres():
    return jsonify({"progres": progres})
