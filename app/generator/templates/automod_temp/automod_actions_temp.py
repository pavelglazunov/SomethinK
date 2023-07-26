AUTOMOD_ACTIONS_BASE_IMPORTS = """
import datetime
import disnake
from disnake import Message
from _____project_name_for_imports_____.utils.decorators import edit_json

 """
AUTOMOD_ACTIONS_WARNING_IMPORT = """
from _____project_name_for_imports_____.utils.warnings import add_warning

 """
AUTOMOD_ACTIONS_PENDING_MESSAGES_IMPORT = """
from _____project_name_for_imports_____.config import PENDING_MESSAGES_JSON_FILENAME
from _____project_name_for_imports_____.utils.parser import parse_config


 """
AUTOMOD_ACTIONS_SEND_TO_COMMAND = """
@edit_json(PENDING_MESSAGES_JSON_FILENAME)
def add_pending_message(message_data, data):
    data.append(message_data)


@edit_json(PENDING_MESSAGES_JSON_FILENAME)
def remove_pending_message(message_id, data: list):
    for i in data:
        if i["message_id"] == int(message_id):
            res = i.copy()
            data.remove(i)
            return res

async def send_to_moderation(message: Message, *_):
    message_content = message.content
    message_author = message.author
    message_channel = message.channel
    message_id = message.id
    message_time = datetime.datetime.now().time()

    add_pending_message({
        "message_id": message_id,
        "from_user_id": message_author.id,
        "from_user_mention": message_author.mention,
        "message_channel_id": message_channel.id,
        "message_channel_name": message_channel.name,
        "message_channel_mention": message_channel.mention,
        "message_content": message_content,
        "message_send_time": str(message_time)
    })

    pending_message_channel = message.guild.get_channel(parse_config("channels_ID.pending_message_channel_id"))
    embed = disnake.Embed(title="Новое сообщение для проверки")
    embed.add_field(name="Текст сообщения", value=message_content, inline=False)
    embed.add_field(name="Информация", value=f"ID сообщения: {message_id}\\n"
                                             f"Сообщение получено от: {message_author.mention}\\n"
                                             f"Сообщение получено в канале: {message_channel.mention}\\n"
                                             f"Сообщение получено в: {message_time}", inline=False)
    await pending_message_channel.send(
        embed=embed,
        components=[
            disnake.ui.Button(label="Одобрить", style=disnake.ButtonStyle.success, custom_id=f"a_{message_id}"),
            disnake.ui.Button(label="Удалить", style=disnake.ButtonStyle.danger, custom_id=f"r_{message_id}"),
        ]
    )
    await message.reply("Автомодерация нашла что-то подозрительное, сообщение было отправлено на проверку")
    await message.delete()
    

 """
AUTOMOD_ACTIONS_REMOVE = """
async def remove(message: Message, *_):
    await message.delete()


 """
AUTOMOD_ACTIONS_WARN = """
async def warn(message: Message, reason: str, word):
    add_warning(message.author.name, "Автомодерация", reason)
    await message.reply(
        "Пользователь {} получает предупреждение за чрезмерное использование {}".format(message.author.name, word))


 """
AUTOMOD_ACTIONS_REMOVE_AND_WARN = """
async def remove_and_warn(message: Message, reason: str, word):
    add_warning(message.author.name, "Автомодерация", reason)
    await message.reply(
        "Пользователь {} получает предупреждение за чрезмерное использование {}".format(message.author.name, word))
    await message.delete()


 """
AUTOMOD_ACTIONS_ACTIONS_LIST = """
ACTIONS = {
     """
AUTOMOD_ACTIONS_REMOVE_FUNC_CALL = """
    "--remove": remove,
     """
AUTOMOD_ACTIONS_WARN_FUNC_CALL = """
    "--warn": warn,
     """
AUTOMOD_ACTIONS_REMOVE_AND_WARN_FUNC_CALL = """
    "--remove-warn": remove_and_warn,
     """
AUTOMOD_ACTIONS_SEND_FUNC_CALL = """
    "--send": send_to_moderation
}
"""
