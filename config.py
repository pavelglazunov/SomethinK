import os

app_dir = os.path.abspath(os.path.dirname(__file__))


# ONLINE = False


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'yandexlyceum_secret_key'
    JWT_SECRET_KEY = 'super-secret'
    RECAPTCHA_PUBLIC_KEY = "6LftGX8lAAAAACiqSptlqEiqmsU0lhAwOLSKOFnR"
    RECAPTCHA_PRIVATE_KEY = "6LftGX8lAAAAAP6c0fTEa5K0b0gOQCOCfEwb2NrT"

    ##### настройка Flask-Mail #####
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_DEBUG = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'somethinkbots@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'vdlhtksjgfpqavno'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    ##### настройка SQL #####
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TELEGRAM_BOT_TOKEN = "6228611353:AAHBaxvVIhBP9HdkHFq4Cw7FS0hNNCY0uJg"


class DevelopementConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or \
    #                           'mysql+pymysql://root:pass@localhost/flask_app_db'


class TestingConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or \
    #                           'mysql+pymysql://root:pass@localhost/flask_app_db'


class ProductionConfig(BaseConfig):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or \
    #                           'mysql+pymysql://root:pass@localhost/flask_app_db'
