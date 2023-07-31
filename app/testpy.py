import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "confirm@somethinkbots.ru"
toaddr = "p6282813@yandex.ru"
mypass = "qAMWkm9LcWuATCLsAWiT"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "авторизация"
code = random.randint(100000, 1000000)

body = """
<div style="display: flex; flex-direction: column; align-items: center">
    <p>Код подтверждения для входа в SomethinK</p>
    <h1>{code}</h1>
    <p>Не сообщайте никому данный код</p>
</div>

""".replace("{code}", str(code))
msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
