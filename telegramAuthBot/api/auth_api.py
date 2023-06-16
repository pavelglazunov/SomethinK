import datetime
import json

from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import config
from random import randint
import hashlib

import os

from app.data import db_session
from app.data.users import User

s = URLSafeTimedSerializer(config.BaseConfig.SECRET_KEY)


def generate_api_token(user_email):
    code = str(randint(10000, 999999))

    with open("./telegramAuthBot/api/tokens.json", "r") as f:
        data = json.load(f)
        while code in data:
            code = str(randint(10000, 999999))

        code_salt = code + "salt"
        data[hashlib.sha512(code_salt.encode()).hexdigest()] = {
            "email": user_email,
            "time_over": datetime.datetime.now() + datetime.timedelta(minutes=10)
        }

    with open("./telegramAuthBot/api/tokens.json", "w") as f:
        json.dump(data, f, default=str)

    return code


def submit_api_token(code):
    with open("./telegramAuthBot/api/tokens.json", "r") as f:
        data = json.load(f)

    code_salt = code + "salt"
    hash_code = hashlib.sha512(code_salt.encode()).hexdigest()
    if hash_code in data:
        email = data[hash_code]["email"]

        # if datetime.datetime.strptime(data["time_over"], datetime.datetime.) > datetime.datetime.now():
        #     return "Время действия кода истекло"

        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == email).first()
        user.confirm_user = True
        db_sess.commit()

        data.pop(hash_code)

        with open("./telegramAuthBot/api/tokens.json", "w") as f:
            json.dump(data, f)

        return ""
    return "Некорректный код"
