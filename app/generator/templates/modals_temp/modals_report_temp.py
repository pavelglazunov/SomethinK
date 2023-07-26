MODAL_REPORT = """
import datetime

import disnake

from _____project_name_for_imports_____.utils.messages import send_message
from _____project_name_for_imports_____.utils.parser import parse_config

class ReportModal(disnake.ui.Modal):
    def __init__(self, member: disnake.Member):
        self.name, self.mention = member.name, member.mention

        components = [
            disnake.ui.TextInput(
                label="Подробности жалобы",
                placeholder="Опишите детали вашей жалобы",
                custom_id="details",
                style=disnake.TextInputStyle.paragraph,
                min_length=10,
                max_length=500
            )
        ]

        title = f"Жалоба на {self.name}"
        super().__init__(title=title, components=components, custom_id="report_data")

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        details = interaction.text_values["details"]

        await send_message(interaction, "report")

        channel = interaction.guild.get_channel(parse_config("channels_ID.report_channel_id"))
        report_embed = disnake.Embed(color=0xfa0a76, title=f"Новая жалоба",
                                     description=f"Жалоба на {self.mention}")
        report_embed.add_field(name="Детали", value=details)
        report_embed.add_field(name="жалоба пришла от", value=f"{interaction.author.mention}", inline=False)
        report_embed.set_footer(text=f"Жалоба получена в {datetime.datetime.now()}")
        await channel.send(embed=report_embed)

"""