import datetime

import disnake
from disnake import ApplicationCommandInteraction as AppInter
from disnake_bot.utils.parser import load_messages

MESSAGES = load_messages()
COMMANDS = MESSAGES["commands"]
ERRORS = MESSAGES["errors"]


def get_description(command):
    return COMMANDS[command]["description"]


def add_values(inter: AppInter, msg: str, user: disnake.Member = "", **kwargs):
    print("msg:", msg)

    if user != "":
        msg = msg.replace("{user_name}", user.name)
        msg = msg.replace("{user_mention}", user.mention)
        msg = msg.replace("{server_name}", user.guild.name)

    if inter:
        msg = msg.replace("{author_name}", inter.user.name)
        msg = msg.replace("{author_mention}", inter.user.mention)
        msg = msg.replace("{server_name}", inter.guild.name)

    msg = msg.replace("{reason}", kwargs.get("reason", ""))
    msg = msg.replace("{argument}", str(kwargs.get("argument", "")))
    msg = msg.replace("{result}", str(kwargs.get("result", "")))
    msg = msg.replace("{ping}", str(kwargs.get("ping", "")))
    msg = msg.replace("{from_language}", str(kwargs.get("from_language", "")))
    msg = msg.replace("{to_language}", str(kwargs.get("to_language", "")))
    msg = msg.replace("{text}", str(kwargs.get("text", "")))
    # msg = msg.replace("{warn_index}", str(kwargs.get("warn_index", "")))
    # msg = msg.replace("{new_name}", str(kwargs.get("new_name", "")))

    msg = msg.replace("{datetime}", str(datetime.datetime.now()))
    msg = msg.replace("{date}", str(datetime.datetime.now().date()))
    msg = msg.replace("{time}", str(datetime.datetime.now().time()))

    if kwargs.get("channel"):
        msg = msg.replace("{channel_name}", kwargs.get("channel").name)
        msg = msg.replace("{channel_mention}", kwargs.get("channel").mention)
    if kwargs.get("role"):
        msg = msg.replace("{role_name}", kwargs.get("role").name)
        msg = msg.replace("{role_mention}", kwargs.get("role").mention)

    return msg


async def send_long_message(inter: AppInter, command):
    command_data = COMMANDS.get(command, {})
    await inter.response.send_message(command_data["waiting_message"])


async def send_message(inter: AppInter, command, user: disnake.Member or disnake.User = "", **kwargs):
    command_data = COMMANDS.get(command, {})
    message_content = add_values(inter, command_data.get("message_text"), user, **kwargs)
    if command_data.get("send_embed"):
        embed = disnake.Embed()
        embed.title = command_data.get("embed_title")
        embed.description = message_content
        embed.footer.text = add_values(inter, command_data.get("embed_footer"), user, **kwargs)
        embed.color = int(command_data.get("embed_color"), 16)

        if kwargs.get("edit_original_message"):
            await inter.edit_original_message(embed=embed, content="")
            return
        await inter.response.send_message(embed=embed)
    else:
        if kwargs.get("edit_original_message"):
            await inter.edit_original_message(content=message_content)
            return
        await inter.response.send_message(message_content)


async def send_event_message(channel, event_config: dict, member: disnake.Member):
    if event_config["enable_embed"]:
        embed = disnake.Embed()
        embed.title = add_values(inter="", msg=event_config["embed"]["header"], user=member)
        embed.description = add_values(inter="", msg=event_config["content"], user=member)
        embed.set_footer(text=add_values(inter="", msg=event_config["embed"]["footer_content"], user=member))
        embed.set_image(event_config["embed"]["image_url"])
        embed.color = int(event_config["embed"]["color"][1:], 16)

        await channel.send(embed=embed)
    else:
        await channel.send(add_values(inter="", msg=event_config["content"], user=member))


async def error(inter: AppInter, error_type, user="", **kwargs):
    error_data = ERRORS.get(error_type, {})
    message_content = add_values(inter, error_data.get("message_text"), user, **kwargs)
    if error_data.get("send_embed"):
        embed = disnake.Embed()
        embed.title = error_data.get("embed_title")
        embed.description = message_content
        embed.footer.text = add_values(inter, error_data.get("embed_footer"), user, **kwargs)
        embed.color = int(error_data.get("embed_color"), 16)

        await inter.response.send_message(embed=embed)
    else:
        await inter.response.send_message(message_content)
