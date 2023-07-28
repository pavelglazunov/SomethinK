import datetime
import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    confirm_user = sqlalchemy.Column(sqlalchemy.Boolean)
    premium = sqlalchemy.Column(sqlalchemy.Boolean)
    discord = sqlalchemy.Column(sqlalchemy.String)
    # discord_auth_token = sqlalchemy.Column(sqlalchemy.String)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    # token = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def get_token(self, expire_time=2):
        expires_delta = datetime.timedelta(expire_time)
        token = create_access_token(identity=self.id, expires_delta=expires_delta)
        return token

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class Projects(SqlAlchemyBase):
    __tablename__ = 'projects'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    author_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    bot_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    config_json = sqlalchemy.Column(sqlalchemy.JSON, nullable=False)
    create_datetime = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
