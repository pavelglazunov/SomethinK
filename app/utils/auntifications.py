import smtplib
from config import BaseConfig
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# def send_token_message(token):
#     return

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

        print("OK")
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err


# def send_message(message, email):
#     sender = BaseConfig.MAIL_DEFAULT_SENDER
#     password = BaseConfig.MAIL_PASSWORD
#
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#
#     try:
#         server.login(sender, password)
#
#         text = "Подтверждение почты"
#         html = f"""\
#         <html>
#           <head></head>
#           <body>
#             <h1>Подтверждение почты</h1>
#             <p>Перейдите по этой ссылке, чтобы подтвердить почту: {message}</p>
#           </body>
#         </html>
#         """
#
#         msg = MIMEMultipart('alternative')
#         msg['Subject'] = "no-reply SomethinK"
#         msg['From'] = BaseConfig.MAIL_DEFAULT_SENDER
#         msg['To'] = email
#
#         part1 = MIMEText(text, 'plain')
#         part2 = MIMEText(html, 'html')
#
#         msg.attach(part1)
#         msg.attach(part2)
#         # msg = MIMEText(
#         #     f"Subject: no-reply\n", "html")
#         # msg["Subject"] = "no-reply SomethinK"
#         # print(message)
#         # print(msg.as_string()[148:160])
#         # print(msg.as_string())
#         server.sendmail(sender, "p6282813@yandex.ru", msg.as_string()
#                         )
#         print("message send")
#     except Exception as e:
#         print(e)
#         print(message[148:160])
#         return e


# send_message("InFxamhkc2RqQHlhbmRleC5ydSI.ZDW11Q.DAxnycok0oHCBKRdEV6kaP_XCuk", "p6282813@yandex.ru")
