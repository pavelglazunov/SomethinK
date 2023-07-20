import os
from app import app, db_session
from telegramAuthBot import dp, remove_codes
from aiogram.utils import executor
from threading import Thread

# class FlaskApp(threading.Thread):
#     def run(self) -> None:
#         db_session.global_init("app/db/db.db")
#         app.run(host="127.0.0.1", port=8080, debug=True)


# class TelegramApp(threading.Thread):
#     def run(self) -> None:
#         executor.start_polling(dp, skip_updates=True)


# from app.models import User, Post, Tag, Category, Employee, Feedback
# from flask_script import Manager, Shell

# from flask_migrate import MigrateCommand

# manager = Manager(app)

# # эти переменные доступны внутри оболочки без явного импорта
# def make_shell_context():
#     return dict(app=app, db=db, User=User, Post=Post, Tag=Tag, Category=Category, Employee=Employee, Feedback=Feedback)


# manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

# def flask_app():
#     db_session.global_init("app/db/db.db")
#     app.run(host="127.0.0.1", port=8080, debug=True)
#
#
# def start_threads():
#     t = Thread(target=flask_app)
#     t.start()


if __name__ == '__main__':
    db_session.global_init("app/db/db.db")

    # app.run(host="127.0.0.1", port=8080, debug=True, threaded=True)

    # Flask app
    Thread(target=lambda: app.run(host="127.0.0.1", port=8080, debug=True, use_reloader=False)).start()

    # Clear register codes
    Thread(target=remove_codes).start()

    # Telegram bot
    executor.start_polling(dp, skip_updates=True)

    # print("here")
# flask_app = FlaskApp()
# telegram_app = TelegramApp()
# flask_app.start()
# telegram_app.start()
