import datetime

import disnake
from disnake.ext import commands
from inspect import currentframe

from disnake_bot.utils.parser import get_command_allow_roles, get_command_allow_channels
from disnake_bot.utils.decorators import allowed_channels
from disnake_bot.utils.warnings import add_warning, get_user_warnings, remove_warnings

from disnake_bot.modals.report_modals import ReportUserSelect
from disnake_bot.modals.embed_modals import EmbedModal
from disnake_bot.modals.feedback_modals import FeedbackTypeSelect

from disnake_bot.utils.messages import send_message, get_description, COMMANDS, add_values, error, send_long_message

from disnake_bot.event_logging import log

users_warn_inputs = {}

TIMEOUT_VARIANTS = commands.option_enum({
    "60 секунд": 60,
    "5 минут": 60 * 5,
    "10 минут": 60 * 10,
    "1 час": 60 * 60,
    "1 день": 60 * 60 * 24,
    "1 неделя": 60 * 60 * 24 * 7,
})


async def autocomplete_user(inter: disnake.ApplicationCommandInteraction, user_input: str):
    global users_warn_inputs
    all_users = [user.name for user in inter.guild.members]
    users_warn_inputs[inter.user.id] = user_input
    print(users_warn_inputs)
    # print(inter.guild.members)
    # print(user_input, all_users)
    return [i for i in all_users if user_input.lower() in i.lower()]


async def autocomplete_user_warns(inter: disnake.ApplicationCommandInteraction, user_input: str):
    print(users_warn_inputs)
    print(users_warn_inputs[inter.user.id])
    warns = [f"{i}. {text[:10]}" for text, i in enumerate(get_user_warnings(users_warn_inputs[inter.user.id]))]
    print(warns)
    # print(inter.guild.members)
    # print(user_input, all_users)
    if not warns:
        warns.append("Вы ввели несуществующего пользователя")
    return warns


