import datetime
import json
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import secrets

from random import randint
import hashlib

from app.data import db_session
from app.data.users import User
from config import BaseConfig


def send_authentication_code(user_email):
    email_server = smtplib.SMTP_SSL(BaseConfig.MAIL_SERVER, int(BaseConfig.MAIL_PORT))
    email_server.login(BaseConfig.MAIL_USERNAME, BaseConfig.MAIL_PASSWORD)

    email_message = MIMEMultipart()

    email_message["From"] = BaseConfig.MAIL_USERNAME

    email_message["To"] = user_email

    email_message["Subject"] = Header("Авторизация", 'utf-8')

    auth_code = generate_authentication_code(user_email)
    message_body = """
    <div style="display: flex; flex-direction: column; align-items: center">
        <p>Your authorization code:</p>
        <h1>{code}</h1>
        <p>Do not share this code with anyone</p>
    </div>
    """.replace("{code}", str(auth_code))

    text = MIMEText(message_body, "html", 'utf-8')
    email_message.attach(text)

    email_server.sendmail(BaseConfig.MAIL_USERNAME, user_email, email_message.as_string())

    email_server.quit()
    pass


def _random_number():
    num = secrets.randbits(20)

    while num < 100000 or num > 999999:
        num = secrets.randbits(20)

    return num


def generate_authentication_code(user_email):

    with open("./app/tokens.json", "r") as f:
        data = json.load(f)
        while (code := str(_random_number())) in data:
            pass

        code_salt = code + BaseConfig.CODE_SALT

        data[user_email] = {
            "time_over": datetime.datetime.now() + datetime.timedelta(minutes=10),
            "code": hashlib.sha512(code_salt.encode()).hexdigest()
        }
        print(hashlib.sha512(code_salt.encode()).hexdigest())
    with open("./app/tokens.json", "w") as f:
        json.dump(data, f, default=str)

    return code


def confirm_authentication_code(code):
    with open("./app/tokens.json", "r") as f:
        data = json.load(f)

    code_salt = code + BaseConfig.CODE_SALT
    hash_code = hashlib.sha512(code_salt.encode()).hexdigest()

    for email, v in data.items():
        if v.get("code") == hash_code:
            data.pop(email)

            with open("./app/tokens.json", "w") as f:
                json.dump(data, f)

            return email
    return False


def remove_authentication_code():
    while True:
        with open("./app/tokens.json", "r") as f:
            data = json.load(f)

        new_data = {}
        for email, value in data.items():
            if datetime.datetime.strptime(value["time_over"], "%Y-%m-%d %H:%M:%S.%f") < datetime.datetime.now():
                continue
            new_data[email] = value

        with open("./app/tokens.json", "w") as file:
            json.dump(new_data, file)

        time.sleep(60)
