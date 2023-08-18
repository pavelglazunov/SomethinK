

import disnake


class EmbedModal(disnake.ui.Modal):
    def __init__(self):

        components = list()
        components.append(disnake.ui.TextInput(
            label="Заголовок",
            placeholder="текст",
            custom_id="title",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=50,
        ))
        components.append(disnake.ui.TextInput(
            label="Описание",
            placeholder="текст",
            custom_id="description",
            style=disnake.TextInputStyle.paragraph,
            min_length=0,
            max_length=100,
        ))

        components.append(disnake.ui.TextInput(
            label=f"Футер",
            placeholder="текст",
            custom_id=f"footer",
            style=disnake.TextInputStyle.short,
            min_length=0,
            max_length=100,
            required=False
        ))
        components.append(disnake.ui.TextInput(
            label=f"Цвет",
            placeholder="цвет в формате HEX (без #)",
            custom_id=f"color",
            style=disnake.TextInputStyle.short,
            min_length=6,
            max_length=6,
        ))
        super().__init__(title="заполнение embed", components=components, custom_id="report_data")

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        try:
            int(interaction.text_values["color"], 16)
        except Exception:

            return
        embed = disnake.Embed()
        embed.title = interaction.text_values["title"]
        embed.description = interaction.text_values["description"]
        embed.set_footer(text=interaction.text_values["footer"])
        embed.color = int(interaction.text_values["color"], 16)

        await interaction.response.send_message(embed=embed)


