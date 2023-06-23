# from msilib.schema import CheckBox

from flask_wtf import FlaskForm, Form
from wtforms import PasswordField, StringField, SubmitField, EmailField, BooleanField, HiddenField, SelectField
from wtforms.validators import DataRequired, InputRequired


class Token(FlaskForm):
    token = StringField("Токен", validators=[InputRequired(), DataRequired()])
    save = SubmitField("Сохранить")
