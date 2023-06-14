import datetime
import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from .db_session import SqlAlchemyBase


class CreateData(SqlAlchemyBase):
    __tablename__ = "create_data"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))

    create_json = sqlalchemy.Column(sqlalchemy.JSON, nullable=False)
    create_datetime = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)


