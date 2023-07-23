import datetime

import disnake
from disnake_bot.config import REPORT_CHANNEL_ID
from disnake_bot.utils.messages import send_message


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

        channel = interaction.guild.get_channel(REPORT_CHANNEL_ID)
        report_embed = disnake.Embed(color=0xfa0a76, title=f"Новая жалоба",
                                     description=f"Жалоба на {self.mention}")
        report_embed.add_field(name="Детали", value=details)
        report_embed.add_field(name="жалоба пришла от", value=f"{interaction.author.mention}", inline=False)
        report_embed.set_footer(text=f"Жалоба получена в {datetime.datetime.now()}")
        await channel.send(embed=report_embed)


class ReportUserSelect(disnake.ui.Select):
    def __init__(self, inter: disnake.ApplicationCommandInteraction):
        options = []
        for member in inter.guild.members:
            opt = disnake.SelectOption(label=member.display_name, value=f"{member.name};{member.mention}")
            options.append(opt)

        super().__init__(
            placeholder="Выберите участника", options=options, min_values=0, max_values=1, custom_id="reported_member"
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            await interaction.response.send_modal(ReportModal(interaction.values[0]))
