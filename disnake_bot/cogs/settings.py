import datetime

import disnake
from disnake.ext import commands
from disnake_bot.config import MODERATION_COMMANDS, EVERYONE_COMMANDS

from disnake_bot.utils.parser import get_command_allow_roles, get_command_allow_channels
from disnake_bot.utils.decorators import allowed_channels, edit_json
from disnake_bot.config import CONFIG_JSON_FILENAME
from disnake_bot.utils.warnings import add_warning, get_user_warnings, remove_warnings

from disnake_bot.modals.report_modals import ReportUserSelect, ReportModal
from disnake_bot.modals.embed_modals import EmbedModal
from disnake_bot.modals.feedback_modals import FeedbackTypeSelect

from enum import Enum

# from disnake_bot import _message, _errors

logging_actions = {
    "выключено": "off",
    "логировать в спец. канал": "channel",
    "логировать в файл": "file",
    "логировать в спец. канал + файл": "channel+file",
}
logging_actions_enum = commands.option_enum(logging_actions)


@edit_json(CONFIG_JSON_FILENAME)
def update_settings(key, value, data):
    data[key] = value


class SettingsCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(name="log", description="Настроить логирование")
    @commands.has_any_role(*get_command_allow_roles("log"))
    @allowed_channels(*get_command_allow_channels("log"))
    async def log(self, inter: disnake.ApplicationCommandInteraction, param: logging_actions_enum):
        """
        Настроить логирование

        Parameters
        ----------
        param: тип логирования
        """
        update_settings("logging", param)
        await inter.response.send_message(
            f"Тип логирования изменен на: {[k for k, v in logging_actions.items() if v == param][0]}")

    @commands.slash_command(name="ar_update", description="Изменить интервал обновления ролей активности")
    @commands.has_any_role(*get_command_allow_roles("ar_update"))
    @allowed_channels(*get_command_allow_channels("ar_update"))
    async def ar_update(self, inter: disnake.ApplicationCommandInteraction, interval: commands.Range[2, ...]):
        """
        Изменить интервал обновления ролей активности

        Parameters
        ----------
        interval: интервал обновления ролей активности в минутах
        """
        update_settings("ar_update_interval", interval)
        await inter.response.send_message(
            f"Интервал обновления ролей активности изменен на: {interval}")
