# import datetime
# import smtplib as smtp
# from email.mime.text import MIMEText
# from email.header import Header
#
# from flask import Flask, render_template, redirect
# from flask_login import LoginManager, current_user, login_required
# from flask_mail import Mail, Message
#
# from data import db_session
# from data.users import User
#
# from bp_create.create_routes import create_bp
# from bp_oauth.oauth_routes import oauth_bp
#
# app = Flask(__name__)
# mail = Mail(app)
#
# # mail.init_app(app)
#
# app.app_context().push()
#
# app.config["SECRET_KEY"] = 'yandexlyceum_secret_key'
# app.config["JWT_SECRET_KEY"] = "super-secret"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['JWT_BLACKLIST-ENABLED'] = True
# app.config['JWT_TOKEN_LOCATION'] = ['cookies']
# app.config['REMEMBER_COOKIE_DURATION'] = datetime.timedelta(days=7)
#
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = 'pavel'
# app.config['MAIL_DEFAULT_SENDER'] = 'somethinkbots@gmail.com'
# app.config['MAIL_PASSWORD'] = 'vdlhtksjgfpqavno'  # 2yShbi7Fh6EBr3P
# app.config["ADMINS"] = ["somethinkbots@gmail.com"]
#
# login_manager = LoginManager()
# login_manager.init_app(app)
#
# app.register_blueprint(create_bp)
# app.register_blueprint(oauth_bp)
#
# # msg = Message('test subject', recipients=["p6282813@yandex.ru"])
# # msg.body = 'text body'
# # msg.html = '<b>HTML</b> body'
# # with app.app_context():
# #     mail.send(msg)
#
#
# #
# # login = 'somethinkbots@gmail.com'
# # password = 'vdlhtksjgfpqavno'
# #
# # server = smtp.SMTP('smtp.gmail.com', 587)
# # server.starttls()
# # server.login(login, password)
# #
# # subject = 'Email'
# # text = 'hello from SomethinK'
# #
# # mime = MIMEText(text, 'plain', 'utf-8')
# # mime['Subject'] = Header(subject, 'utf-8')
#
# # server.sendmail(login, 'p6282813@yandex.ru', f'Subject:{subject}\n{text}')
#
#
# # msg = Message("theme", sender="somethinkbots@gmail.com", recipients=['p6282813@yandex.ru'])
# # msg.body = "Mail body"
# # msg.html = "<h1>SomethinK</h1>"
# # mail.send(msg)
#
#
# if __name__ == '__main__':
#     db_session.global_init("db/db.db")
#     app.run(host="127.0.0.1", port=8080, debug=True)
