
import datetime
import disnake
from disnake.ext import commands
from utils.parser import get_command_allow_roles, get_command_allow_channels
from utils.decorators import allowed_channels, allowed_roles
from utils.messages import send_message, send_long_message, get_description
from utils.messages import send_error_message, detected_error

 
import requests

 
from modals.embed_modals import EmbedModal
 
from modals.feedback_modals import FeedbackTypeSelect

 
from translate import Translator

 
languages = commands.option_enum({
    "Английский": "en",
    "Русский": "ru",
    "Японский": "ja",
    "Испанский": "es",
    "Французский": "fr",
    "Украинский": "uk",
    "Китайский": "zh",
    "Итальянский": "it",
    "Португальский": "pt"
})
 
class AnotherCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

     
    @commands.slash_command(name="color", description=get_description("color"))
    @allowed_roles(*get_command_allow_roles("color"))
    @allowed_channels(*get_command_allow_channels("color"))
    async def color(self, inter: disnake.ApplicationCommandInteraction,
                    color: commands.String[0, 6] or commands.String[2, 2]):
        """
        Изменить цвет имени в чате

        Parameters
        ----------
        color: Цвет в формате HEX (без ) или -1 для очистки цвета
        """

        await send_long_message(inter, "color")
        color = color.lower()
        try:
            int(color, 16)
        except Exception:
            await send_error_message(inter, "color_input_error", **{"edit_original_message": True})
            return
        if len(color) == 2 and color != "-1":
            await send_error_message(inter, "color_input_error", **{"edit_original_message": True})
            return
        if color == "-1":
            for user_role in inter.user.roles:
                if user_role.name == "":
                    await inter.user.remove_roles(user_role,
                                                  reason="Пользователь {} сбросил цвет при помощи команды /color -1 путем снятия роли {} в {}".format(
                                                      inter.user.name, user_role.name, datetime.datetime.now()))

            for guild_role in inter.guild.roles:
                if guild_role.name == "" and len(guild_role.members) == 0:
                    await guild_role.delete(
                        reason="Роль {} была удаленна после того, как последний участник ({}) снял ее при помощи команды /color -1 в {}".format(
                            guild_role.name, inter.user.name, datetime.datetime.now()))
            await inter.edit_original_message("Ваш цвет сброшен")

            return 0

        if len([i for i in color if i in "0123456789abcdef"]) != len(color):
            await send_error_message(inter, "color_input_error", **{"edit_original_message": True})
            return

        for r in inter.guild.roles:
            if r.name == "":
                if str(r.color)[1:] == color:
                    role = r
                if inter.user.id in list(map(lambda x: x.id, r.members)):
                    await inter.user.remove_roles(r)
                    await r.delete(
                        reason="Роль {} была удаленна после того, как последний участник ({}) заменил ее при помощи команды /color -1 в {}".format(
                            r.name, inter.user.name, datetime.datetime.now()))
        else:
            role = await self.bot.guilds[0].create_role(
                name=f" ",
                color=int(color, 16)
            )

        bot_member = inter.guild.get_member(self.bot.user.id)
        bot_role_position = bot_member.top_role.position

        await inter.guild.edit_role_positions(positions={role: bot_role_position - 1})
        await inter.user.add_roles(role,
                                   reason="Пользователь {} изменил цвет на {} при помощи команды /color путем получения роли color_{} в {}".format(
                                       inter.user.name, color, color, datetime.datetime.now()))
        await send_message(inter, "color", user=inter.author,
                           **{"argument": color, "edit_original_message": True})

     
    @commands.slash_command(name="nick", description=get_description("nick"))
    @allowed_roles(*get_command_allow_roles("nick"))
    @allowed_channels(*get_command_allow_channels("nick"))
    async def nick(self, inter: disnake.ApplicationCommandInteraction, name: str):
        """
        Изменить имя в чате

        Parameters
        ----------
        name: Новое имя
        """
        await inter.user.edit(nick=name,
                              reason="Пользователь {} изменил имя в чате на {} при помощи команды /nick в {}".format(
                                  inter.user.name, name, datetime.datetime.now()))

        await send_message(inter, "nick", user="", **{"argument": name})

     
    @commands.slash_command(name="joke", description=get_description("joke"))
    @allowed_roles(*get_command_allow_roles("joke"))
    @allowed_channels(*get_command_allow_channels("joke"))
    async def joke(self, inter: disnake.ApplicationCommandInteraction):
        """
        Случайный анекдот

        Parameters
        ----------
        """
        await send_long_message(inter, "joke")
        joke = requests.get(" http://rzhunemogu.ru/RandJSON.aspx?CType=1").text[12:-2]

        await send_message(inter, "joke", user="", **{"result": joke,
                                                      "edit_original_message": True})

     
    @commands.slash_command(name="translate", description=get_description("translate"))
    @allowed_roles(*get_command_allow_roles("translate"))
    @allowed_channels(*get_command_allow_channels("translate"))
    async def translate(self, inter: disnake.ApplicationCommandInteraction, from_language: languages,
                        to_language: languages, text: str):
        """
        Перевод текста с одного языка на другой

        Parameters
        ----------
        from_language: перевести с
        to_language: перевести на
        text: Текст, который нудно перевести
        """
        await send_long_message(inter, "translate")
        translator = Translator(from_lang=from_language, to_lang=to_language)
        answer = translator.translate(text)
        await send_message(inter, "translate", user="", **{"result": answer, "from_language": from_language,
                                                           "to_language": to_language, "text": text,
                                                           "edit_original_message": True})

     
    @commands.slash_command(name="say", description=get_description("say"))
    @allowed_roles(*get_command_allow_roles("say"))
    @allowed_channels(*get_command_allow_channels("say"))
    async def say(self, inter: disnake.ApplicationCommandInteraction, text: str):
        """
        Написать текст от имени бота

        Parameters
        ----------
        text: Текст, который нудно перевести
        """
        await send_message(inter, "say", user="", **{"result": text})

     
    @commands.slash_command(name="avatar", description=get_description("avatar"))
    @allowed_roles(*get_command_allow_roles("avatar"))
    @allowed_channels(*get_command_allow_channels("avatar"))
    async def avatar(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Получить аватар пользователя

        Parameters
        ----------
        member: Пользователь
        """
        embed = disnake.Embed()

        embed.set_image(member.avatar)

        await inter.send(embed=embed)

     
    @commands.slash_command(name="embed", description=get_description("embed"))
    @allowed_roles(*get_command_allow_roles("embed"))
    @allowed_channels(*get_command_allow_channels("embed"))
    async def embed(self, inter: disnake.ApplicationCommandInteraction):
        """
        Создать embed

        Parameters
        ----------
        """
        await inter.response.send_modal(modal=EmbedModal())

     
    @commands.slash_command(name="feedback", description=get_description("feedback"))
    @allowed_roles(*get_command_allow_roles("feedback"))
    @allowed_channels(*get_command_allow_channels("feedback"))
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

     

    
    @color.error
    async def color_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @nick.error
    async def nick_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @joke.error
    async def joke_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @translate.error
    async def translate_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @say.error
    async def say_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @avatar.error
    async def avatar_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @embed.error
    async def embed_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    @feedback.error
    async def feedback_error(self, ctx, error_):
        await detected_error(ctx, error_)

    
    
