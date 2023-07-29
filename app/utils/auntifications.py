import smtplib
from config import BaseConfig


def send_message(text, recipients):
    user = BaseConfig.MAIL_DEFAULT_SENDER
    passwd = BaseConfig.MAIL_PASSWORD
    server = "smtp.gmail.com"
    port = 587

    subject = "no-reply SomethinK"
    charset = 'Content-Type: text/plain; charset=utf-8'
    mime = 'MIME-Version: 1.0'

    msg = f"Ссылка для <h1>подтверждения</h1> регистрации: {text}"
    body = "\r\n".join((f"From: {user}", f"To: {recipients}",
                        f"Subject: {subject}", mime, charset, "", msg))

    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user, passwd)
        smtp.sendmail(user, recipients, body.encode('utf-8'))

    except smtplib.SMTPException as err:
        print(f"Email error: {err}")
