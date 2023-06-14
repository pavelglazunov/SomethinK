import disnake
from disnake.ext import commands
from disnake_bot.config import MESSAGES_CONFIG, MODERATION_COMMANDS, MODERATION_ROLES_ID, EVERYONE_COMMANDS

from enum import Enum

from disnake_bot import _message, _errors


class Animal(str, Enum):
    Dog = 'dog'
    Cat = 'cat'
    Penguin = 'peng'


class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(name="ban", description="Забанить участника")
    @commands.has_any_role(*MODERATION_ROLES_ID)
    async def ban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Забанить участника сервера

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        await member.ban(reason=reason)
        await _message.send_embed(inter=inter,
                                  title=MESSAGES_CONFIG["commands"]["ban"]["title"],
                                  body=MESSAGES_CONFIG["commands"]["ban"]["body"].format(member.name, reason),
                                  color=MESSAGES_CONFIG["commands"]["ban"]["color"])

    @commands.slash_command(name="unban", description="Разблокировать участника")
    @commands.has_any_role(*MODERATION_ROLES_ID)
    async def unban(self, inter: disnake.ApplicationCommandInteraction, member, reason: str = ""):
        """
        Разблокировать участника сервера

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """

        print(member)
        bans_user = await inter.guild.fetch_ban(disnake.Object(int(member[3:-2])))

        print(bans_user.user)
        # for i in bans_user:
        #     print(i)
        # try:
        #     # banned_user = await inter.guild.fetch_ban(disnake.Object(member))
        # except disnake.NotFound:
        #     await inter.response.send_message(f'Пользователь с ID {member} не забанен на сервере', delete_after=10)
        #     return
        for guild in self.bot.guilds:
            print(guild.name)
        # await member.unban(reason=reason)
        # await _message.send_embed(inter=inter,
        #                           title=MESSAGES_CONFIG["commands"]["unban"]["title"],
        #                           body=MESSAGES_CONFIG["commands"]["unban"]["body"].format(member.name, reason),
        #                           color=MESSAGES_CONFIG["commands"]["unban"]["color"])
