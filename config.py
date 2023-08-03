import os
from dotenv import load_dotenv

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    load_dotenv()
    SECRET_KEY = os.getenv("SK_SECRET_KEY") or "very secret key"
    JWT_SECRET_KEY = os.getenv("SK_JWT_KEY") or "super-secret"
    CODE_SALT = os.getenv("SK_CODE_SALT") or "salt"

    # настройка Flask-Mail
    MAIL_SERVER = os.getenv("SK_MAIL_SERVER") or 'smtp.googlemail.com'
    MAIL_PORT = os.getenv("SK_MAIL_PORT") or 465
    MAIL_USERNAME = os.environ.get('SK_MAIL_USERNAME') or 'your_email@gmail.com'
    MAIL_PASSWORD = os.environ.get('SK_MAIL_PASSWORD') or 'special_password'

    # настройка SQL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # настройка telegram
    TELEGRAM_BOT_TOKEN = os.getenv("SK_TELEGRAM_BOT_TOKEN") or "TOKEN"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
