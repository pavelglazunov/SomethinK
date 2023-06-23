import sys

import requests
from flask import Blueprint, render_template, session, redirect
from flask_login import login_required, current_user

from app import limiter
from app.forms.create_forms import *
from zenora import APIClient, GuildBase

# from discord.utils import get as discord_get

import config as api_config
from app.utils.discord_api import get_user_roles, get_user_channels, check_token_valid

create_bp = Blueprint("create", __name__, template_folder="templates", static_folder="static", url_prefix="/create")


# @create_bp.route("/", methods=["GET", "POST"])
# @login_required
# def main_create():
#     if session.get("token"):
#         form = ServersSelect()
#

#
#         form.servers.choices = user_owner_guilds
#
#         if form.is_submitted():
#             session["guild_id"] = form.servers.data
#
#             # guild = discord_get()
#
#             print(session["token"])
#             print(form.servers.data)
#             print(get_user_roles(form.servers.data, api_config.TEST_BOT_TOKEN))
#             print(get_user_channels(form.servers.data, api_config.TEST_BOT_TOKEN))
#             # r = requests.get(f"https://discord.com/api/v8/guilds/{form.servers.data}/roles",
#             headers={"Authorization": f"Bot {api_config.TEST_BOT_TOKEN}"})
#             # r1 = requests.get(f"https://discord.com/api/v8/oauth2/@me",
#             headers={"Authorization": f"Bearer {session['token']}"})
#             # print(r.text)  # 1076824052007714937 | 1076824052007714937
#             # print(r1.text)
#
#             return render_template("create/create_main.html", form=form, has_form=True)
#
#         # if session.get("guild_id"):
#         #     print("here")
#         # form.servers.process_data(2)
#         # form.servers.default = 2
#         # form.process()
#
#         print(user_owner_guilds)
#         return render_template("create/create_main.html", form=form, has_form=True)
#
#     return render_template("create/create_main.html", has_form=False)

# def has_bot_token(func):
#     def wrapper(*args, **kwargs):
#         if not session.get("user_bot_token"):
#             return redirect("/create/token")
#         func()
#
#     wrapper.__name__ = func.__name__
#     return wrapper

def has_bot_token():
    return session.get("user_bot_token")


@create_bp.route("/token", methods=["GET", "POST"])
@login_required
def get_token():
    form = Token()

    if form.validate_on_submit():
        if not check_token_valid(form.token.data):
            print("invalid token")
            return render_template("create/token.html",
                                   form=form,
                                   status=False,
                                   message="некорректный токен",
                                   from_submit=True,
                                   auth_with_discord=bool(session.get("token"))
                                   )

        session["user_bot_token"] = session.get("user_bot_token", form.token.data)
        session["user_guild_id"] = requests.get(f"https://discord.com/api/v8/users/@me/guilds",
                                                headers={"Authorization": f"Bot {session['user_bot_token']}"}).json()[0]["id"]
        session["configurator"] = session.get("configurator", {
            "moderation": {},
            "messages": {},
            "roles": {},
            "social_media": {},
            "another": {},
            "settings": {},
            "customization": {}
        })

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
    # if session.get("token"):
    #     return render_template("create/sm.html")
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


@create_bp.route("/create")
def create_page():
    ...
