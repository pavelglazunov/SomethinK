
import datetime
import disnake
from disnake.ext import commands
from utils.parser import get_command_allow_roles, get_command_allow_channels
from utils.decorators import allowed_channels, allowed_roles
from utils.messages import send_message, get_description, send_error_message, send_long_message,     detected_error

 
from utils.warnings import add_warning
 
from utils.warnings import get_user_warnings
 
from utils.warnings import remove_warnings


 
TIMEOUT_VARIANTS = commands.option_enum({
    "60 секунд": 60,
    "5 минут": 60 * 5,
    "10 минут": 60 * 10,
    "1 час": 60 * 60,
    "1 день": 60 * 60 * 24,
    "1 неделя": 60 * 60 * 24 * 7,
})


 
class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

     
    @commands.slash_command(name="ban", description=get_description("ban"))
    @allowed_roles(*get_command_allow_roles("ban"))
    @allowed_channels(*get_command_allow_channels("ban"))
    async def ban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Забанить участника сервера

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        await member.ban(reason=reason)
        await send_message(inter, "ban", user=member, **{"reason": reason})

     
    @commands.slash_command(name="kick", description=get_description("kick"))
    @allowed_roles(*get_command_allow_roles("kick"))
    @allowed_channels(*get_command_allow_channels("kick"))
    async def kick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Забанить участника сервера

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        await member.kick(reason=reason)
        await send_message(inter, "kick", user=member, **{"reason": reason})

     
    @commands.slash_command(name="unban", description=get_description("unban"))
    @allowed_roles(*get_command_allow_roles("unban"))
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
            int(member_id)
        except Exception:
            await send_error_message(inter, "unban_input_error")
            return

        try:
            member = await self.bot.fetch_user(member_id)
            await inter.guild.unban(user=member, reason=reason)
        except Exception:
            await send_error_message(inter, "unban_value_error", **{"argument": member_id})
            return

        await send_message(inter, "unban", user=member, **{"reason": reason})

     
    @commands.slash_command(name="mute", description=get_description("mute"))
    @allowed_roles(*get_command_allow_roles("mute"))
    @allowed_channels(*get_command_allow_channels("mute"))
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
            await send_error_message(inter, "mute_error", member)

     
    @commands.slash_command(name="unmute", description=get_description("unmute"))
    @allowed_roles(*get_command_allow_roles("unmute"))
    @allowed_channels(*get_command_allow_channels("unmute"))
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
            await send_error_message(inter, "unmute_error", member)

     
    @commands.slash_command(name="chatmute", description=get_description("chatmute"))
    @allowed_roles(*get_command_allow_roles("chatmute"))
    @allowed_channels(*get_command_allow_channels("chatmute"))
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
    @allowed_roles(*get_command_allow_roles("chatunmute"))
    @allowed_channels(*get_command_allow_channels("chatunmute"))
    async def chatunmute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Включить пользователю возможность писать в чат

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        await send_long_message(inter, "chatunmute")

        for channel in inter.guild.text_channels:
            permissions = channel.permissions_for(member)
            if not permissions.send_messages:
                await channel.set_permissions(member, send_messages=True)

        await send_message(inter, "chatunmute", user=member, **{"reason": reason, "edit_original_message": True})

     
    @commands.slash_command(name="timeout", description=get_description("timeout"))
    @allowed_roles(*get_command_allow_roles("timeout"))
    @allowed_channels(*get_command_allow_channels("timeout"))
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

        duration = datetime.timedelta(seconds=minutes).seconds

        await member.timeout(duration=duration, reason=reason)

        await send_message(inter, "timeout", user=member, **{"reason": reason, "argument": minutes})

     
    @commands.slash_command(name="rmtimeout", description=get_description("rmtimeout"))
    @allowed_roles(*get_command_allow_roles("rmtimeout"))
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

        await send_message(inter, "rmtimeout", user=member, **{"reason": reason})

     

    @commands.slash_command(name="fullban", description=get_description("fullban"))
    @allowed_roles(*get_command_allow_roles("fullban"))
    @allowed_channels(*get_command_allow_channels("fullban"))
    async def fullban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str):
        """
        Заблокировать пользователя и удалить все его сообщения

        Parameters
        ----------
        member: Участник
        reason: причина
        """
        await send_long_message(inter, "fullban")
        await inter.response.defer()
        await member.ban(reason=reason)
        for channel in inter.guild.text_channels:
            await channel.purge(limit=None, check=lambda msg: msg.author == member)

        await send_message(inter, "fullban", user=member, **{"reason": reason, "edit_original_message": True})

     

    @commands.slash_command(name="clear", description=get_description("clear"))
    @allowed_roles(*get_command_allow_roles("clear"))
    @allowed_channels(*get_command_allow_channels("clear"))
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
    @allowed_roles(*get_command_allow_roles("afk"))
    @allowed_channels(*get_command_allow_channels("afk"))
    async def afk(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Переместить участника в AFK

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        if not member.voice:
            await send_error_message(inter, "afk_error", member)
            return

        if inter.guild.afk_channel.id != member.voice.channel.id:
            await member.move_to(inter.guild.afk_channel)
        else:
            await send_error_message(inter, "afk_already_error", member)
            return

        await send_message(inter, "afk", user=member, **{"reason": reason})

     

    @commands.slash_command(name="move", description=get_description("move"))
    @allowed_roles(*get_command_allow_roles("move"))
    @allowed_channels(*get_command_allow_channels("move"))
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
            await send_error_message(inter, "move_error", member)
            return

        if member.voice.channel != channel:
            await member.move_to(channel)
        else:
            await send_error_message(inter, "move_new_channel_error", member)
            return 0

        await send_message(inter, "move", user=member, **{"reason": reason, "channel": channel})

     

    @commands.slash_command(name="deafen", description=get_description("deafen"))
    @allowed_roles(*get_command_allow_roles("deafen"))
    @allowed_channels(*get_command_allow_channels("deafen"))
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
            await send_error_message(inter, "deafen_error", member)

     

    @commands.slash_command(name="undeafen", description=get_description("undeafen"))
    @allowed_roles(*get_command_allow_roles("undeafen"))
    @allowed_channels(*get_command_allow_channels("undeafen"))
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
            await send_error_message(inter, "undeafen_error", member)

     

    @commands.slash_command(name="addrole", description=get_description("addrole"))
    @allowed_roles(*get_command_allow_roles("addrole"))
    @allowed_channels(*get_command_allow_channels("addrole"))
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
            await send_error_message(inter, "addrole_error", member)
            return
        await member.add_roles(role)
        await send_message(inter, "addrole", user=member, **{"reason": reason, "role": role})

     

    @commands.slash_command(name="rmrole", description=get_description("rmrole"))
    @allowed_roles(*get_command_allow_roles("rmrole"))
    @allowed_channels(*get_command_allow_channels("rmrole"))
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
            await send_error_message(inter, "rmrole_error", member)
            return
        await member.remove_roles(role)
        await send_message(inter, "rmrole", user=member, **{"reason": reason, "role": role})

     

    @commands.slash_command(name="ping", description=get_description("ping"))
    @allowed_roles(*get_command_allow_roles("ping"))
    @allowed_channels(*get_command_allow_channels("ping"))
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """
        Получить пинг бота

        Parameters
        ----------

        """
        await send_message(inter, "ping", user="", **{"ping": self.bot.latency})

     

    @commands.slash_command(name="slowmode", description=get_description("slowmode"))
    @allowed_roles(*get_command_allow_roles("slowmode"))
    @allowed_channels(*get_command_allow_channels("slowmode"))
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
    @allowed_roles(*get_command_allow_roles("vkick"))
    @allowed_channels(*get_command_allow_channels("vkick"))
    async def vkick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = ""):
        """
        Отключить участника от голосового канала

        Parameters
        ----------
        member: Участник
        reason: Причина (необязательно)
        """
        if member.voice:
            await member.edit(voice_channel=None)
            await send_message(inter, "vkick", user=member, **{"reason": reason})

        else:
            await send_error_message(inter, "vkick_error", member)

     

    @commands.slash_command(name="warn", description=get_description("warn"))
    @allowed_roles(*get_command_allow_roles("warn"))
    @allowed_channels(*get_command_allow_channels("warn"))
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
    @allowed_roles(*get_command_allow_roles("warns"))
    @allowed_channels(*get_command_allow_channels("warns"))
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
    @allowed_roles(*get_command_allow_roles("rmwarn"))
    @allowed_channels(*get_command_allow_channels("rmwarn"))
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
        try:
            _ = get_user_warnings(member.name)[index]
        except IndexError:
            await send_error_message(inter, "rm_warns_index_error")
            return
        answer = remove_warnings(member.name, index)
        await send_message(inter, "rmwarn", user=member, **{"reason": reason, "argument": index})

     

    @commands.slash_command(name="report", description=get_description("report"))
    @allowed_roles(*get_command_allow_roles("report"))
    @allowed_channels(*get_command_allow_channels("report"))
    async def report(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Пожаловаться на участника

        Parameters
        ----------
        member: Пользователь, на которого вы хотите пожаловаться
        """
        from modals.report_modals import ReportModal
        await inter.response.send_modal(modal=ReportModal(member))

     

    
    @ban.error
    async def ban_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @kick.error
    async def kick_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @unban.error
    async def unban_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @mute.error
    async def mute_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @unmute.error
    async def unmute_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @chatmute.error
    async def chatmute_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @chatunmute.error
    async def chatunmute_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @timeout.error
    async def timeout_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @rmtimeout.error
    async def rmtimeout_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @fullban.error
    async def fullban_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @clear.error
    async def clear_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @afk.error
    async def afk_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @move.error
    async def move_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @deafen.error
    async def deafen_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @undeafen.error
    async def undeafen_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @addrole.error
    async def addrole_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @rmrole.error
    async def rmrole_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @ping.error
    async def ping_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @slowmode.error
    async def slowmode_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @vkick.error
    async def vkick_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @warn.error
    async def warn_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @warns.error
    async def warns_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @rmwarn.error
    async def rmwarn_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @report.error
    async def report_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    
