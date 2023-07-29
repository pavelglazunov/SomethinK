from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class Token(FlaskForm):
    token = StringField("Токен", validators=[InputRequired(), DataRequired()])
    save = SubmitField("Сохранить")


class CreateFinsh(FlaskForm):
    project_name = StringField("Имя бота", validators=[InputRequired()])
    create_button = SubmitField("Создать")
