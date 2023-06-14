# from msilib.schema import CheckBox

from flask_wtf import FlaskForm, Form
from wtforms import PasswordField, StringField, SubmitField, EmailField, BooleanField, HiddenField, SelectField
from wtforms.validators import DataRequired, InputRequired


class ServersSelect(FlaskForm):
    servers = SelectField()
    submit = SubmitField("сохранить")


class Token(FlaskForm):
    token = StringField("Токен", validators=[InputRequired(), DataRequired()])
    save = SubmitField("Сохранить")


class ModerationMainForm(FlaskForm):
    form_id = HiddenField()

    cm_ban = BooleanField("ban", false_values=True)

    # trigger = StringField("команда")
    # description = StringField("описание")
    #
    # cancel = SubmitField("отмена")
    save = SubmitField("Сохранить")
