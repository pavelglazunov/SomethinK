import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

fromaddr = "confirm@somethinkbots.ru"
toaddr = "p6282813@yandex.ru"
mypass = "qAMWkm9LcWuATCLsAWiT"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "data base"

body = """
data base
"""
msg.attach(MIMEText(body, 'html'))

with open("db/db.db", "rb") as file:
    part = MIMEApplication(
        file.read(),
        Name="db.db"
    )
    part['Content-Disposition'] = 'attachment; filename="%s"' % "db.db"
    msg.attach(part)

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
