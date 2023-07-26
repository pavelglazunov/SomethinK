MODAL_FEEDBACK = """

import datetime
import disnake


class FeedbackModal(disnake.ui.Modal):
    def __init__(self, arg, bot: disnake.ApplicationCommandInteraction):
        self.arg = arg
        self.bot = bot

        if arg == "report":
            self.embed_title = "Новый репорт о баге"
            self.color = "FF0000"
            header_label = "В какой команде произошла ошибка"
            header_placeholder = "Название или краткое описание"
            detail_label = "Опишите подробно ошибку"
            detail_placeholder = "Подробное описание"
            title = "анкета ошибки"
        elif arg == "new":
            self.embed_title = "Новое предложение о нововведении"
            self.color = "00FF00"

            header_label = "Краткое описание"
            header_placeholder = "Введите краткое описание нововведения"
            detail_label = "Описание вашей идеи"
            detail_placeholder = "Опишите подробно то, что вам хотелось бы видеть в боте"
            title = "анкета нововведения"

        else:
            self.embed_title = "Обратная связь"
            self.color = "fcba03"

            header_label = "Краткое описание"
            header_placeholder = "Введите краткое описание"
            detail_label = "Описание"
            detail_placeholder = "текст"
            title = "анкета"

        components = [
            disnake.ui.TextInput(
                label=header_label,
                placeholder=header_placeholder,
                custom_id="header",
                style=disnake.TextInputStyle.short,
                min_length=1,
                max_length=100,
            ),
            disnake.ui.TextInput(
                label=detail_label,
                placeholder=detail_placeholder,
                custom_id="details",
                style=disnake.TextInputStyle.paragraph,
                min_length=10,
                max_length=1000,
            ),
            disnake.ui.TextInput(
                label="Как с вами можно связаться",
                placeholder="(необязательно) Укажите телеграм/дискорд или другой способ связи",
                custom_id="connect",
                style=disnake.TextInputStyle.paragraph,
                required=False,
                min_length=0,
                max_length=150,
            )
        ]

        super().__init__(title=title, components=components, custom_id="feedback_data")

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        header = interaction.text_values["header"]
        details = interaction.text_values["details"]
        connect = interaction.text_values["connect"]

        server_id = interaction.guild.id
        server_name = interaction.guild.name

        bot_id = self.bot.user.id
        bot_name = self.bot.user.name

        from_user_id = interaction.user.id
        from_user_name = interaction.user.name

        actual_datetime = datetime.datetime.now()

        embed = disnake.Embed()
        embed.title = self.embed_title
        embed.description = header
        embed.color = int(self.color, 16)

        embed.add_field(
            name="Детали: ",
            value=details,
            inline=False
        )

        embed.add_field(
            name="Контакты: ",
            value=connect + "|",
            inline=False
        )

        embed.add_field(
            name="Метаданные: ",
            value=f"Server ID: {server_id}\\n"
                  f"Server name: {server_name}\\n"
                  f"Bot ID: {bot_id}\\n"
                  f"Bot name: {bot_name}\\n"
                  f"From ID: {from_user_id}\\n"
                  f"From name: {from_user_name}\\n"
                  f"Time: {actual_datetime}",
            inline=False
        )
        me = await self.bot.fetch_user(582952714175119370)
        await me.send(embed=embed)

        user_embed = disnake.Embed()
        user_embed.title = "Спасибо за обратную связь"
        user_embed.description = "Мы рассмотрим ваше сообщение и при необходимости свяжемся с вами"

        user_embed.color = int("00FF00", 16)

        await interaction.response.send_message(embed=user_embed)


class FeedbackTypeSelect(disnake.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        options = [
            disnake.SelectOption(label="Сообщить об ошибке в работе бота", value="error"),
            disnake.SelectOption(label="Предложить нововведение", value="new"),
            disnake.SelectOption(label="Другое", value="another")
        ]

        super().__init__(
            placeholder="Выберите тип обращения", options=options, min_values=1, max_values=1,
            custom_id="feedback_select"
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            await interaction.response.send_modal(FeedbackModal(interaction.values[0], self.bot))

"""