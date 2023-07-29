import requests

from flask import Blueprint, render_template, session, redirect
from flask_login import login_required

from app import limiter
from app.forms.create_forms import *
from app.utils.discord_api import get_user_roles, get_user_channels, check_token_valid, get_everyone_id
from app.bp_create.base_config import BASE_CONFIG

create_bp = Blueprint("create", __name__, template_folder="templates", static_folder="static", url_prefix="/create")


def has_bot_token():
    return session.get("user_bot_token")


@create_bp.route("/token", methods=["GET", "POST"])
@login_required
def get_token():
    form = Token()

    if form.validate_on_submit():

        if not check_token_valid(form.token.data):
            return render_template("create/token.html",
                                   form=form,
                                   status=False,
                                   message="некорректный токен",
                                   from_submit=True,
                                   auth_with_discord=bool(session.get("token"))
                                   )

        session["user_bot_token"] = session.get("user_bot_token") if session.get("user_bot_token") else form.token.data
        session["user_guild_id"] = requests.get(f"https://discord.com/api/v8/users/@me/guilds",
                                                headers={"Authorization": f"Bot {session['user_bot_token']}"}).json()[
            0]["id"]
        session["configurator"] = session.get("configurator") if session.get("configurator") else BASE_CONFIG.copy()

        session["everyone_id"] = get_everyone_id(session.get("user_guild_id"), session.get("user_bot_token"))[0]

        return render_template("create/token.html", form=form, status=True, message="токен подтвержден",
                               from_submit=True, auth_with_discord=bool(session.get("token")))

    form.token.data = session.get("user_bot_token")
    return render_template("create/token.html",
                           form=form,
                           status=bool(session.get("user_bot_token")),
                           auth_with_discord=bool(session.get("token")),
                           )


@create_bp.route("/moderation", methods=["GET", "POST"])
@limiter.exempt
@login_required
def get_moderation():
    if not has_bot_token():
        return redirect("/create/token")
    if session.get("token"):
        return render_template("create/moder.html",
                               auth_with_discord=True,
                               channels=get_user_channels(session.get("user_guild_id"),
                                                          session.get("user_bot_token")),
                               roles=get_user_roles(session.get("user_guild_id"), session.get("user_bot_token")),
                               status=True)
    return render_template("create/moder.html", auth_with_discord=False,
                           roles=[],
                           status=True)


@create_bp.route("/messages")
@login_required
def get_messages():
    if not has_bot_token():
        return redirect("/create/token")
    return render_template("create/messages.html", status=True)


@create_bp.route("/roles")
@login_required
def get_roles():
    if not has_bot_token():
        return redirect("/create/token")
    return render_template("create/roles.html", status=True)


@create_bp.route("/social_media")
@login_required
def get_sm():
    if not has_bot_token():
        return redirect("/create/token")
    return render_template("create/sm.html", status=True)


@create_bp.route("/another")
@login_required
def get_another():
    if not has_bot_token():
        return redirect("/create/token")
    return render_template("create/another.html", status=True)


@create_bp.route("/settings")
@login_required
def get_settings():
    if not has_bot_token():
        return redirect("/create/token")
    return render_template("create/settings.html", status=True)


@create_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_page():
    if not has_bot_token():
        return redirect("/create/token")
    return render_template("create/create_bot.html", status=True)