class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(name="ban", description=get_description("ban"))
    @commands.has_any_role(*get_command_allow_roles("ban"))
    @allowed_channels(*get_command_allow_channels("ban"))
    @commands.check(predicate=lambda inr: log(inr, "/ban", "commands"))
    async def ban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Забанить участника сервера

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        # logging_data(inter, "/ban", "commands", member.name, reason)
        # await member.ban(reason=reason)
        await send_message(inter, "ban", user=member, **{"reason": reason})

    @commands.slash_command(name="unban", description=get_description("unban"))
    @commands.has_any_role(*get_command_allow_roles("unban"))
    @allowed_channels(*get_command_allow_channels("unban"))
    @commands.check(predicate=lambda inr: log(inr, "/unban", "commands"))
    async def unban(self, inter: disnake.ApplicationCommandInteraction, member_id, reason: str = ""):
        """
        Разблокировать участника сервера

        Parameters
        ----------
        member_id: Id участник
        reason: Причина (необязательно)
        """
        try:
            int(member_id)
        except Exception:
            await error(inter, "unban_input_error")
            return

        try:
            member = await self.bot.fetch_user(member_id)
            await inter.guild.unban(user=member, reason=reason)
        except Exception:
            await error(inter, "unban_value_error", **{"argument": member_id})
            return

        await send_message(inter, "unban", user=member, **{"reason": reason})

    @commands.slash_command(name="mute", description=get_description("mute"))
    @commands.has_any_role(*get_command_allow_roles("mute"))
    @allowed_channels(*get_command_allow_channels("mute"))
    @commands.check(predicate=lambda inr: log(inr, "/mute", "commands"))
    async def mute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Выключить микрофон участнику

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """

        if member.voice:
            await member.edit(mute=True)

            await send_message(inter, "mute", user=member, **{"reason": reason})

        else:
            await error(inter, "mute_error", member)

    @commands.slash_command(name="unmute", description=get_description("unmute"))
    @commands.has_any_role(*get_command_allow_roles("unmute"))
    @allowed_channels(*get_command_allow_channels("unmute"))
    @commands.check(predicate=lambda inr: log(inr, "/unmute", "commands"))
    async def unmute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Включить микрофон участнику

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """

        if member.voice:
            await member.edit(mute=False)

            await send_message(inter, "unmute", user=member, **{"reason": reason})
        else:
            await error(inter, "unmute_error", member)

    @commands.slash_command(name="chatmute", description=get_description("chatmute"))
    @commands.has_any_role(*get_command_allow_roles("chatmute"))
    @allowed_channels(*get_command_allow_channels("chatmute"))
    @commands.check(predicate=lambda inr: log(inr, "/chatmute", "commands"))
    async def chatmute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Выключить пользователю возможность писать в чат

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        await send_long_message(inter, "chatmute")
        for channel in inter.guild.channels:
            permissions = channel.permissions_for(member)
            if permissions.send_messages:
                await channel.set_permissions(member, send_messages=False)

        await send_message(inter, "chatmute", user=member, **{"reason": reason, "edit_original_message": True})

    @commands.slash_command(name="chatunmute", description=get_description("chatunmute"))
    @commands.has_any_role(*get_command_allow_roles("chatunmute"))
    @allowed_channels(*get_command_allow_channels("chatunmute"))
    @commands.check(predicate=lambda inr: log(inr, "/chatunmute", "commands"))
    async def chatunmute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Включить пользователю возможность писать в чат

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        await send_long_message(inter, "chatunmute")
        # await inter.response.defer()
        for channel in inter.guild.text_channels:
            permissions = channel.permissions_for(member)
            if not permissions.send_messages:
                await channel.set_permissions(member, send_messages=True)

        await send_message(inter, "chatunmute", user=member, **{"reason": reason, "edit_original_message": True})

    @commands.slash_command(name="timeout", description=get_description("timeout"))
    @commands.has_any_role(*get_command_allow_roles("timeout"))
    @allowed_channels(*get_command_allow_channels("timeout"))
    @commands.check(predicate=lambda inr: log(inr, "/timeout", "commands"))
    async def timeout(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member,
                      minutes: TIMEOUT_VARIANTS,
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
        duration = datetime.timedelta(seconds=minutes).seconds

        await member.timeout(duration=duration, reason=reason)

        await send_message(inter, "timeout", user=member, **{"reason": reason, "argument": minutes})

    @commands.slash_command(name="rmtimeout", description=get_description("rmtimeout"))
    @commands.has_any_role(*get_command_allow_roles("rmtimeout"))
    @allowed_channels(*get_command_allow_channels("rmtimeout"))
    @commands.check(predicate=lambda inr: log(inr, "/rmtimeout", "commands"))
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

        await send_message(inter, "rmtimeout", user=member, **{"reason": reason})

    @commands.slash_command(name="fullban", description=get_description("fullban"))
    @commands.has_any_role(*get_command_allow_roles("fullban"))
    @allowed_channels(*get_command_allow_channels("fullban"))
    @commands.check(predicate=lambda inr: log(inr, "/fullban", "commands"))
    async def fullban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str):
        """
        Заблокировать пользователя и удалить все его сообщения

        Parameters
        ----------
        member: Участник
        reason: причина
        """
        # await inter.response.defer()
        # await member.ban(reason=reason)
        # for channel in inter.guild.text_channels:
        #     await channel.purge(limit=None, check=lambda msg: msg.author == member)

        await send_message(inter, "fullban", user=member, **{"reason": reason})

    @commands.slash_command(name="clear", description=get_description("clear"))
    @commands.has_any_role(*get_command_allow_roles("clear"))
    @allowed_channels(*get_command_allow_channels("clear"))
    @commands.check(predicate=lambda inr: log(inr, "/clear", "commands"))
    async def clear(self, inter: disnake.ApplicationCommandInteraction, count: commands.Range[1, ...]):
        """
        Удалить сообщения

        Parameters
        ----------
        count: количество
        """

        await send_message(inter, "clear", user="", **{"argument": count})
        await inter.channel.purge(limit=count + 1)

    @commands.slash_command(name="afk", description=get_description("afk"))
    @commands.has_any_role(*get_command_allow_roles("afk"))
    @allowed_channels(*get_command_allow_channels("afk"))
    @commands.check(predicate=lambda inr: log(inr, "/afk", "commands"))
    async def afk(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Переместить участника в AFK

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        if not member.voice:
            await error(inter, "afk_error", member)
            return

        if inter.guild.afk_channel.id != member.voice.channel.id:
            await member.move_to(inter.guild.afk_channel)
        else:
            await error(inter, "afk_already_error", member)
            return 0

        await send_message(inter, "afk", user=member, **{"reason": reason})

    @commands.slash_command(name="move", description=get_description("move"))
    @commands.has_any_role(*get_command_allow_roles("move"))
    @allowed_channels(*get_command_allow_channels("move"))
    @commands.check(predicate=lambda inr: log(inr, "/move", "commands"))
    async def move(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member,
                   channel: disnake.VoiceChannel, reason: str = ""):
        """
        Переместить участника в другой голосовой канал

        Parameters
        ----------
        member: Участник
        channel: Голосовой канал
        reason: Причина (необязательно)
        """
        if not member.voice:
            await error(inter, "move_error", member)
            return

        if member.voice.channel != channel:
            await member.move_to(channel)
        else:
            await error(inter, "move_new_channel_error", member)
            return 0

        await send_message(inter, "move", user=member, **{"reason": reason, "channel": channel})

    @commands.slash_command(name="deafen", description=get_description("deafen"))
    @commands.has_any_role(*get_command_allow_roles("deafen"))
    @allowed_channels(*get_command_allow_channels("deafen"))
    @commands.check(predicate=lambda inr: log(inr, "/deafen", "commands"))
    async def deafen(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Выключить звук пользователю

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """

        if member.voice:
            await member.edit(deafen=True)

            await send_message(inter, "deafen", user=member, **{"reason": reason})
        else:
            await error(inter, "deafen_error", member)

    @commands.slash_command(name="undeafen", description=get_description("undeafen"))
    @commands.has_any_role(*get_command_allow_roles("undeafen"))
    @allowed_channels(*get_command_allow_channels("undeafen"))
    @commands.check(predicate=lambda inr: log(inr, "/undeafen", "commands"))
    async def undeafen(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Включить звук участнику

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """

        if member.voice:
            await member.edit(deafen=False)

            await send_message(inter, "undeafen", user=member, **{"reason": reason})
        else:
            await error(inter, "undeafen_error", member)

    @commands.slash_command(name="addrole", description=get_description("addrole"))
    @commands.has_any_role(*get_command_allow_roles("addrole"))
    @allowed_channels(*get_command_allow_channels("addrole"))
    @commands.check(predicate=lambda inr: log(inr, "/addrole", "commands"))
    async def addrole(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, role: disnake.Role,
                      reason: str = ""):
        """
        Выдать участнику роль

        Parameters
        ----------
        member: Участник
        role: Роль
        reason: Причина (необязательно)
        """
        if role in member.roles:
            await error(inter, "addrole_error", member)
            return
        await member.add_roles(role)
        await send_message(inter, "addrole", user=member, **{"reason": reason, "role": role})

    @commands.slash_command(name="rmrole", description=get_description("rmrole"))
    @commands.has_any_role(*get_command_allow_roles("rmrole"))
    @allowed_channels(*get_command_allow_channels("rmrole"))
    @commands.check(predicate=lambda inr: log(inr, "/rmrole", "commands"))
    async def rmrole(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, role: disnake.Role,
                     reason: str = ""):
        """
        Удалить роль у пользователя

        Parameters
        ----------
        member: Участник
        role: Роль
        reason: Причина (необязательно)
        """

        if not (role in member.roles):
            await error(inter, "rmrole_error", member)
            return
        await member.remove_roles(role)
        await send_message(inter, "rmrole", user=member, **{"reason": reason, "role": role})

    @commands.slash_command(name="ping", description=get_description("ping"))
    @commands.has_any_role(*get_command_allow_roles("ping"))
    @allowed_channels(*get_command_allow_channels("ping"))
    @commands.check(predicate=lambda inr: log(inr, "/ping", "commands"))
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """
        Получить пинг бота

        Parameters
        ----------

        """
        await send_message(inter, "ping", user="", **{"ping": self.bot.latency})
        # await inter.response.send_message(" {}".format())

    @commands.slash_command(name="slowmode", description=get_description("slowmode"))
    @commands.has_any_role(*get_command_allow_roles("slowmode"))
    @allowed_channels(*get_command_allow_channels("slowmode"))
    @commands.check(predicate=lambda inr: log(inr, "/slowmode", "commands"))
    async def slowmode(self, inter: disnake.ApplicationCommandInteraction, delay: commands.Range[0, 21600],
                       reason: str = ""):
        """
        Установить медленный режим

        Parameters
        ----------
        delay: задержка в секундах (0 для выключения)
        reason: Причина (необязательно)
        """
        await inter.channel.edit(slowmode_delay=delay)
        await send_message(inter, "slowmode", user="", **{"reason": reason, "argument": delay})

    @commands.slash_command(name="vkick", description=get_description("vkick"))
    @commands.has_any_role(*get_command_allow_roles("vkick"))
    @allowed_channels(*get_command_allow_channels("vkick"))
    @commands.check(predicate=lambda inr: log(inr, "/vkick", "commands"))
    async def vkick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Отключить участника от голосового канала

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        # await inter.guild.edit(slowmode_delay=delay)
        if member.voice:
            await member.edit(voice_channel=None)
            await send_message(inter, "vkick", user=member, **{"reason": reason})

        else:
            await error(inter, "vkick_error", member)

    @commands.slash_command(name="warn", description=get_description("warn"))
    @commands.has_any_role(*get_command_allow_roles("warn"))
    @allowed_channels(*get_command_allow_channels("warn"))
    @commands.check(predicate=lambda inr: log(inr, "/warn", "commands"))
    async def warn(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str):
        """
        Выдать предупреждение участнику

        Parameters
        ----------
        member: Участник
        reason: Причина
        """
        add_warning(member.name, inter.user.name, reason)

        await send_message(inter, "warn", user=member, **{"reason": reason})

    @commands.slash_command(name="warns", description=get_description("warns"))
    @commands.has_any_role(*get_command_allow_roles("warns"))
    @allowed_channels(*get_command_allow_channels("warns"))
    @commands.check(predicate=lambda inr: log(inr, "/warns", "commands"))
    async def warns(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Список предупреждений участника

        Parameters
        ----------
        member: Участник
        """
        warnings = get_user_warnings(member.name)
        embed_body = "\n".join([f"{w['id'] + 1}. {w['reason']} от {w['from']} ({w['time']})" for w in warnings])
        if not embed_body:
            embed_body = "У пользователя {} ещё нет предупреждений".format(member.name)

        await send_message(inter, "warns", user=member, **{"result": embed_body})

    @commands.slash_command(name="rmwarn", description=get_description("rmwarn"))
    @commands.has_any_role(*get_command_allow_roles("rmwarn"))
    @allowed_channels(*get_command_allow_channels("rmwarn"))
    @commands.check(predicate=lambda inr: log(inr, "/rmwarn", "commands"))
    async def rmwarn(self, inter: disnake.ApplicationCommandInteraction,
                     member: disnake.Member,
                     index: int, reason: str = ""):
        """
        Удалить предупреждение у участника

        Parameters
        ----------
        member: Участник
        index: Номер предупреждения или 0, чтобы удалить все
        reason: Причина (необязательно)
        """
        answer = remove_warnings(member.name, index)
        await send_message(inter, "rmwarn", user=member, **{"reason": reason, "argument": index})

    @commands.slash_command(name="report", description=get_description("report"))
    @commands.has_any_role(*get_command_allow_roles("report"))
    @allowed_channels(*get_command_allow_channels("report"))
    @commands.check(predicate=lambda inr: log(inr, "/report", "commands"))
    async def report(self, inter: disnake.ApplicationCommandInteraction):
        """
        Пожаловаться на участника

        Parameters
        ----------
        member: Участник, на которого вы хотите подать жалобу
        text: Детали жалобы
        """
        # if not member:
        view = disnake.ui.View()
        view.add_item(ReportUserSelect(inter))
        # Тут можно добавть эмбед с описанием ролей
        await inter.response.send_message(
            add_values(inter, COMMANDS["report"]["select_message"])
            , view=view,
            ephemeral=True)
        # else:
        #     await inter.response.send_modal(ReportModal(f"{member.name};{member.mention}", text))

    @commands.slash_command(name="embed", description=get_description("embed"))
    @commands.has_any_role(*get_command_allow_roles("embed"))
    @allowed_channels(*get_command_allow_channels("embed"))
    @commands.check(predicate=lambda inr: log(inr, "/embed", "commands"))
    async def embed(self, inter: disnake.ApplicationCommandInteraction):
        """
        Создать embed

        Parameters
        ----------
        """
        await inter.response.send_modal(modal=EmbedModal())

    @commands.slash_command(name="feedback", description=get_description("feedback"))
    @commands.has_any_role(*get_command_allow_roles("feedback"))
    @allowed_channels(*get_command_allow_channels("feedback"))
    @commands.check(predicate=lambda inr: log(inr, "/feedback", "commands"))
    async def feedback(self, inter: disnake.ApplicationCommandInteraction):
        """
        Обратиться к разработчику бота

        Parameters
        ----------
        """
        view = disnake.ui.View()
        view.add_item(FeedbackTypeSelect(self.bot))
        await inter.response.send_message(view=view,
                                          ephemeral=True)
