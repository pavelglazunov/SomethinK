import datetime

import disnake
from disnake.ext import commands
from disnake_bot.config import MODERATION_COMMANDS, EVERYONE_COMMANDS

from disnake_bot.utils.parse_commands import get_command_allow_roles, get_command_allow_channels
from disnake_bot.utils.decorators import allowed_channels

from enum import Enum

from disnake_bot import _message, _errors


class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(name="ban", description="Забанить участника")
    @commands.has_any_role(*get_command_allow_roles("ban"))
    @allowed_channels(*get_command_allow_channels("ban"))
    async def ban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Забанить участника сервера

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        # await member.ban(reason=reason)
        await _message.send_embed(inter=inter,
                                  title="Ban",
                                  body="Участник {} был заблокирован модератором {} по причине: {}".format(member.name,
                                                                                                           inter.user.name,
                                                                                                           reason),
                                  color="FF0000")

    @commands.slash_command(name="unban", description="Разблокировать участника")
    @commands.has_any_role(*get_command_allow_roles("unban"))
    @allowed_channels(*get_command_allow_channels("unban"))
    async def unban(self, inter: disnake.ApplicationCommandInteraction, member_id, reason: str = ""):
        """
        Разблокировать участника сервера

        Parameters
        ----------
        member_id: Id участник
        reason: Причина (необязательно)
        """

        try:
            member = await self.bot.fetch_user(member_id)
            await inter.guild.unban(user=member, reason=reason)
        except disnake.NotFound:
            await inter.response.send_message(f'Пользователь с ID {member_id} не забанен на сервере', delete_after=10)
            return

        await _message.send_embed(inter=inter,
                                  title="Unban",
                                  body="Участник {} был разблокирован модератором {} по причине: {}".format(member.name,
                                                                                                            inter.user.name,
                                                                                                            reason),
                                  color="00FF00")

    @commands.slash_command(name="mute", description="Выключить микрофон участнику")
    @commands.has_any_role(*get_command_allow_roles("mute"))
    @allowed_channels(*get_command_allow_channels("mute"))
    async def mute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Выключить микрофон участнику

        Parameters
        ----------
        member: Участник
        """

        if member.voice:
            await member.edit(mute=True)

            await _message.send_embed(inter=inter,
                                      title="Mute",
                                      body="Участник {} выключил микрофон пользователю {}".format(inter.user.name,
                                                                                                  member.name),
                                      color="f2433d")
        else:
            await inter.response.send_message("Участник {} не находиться в голосов канале".format(member.name))

    @commands.slash_command(name="unmute", description="Включить микрофон участнику")
    @commands.has_any_role(*get_command_allow_roles("unmute"))
    @allowed_channels(*get_command_allow_channels("unmute"))
    async def unmute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Включить микрофон участнику

        Parameters
        ----------
        member: Участник
        """

        if member.voice:
            await member.edit(mute=False)

            await _message.send_embed(inter=inter,
                                      title="Unmute",
                                      body="Участник {} включил микрофон пользователю {}".format(inter.user.name,
                                                                                                 member.name),
                                      color="85f23d")
        else:
            await inter.response.send_message("Участник {} не находиться в голосов канале".format(member.name))

    @commands.slash_command(name="chatmute", description="выключить пользователю возможность писать в чат")
    @commands.has_any_role(*get_command_allow_roles("chatmute"))
    @allowed_channels(*get_command_allow_channels("chatmute"))
    async def chatmute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Выключить пользователю возможность писать в чат

        Parameters
        ----------
        member: Участник
        """

        for channel in inter.guild.channels:
            permissions = channel.permissions_for(member)
            if permissions.send_messages:
                await channel.set_permissions(member, send_messages=False)

        await _message.send_embed(inter=inter,
                                  title="chat mute",
                                  body="Участник {} запретил пользователю {} писать в чат".format(inter.user.name,
                                                                                                  member.name),
                                  color="FF0000")

    @commands.slash_command(name="chatunmute", description="включить пользователю возможность писать в чат")
    @commands.has_any_role(*get_command_allow_roles("chatunmute"))
    @allowed_channels(*get_command_allow_channels("chatunmute"))
    async def chatunmute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Включить пользователю возможность писать в чат

        Parameters
        ----------
        member: Участник
        """

        # await inter.response.defer()
        for channel in inter.guild.text_channels:
            permissions = channel.permissions_for(member)
            if not permissions.send_messages:
                await channel.set_permissions(member, send_messages=True)

        await _message.send_embed(inter=inter,
                                  title="chat unmute",
                                  body="Участник {} разрешил пользователю {} писать в чат".format(inter.user.name,
                                                                                                  member.name),
                                  color="00FF00")

    @commands.slash_command(name="timeout", description="выдать пользователю тайм-аут")
    @commands.has_any_role(*get_command_allow_roles("timeout"))
    @allowed_channels(*get_command_allow_channels("timeout"))
    async def timeout(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, minutes: int,
                      reason: str = ""):
        """
        Выдать пользователю тайм-аут

        Parameters
        ----------
        member: Участник
        minutes: длительность тайм-аута в минутах
        reason: причина (необязательно)
        """

        # await inter.response.defer()
        duration = datetime.timedelta(minutes=minutes)

        await member.timeout(duration=duration, reason=reason)

        await _message.send_embed(inter=inter,
                                  title="chat mute",
                                  body="Участник {} выдал тайм-аут участнику {} по причине: {}".format(inter.user.name,
                                                                                                       member.name,
                                                                                                       reason),
                                  color="FF0000")

    @commands.slash_command(name="rmtimeout", description="удалить тайм-аут у пользователя")
    @commands.has_any_role(*get_command_allow_roles("rmtimeout"))
    @allowed_channels(*get_command_allow_channels("rmtimeout"))
    async def rmtimeout(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Удалить тайм-аут у пользователя

        Parameters
        ----------
        member: Участник
        reason: причина (необязательно)
        """

        duration = datetime.timedelta(minutes=0)

        await member.timeout(duration=duration, reason=reason)

        await _message.send_embed(inter=inter,
                                  title="timeout",
                                  body="Участник {} удалил тайм-аут у участника {} по причине: {}".format(
                                      inter.user.name,
                                      member.name,
                                      reason),
                                  color="00FF00")

    @commands.slash_command(name="fullban", description="Заблокировать пользователя и удалить все его сообщения")
    @commands.has_any_role(*get_command_allow_roles("fullban"))
    @allowed_channels(*get_command_allow_channels("fullban"))
    async def fullban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Заблокировать пользователя и удалить все его сообщения

        Parameters
        ----------
        member: Участник
        reason: причина (необязательно)
        """
        # await inter.response.defer()
        await member.ban(reason=reason)
        for channel in inter.guild.text_channels:
            await channel.purge(limit=None, check=lambda msg: msg.author == member)

        await _message.send_embed(inter=inter,
                                  title="full ban",
                                  body="Участник {} заблокировал участника {} и удалил все его сообщения по причине: {}".format(
                                      inter.user.name,
                                      member.name,
                                      reason),
                                  color="000000")

    @commands.slash_command(name="clear", description="Удалить сообщения")
    @commands.has_any_role(*get_command_allow_roles("clear"))
    @allowed_channels(*get_command_allow_channels("clear"))
    async def clear(self, inter: disnake.ApplicationCommandInteraction, count: int):
        """
        Удалить сообщения

        Parameters
        ----------
        count: количество
        """
        await inter.response.send_message("Удалено {} сообщений".format(count))
        await inter.channel.purge(limit=count + 1)

    @commands.slash_command(name="afk", description="Переместить участника в AFK")
    @commands.has_any_role(*get_command_allow_roles("afk"))
    @allowed_channels(*get_command_allow_channels("afk"))
    async def afk(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Переместить участника в AFK

        Parameters
        ----------
        member: Участник
        """

        if inter.guild.afk_channel.id != member.voice.channel.id:
            await member.move_to(inter.guild.afk_channel)
        else:
            await inter.response.send_message("Пользователь уже в AFK канале")
            return 0

        await _message.send_embed(inter=inter,
                                  title="afk",
                                  body="Участник {} перемещает участника {} в AFK".format(
                                      inter.user.name,
                                      member.name),
                                  color="FD0000")

    @commands.slash_command(name="move", description="Переместить участника в другой голосовой канал")
    @commands.has_any_role(*get_command_allow_roles("move"))
    @allowed_channels(*get_command_allow_channels("move"))
    async def move(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member,
                   channel: disnake.VoiceChannel):
        """
        Переместить участника в другой голосовой канал

        Parameters
        ----------
        member: Участник
        channel: Голосовой канал
        """

        if member.voice.channel != channel:
            await member.move_to(channel)
        else:
            await inter.response.send_message("Пользователь уже в этом канале")
            return 0

        await _message.send_embed(inter=inter,
                                  title="move",
                                  body="Участник {} перемещает участника {} в {}".format(
                                      inter.user.name,
                                      member.name,
                                      channel),
                                  color="00FF00")

    @commands.slash_command(name="deafen", description="Выключить звук пользователю")
    @commands.has_any_role(*get_command_allow_roles("deafen"))
    @allowed_channels(*get_command_allow_channels("deafen"))
    async def deafen(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Выключить звук пользователю

        Parameters
        ----------
        member: Участник
        """

        if member.voice:
            await member.edit(deafen=True)

            await _message.send_embed(inter=inter,
                                      title="Deafen",
                                      body="Участник {} выключил звук пользователю {}".format(inter.user.name,
                                                                                              member.name),
                                      color="f2433d")
        else:
            await inter.response.send_message("Участник {} не находиться в голосов канале".format(member.name))

    @commands.slash_command(name="undeafen", description="Включить звук участнику")
    @commands.has_any_role(*get_command_allow_roles("undeafen"))
    @allowed_channels(*get_command_allow_channels("undeafen"))
    async def undeafen(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Включить звук участнику

        Parameters
        ----------
        member: Участник
        """

        if member.voice:
            await member.edit(deafen=False)

            await _message.send_embed(inter=inter,
                                      title="undeafen",
                                      body="Участник {} включил звук пользователю {}".format(inter.user.name,
                                                                                             member.name),
                                      color="85f23d")
        else:
            await inter.response.send_message("Участник {} не находиться в голосов канале".format(member.name))

    @commands.slash_command(name="addrole", description="Выдать участнику роль")
    @commands.has_any_role(*get_command_allow_roles("addrole"))
    @allowed_channels(*get_command_allow_channels("addrole"))
    async def addrole(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, role: disnake.Role):
        """
        Выдать участнику роль

        Parameters
        ----------
        member: Участник
        role: Роль
        """
        if role in member.roles:
            await inter.response.send_message("У пользователя {} уже есть роль {}".format(member.name, role.name))
            return
        await member.add_roles(role)
        await _message.send_embed(inter=inter,
                                  title="add role",
                                  body="Участник {} выдал пользователю {} роль\"{}\"".format(inter.user.name,
                                                                                             member.name,
                                                                                             role),
                                  color="00FF00")

    @commands.slash_command(name="rmrole", description="Удалить роль у пользователя")
    @commands.has_any_role(*get_command_allow_roles("rmrole"))
    @allowed_channels(*get_command_allow_channels("rmrole"))
    async def rmrole(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, role: disnake.Role):
        """
        Удалить роль у пользователя

        Parameters
        ----------
        member: Участник
        role: Роль
        """
        if not (role in member.roles):
            await inter.response.send_message("У пользователя {} ещё нет роли {}".format(member.name, role.name))
            return
        await member.remove_roles(role)
        await _message.send_embed(inter=inter,
                                  title="remove role",
                                  body="Участник {} забрал роль {} у пользователя {}".format(inter.user.name,
                                                                                             role,
                                                                                             member.name
                                                                                             ),
                                  color="FF0000")

    @commands.slash_command(name="ping", description="Получить пинг бота")
    @commands.has_any_role(*get_command_allow_roles("ping"))
    @allowed_channels(*get_command_allow_channels("ping"))
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """
        Получить пинг бота

        Parameters
        ----------

        """

        await inter.response.send_message("Понг. Пинг бота: {}".format(self.bot.latency))

    @commands.slash_command(name="slowmode", description="Установить медленный режим")
    @commands.has_any_role(*get_command_allow_roles("slowmode"))
    @allowed_channels(*get_command_allow_channels("slowmode"))
    async def slowmode(self, inter: disnake.ApplicationCommandInteraction, delay: int):
        """
        Установить медленный режим

        Parameters
        ----------
        delay: задержка в секундах (0 для выключения)
        """
        # await inter.guild.edit(slowmode_delay=delay)
        await inter.channel.edit(slowmode_delay=delay)
        await inter.response.send_message("Медленный режим включен, задержка между сообщениями: {}".format(delay))

    @commands.slash_command(name="vkick", description="Отключить участника от голосового канала")
    @commands.has_any_role(*get_command_allow_roles("vkick"))
    @allowed_channels(*get_command_allow_channels("vkick"))
    async def vkick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Отключить участника от голосового канала

        Parameters
        ----------
        member: Участник
        """
        # await inter.guild.edit(slowmode_delay=delay)
        if member.voice:
            await member.edit(voice_channel=None)
            await _message.send_embed(inter=inter,
                                      title="voice kick",
                                      body="Участник {} отключает пользователя {} от голосового канала".format(
                                          inter.user.name,
                                          member.name
                                          ),
                                      color="FF0000")

        else:
            await inter.send('Участник не находится в голосовом канале')
