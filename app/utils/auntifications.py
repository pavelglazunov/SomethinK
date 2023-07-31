import datetime
import json
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from random import randint
import hashlib

from app.data import db_session
from app.data.users import User
from config import BaseConfig


def send_authentication_code(user_email):
    print(user_email)
    email_server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    print("server created")
    email_server.login(BaseConfig.MAIL_USERNAME, BaseConfig.MAIL_PASSWORD)
    print("account logged")

    email_message = MIMEMultipart()
    print("message object created")

    email_message["From"] = BaseConfig.MAIL_USERNAME
    print("message from")

    email_message["To"] = user_email
    print("message to")

    email_message["Subject"] = "Авторизация"
    print("message subject")

    code = generate_authentication_code(user_email)
    print("code generated")

    message_body = """
    <div style="display: flex; flex-direction: column; align-items: center">
        <p>Код подтверждения для входа в SomethinK</p>
        <h1>{code}</h1>
        <p>Не сообщайте никому данный код</p>
    </div>

    """.replace("{code}", str(code))
    print("message text created")

    email_message.attach(MIMEText(message_body, "html"))
    print("text added to message")

    message_text = email_message.as_string()
    print("convert to string")

    email_server.sendmail(BaseConfig.MAIL_USERNAME, user_email, message_text)
    print("message sent")

    email_server.quit()
    print("server closed")

    pass


def generate_authentication_code(user_email):
    code = str(randint(100000, 999999))

    with open("./app/tokens.json", "r") as f:
        data = json.load(f)
        while code in data:
            code = str(randint(100000, 999999))

        print("code >", code)
        code_salt = code + BaseConfig.CODE_SALT
        data[hashlib.sha512(code_salt.encode()).hexdigest()] = {
            "email": user_email,
            "time_over": datetime.datetime.now() + datetime.timedelta(minutes=10)
        }

    with open("./app/tokens.json", "w") as f:
        json.dump(data, f, default=str)

    return code


def confirm_authentication_code(code):
    with open("./app/tokens.json", "r") as f:
        data = json.load(f)

    code_salt = code + BaseConfig.CODE_SALT
    hash_code = hashlib.sha512(code_salt.encode()).hexdigest()
    if hash_code in data:
        email = data[hash_code]["email"]

        data.pop(hash_code)

        with open("./app/tokens.json", "w") as f:
            json.dump(data, f)

        return email
    return False


def remove_authentication_code():
    while True:
        print("removing..")
        with open("./app/tokens.json", "r") as f:
            data = json.load(f)

        new_data = {}
        for code, value in data.items():

            # print(datetime.datetime.strptime(value["time_over"], "%Y-%m-%d %H:%M:%S.%f") > datetime.datetime.now())
            if datetime.datetime.strptime(value["time_over"], "%Y-%m-%d %H:%M:%S.%f") < datetime.datetime.now():
                print(code)
                continue
            new_data[code] = value

        with open("./app/tokens.json", "w") as file:
            json.dump(new_data, file)

        time.sleep(60)
