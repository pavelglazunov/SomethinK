import requests
import config as cfg


def get_user_roles(guild, token):
    return [(role["id"], role["name"]) for role in requests.get(f"https://discord.com/api/v8/guilds/{guild}/roles",
                                                                headers={"Authorization": f"Bot {token}"}).json()]


def get_user_channels(guild, token):
    r = requests.get(f"https://discord.com/api/v8/guilds/{guild}/channels",
                     headers={"Authorization": f"Bot {token}"}).json()

    # print("here", r)
    return {"text": [(i["id"], i["name"]) for i in r if i["type"] == 0],
            "voice": [(i["id"], i["name"]) for i in r if i["type"] == 2],
            "category": [(i["id"], i["name"]) for i in r if i["type"] == 4]}


def check_token_valid(token):
    r = requests.get(f"https://discord.com/api/v8/users/@me",
                     headers={"Authorization": f"Bot {token}"})

    print(r.text)
    return r.status_code == 200
