import datetime

import disnake
import requests
from disnake.ext import commands
from disnake_bot.config import MODERATION_COMMANDS, EVERYONE_COMMANDS

from disnake_bot.utils.parser import get_command_allow_roles, get_command_allow_channels
from disnake_bot.utils.decorators import allowed_channels
from disnake_bot.config import WEATHER_API_KEY
from disnake_bot.event_logging import log

from disnake_bot import _message, _errors

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

    @commands.slash_command(name="color", description="Изменить цвет имени в чате")
    @commands.has_any_role(*get_command_allow_roles("color"))
    @allowed_channels(*get_command_allow_channels("color"))
    @commands.check(predicate=lambda inr: log(inr, "/color", "commands"))
    async def color(self, inter: disnake.ApplicationCommandInteraction,
                    color: commands.String[0, 6] or commands.String[2, 2]):
        """
        Изменить цвет имени в чате

        Parameters
        ----------
        color: Цвет в формате HEX (без #) или -1 для очистки цвета
        """

        color = color.lower()
        try:
            int(color, 16)
        except Exception:
            await inter.response.send_message("Вы ввели неправильный цвет", ephemeral=True)
            return
        if len(color) == 2 and color != "-1":
            await inter.response.send_message("Введено неверное значение цвета", ephemeral=True)
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
            await inter.response.send_message("Ваш цвет сброшен", ephemeral=True)

            return 0

        if len([i for i in color if i in "0123456789abcdef"]) != len(color):
            await inter.response.send_message("Введено неверное значение цвета", ephemeral=True)
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
        await inter.response.send_message("Ваш цвет изменен на #{}".format(color), ephemeral=True)

    @commands.slash_command(name="nick", description="Изменить имя в чате")
    @commands.has_any_role(*get_command_allow_roles("nick"))
    @allowed_channels(*get_command_allow_channels("nick"))
    @commands.check(predicate=lambda inr: log(inr, "/nick", "commands"))
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
        await inter.response.send_message("Ваше имя изменено на {}".format(name), ephemeral=True)

    @commands.slash_command(name="joke", description="Случайный анекдот")
    @commands.has_any_role(*get_command_allow_roles("joke"))
    @allowed_channels(*get_command_allow_channels("joke"))
    @commands.check(predicate=lambda inr: log(inr, "/joke", "commands"))
    async def joke(self, inter: disnake.ApplicationCommandInteraction):
        """
        Случайный анекдот

        Parameters
        ----------

        """
        joke = requests.get(" http://rzhunemogu.ru/RandJSON.aspx?CType=1").text[12:-2]
        await inter.response.send_message(joke + "\n\nАнекдоты взяты с сайта http://rzhunemogu.ru/")

    @commands.slash_command(name="weather", description="Актуальная погода")
    @commands.has_any_role(*get_command_allow_roles("weather"))
    @allowed_channels(*get_command_allow_channels("weather"))
    @commands.check(predicate=lambda inr: log(inr, "/weather", "commands"))
    async def weather(self, inter: disnake.ApplicationCommandInteraction, city: str):
        """
        Актуальная погода

        Parameters
        ----------
        city: Город
        """
        weather = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no&lang=ru").json()
        # print(weather)
        if weather.get("current"):
            answer = f"{weather['current']['condition']['text']}. Температура воздуха: {weather['current']['temp_c']}°. Скорость ветра: {weather['current']['wind_kph']} км/ч"
        else:
            answer = "Произошла ошибка в запросе: " + weather.get("error").get("message")
        await inter.response.send_message(answer)

    @commands.slash_command(name="translate", description="Перевод текста с одного языка на другой")
    @commands.has_any_role(*get_command_allow_roles("translate"))
    @allowed_channels(*get_command_allow_channels("translate"))
    @commands.check(predicate=lambda inr: log(inr, "/translate", "commands"))
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
        translator = Translator(from_lang=from_language, to_lang=to_language)
        answer = translator.translate(text)
        await inter.response.send_message(answer)

    @commands.slash_command(name="say", description="Написать текст от имени бота")
    @commands.has_any_role(*get_command_allow_roles("say"))
    @allowed_channels(*get_command_allow_channels("say"))
    @commands.check(predicate=lambda inr: log(inr, "/say", "commands"))
    async def say(self, inter: disnake.ApplicationCommandInteraction, text: str):
        """
        Написать текст от имени бота

        Parameters
        ----------
        text: Текст, который нудно перевести
        """

        await inter.response.send_message(text)

    @commands.slash_command(name="avatar", description="Получить аватар пользователя")
    @commands.has_any_role(*get_command_allow_roles("avatar"))
    @allowed_channels(*get_command_allow_channels("avatar"))
    @commands.check(predicate=lambda inr: log(inr, "/avatar", "commands"))
    async def avatar(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """
        Получить аватар пользователя

        Parameters
        ----------
        member: Пользователь
        """
        embed = disnake.Embed()

        embed.title = "Аватар пользователя {}".format(member.name)
        embed.set_image(member.avatar)

        await inter.send(embed=embed)
