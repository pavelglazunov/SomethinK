from app import application, db_session
from app.generator.remove_zips import start_removing
from SomethinKTelegramBot import dp, remove_codes
from aiogram.utils import executor
from threading import Thread

if __name__ == '__main__':
    db_session.global_init("save/db.db")

    Thread(target=start_removing).start()
    Thread(target=remove_codes).start()

    # Flask app
    Thread(target=lambda: application.run(host="127.0.0.1", port=8080, debug=True, use_reloader=False)).start()

    # Telegram bot
    executor.start_polling(dp, skip_updates=True)

"""

./config.py
/config.py
config.py

./app/ds_config.py
/app/ds_config.py
app/ds_config.py
"""
