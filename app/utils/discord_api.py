import requests


def get_user_roles(guild, token):
    return [(role["id"], role["name"]) for role in requests.get(f"https://discord.com/api/v8/guilds/{guild}/roles",
                                                                headers={"Authorization": f"Bot {token}"}).json()]


def get_everyone_id(guild, token):
    return [role["id"] for role in requests.get(f"https://discord.com/api/v8/guilds/{guild}/roles",
                                                headers={"Authorization": f"Bot {token}"}).json() if
            role["name"] == "@everyone"]


def get_user_channels(guild, token):
    r = requests.get(f"https://discord.com/api/v8/guilds/{guild}/channels",
                     headers={"Authorization": f"Bot {token}"}).json()

    return {"text": [(i["id"], i["name"]) for i in r if i["type"] == 0],
            "voice": [(i["id"], i["name"]) for i in r if i["type"] == 2],
            "category": [(i["id"], i["name"]) for i in r if i["type"] == 4]}


def check_token_valid(token):
    r = requests.get(f"https://discord.com/api/v8/users/@me",
                     headers={"Authorization": f"Bot {token}"})

    return r.status_code == 200


USER_GET_FUNC = {
    "channels": get_user_channels,
    "roles": get_user_roles
}
