from disnake import Embed
import datetime

from disnake_bot.config import MODERATION_COMMANDS


def message(title, description, color):
    embed = Embed(
        title=title,
        description=description,
        color=color
    )
    return embed


class EmbedMessages:
    def __init__(self):
        self.embed = Embed()

    async def send_embed(self, inter, title, body, color, footer="Время выполнения команды: {}"):
        self.embed.title = title
        self.embed.description = body
        self.embed.color = int(color, 16)
        self.embed.set_footer(text=footer.format(datetime.datetime.now()))
        await inter.response.send_message(embed=self.embed)

    # async def success(self, inter, title, description, color=0x24FF00):
    #     await inter.response.send_message(embed=message(title, description, color))


class ErrorMessages:
    def __init__(self):
        self.embed = Embed()

    async def missing_role(self, inter):
        self.embed.title = MESSAGES_CONFIG["errors"]["missing_role"]["title"]
        self.embed.description = MESSAGES_CONFIG["errors"]["missing_role"]["body"]
        self.embed.color = int(MESSAGES_CONFIG["errors"]["missing_role"]["color"], 16)
        # embed = message(
        #     title="ошибка :(",
        #     description="У вас нет прав, для использования данной команды",
        #     color=0xFF0000
        # )
        await inter.response.send_message(embed=self.embed)

    async def command_not_found(self, inter):
        self.embed.title = MESSAGES_CONFIG["errors"]["command_not_found"]["title"]
        self.embed.description = MESSAGES_CONFIG["errors"]["command_not_found"]["body"]
        self.embed.color = int(MESSAGES_CONFIG["errors"]["command_not_found"]["color"], 16)
        # embed = message(
        #     title="ошибка :(",
        #     description="У вас нет прав, для использования данной команды",
        #     color=0xFF0000
        # )
        await inter.response.send_message(embed=self.embed)
