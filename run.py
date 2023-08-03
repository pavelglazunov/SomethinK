from app import application, db_session
from app.generator.remove_zips import start_removing
from SomethinKTelegramBot import dp
from app.utils.auntifications import remove_authentication_code
from aiogram.utils import executor
from threading import Thread

if __name__ == '__main__':
    db_session.global_init("app/db/db.db")

    # Thread(target=start_removing).start()
    # Thread(target=remove_authentication_code).start()

    # Flask app
    # application.run(host="127.0.0.1", port=8080, debug=True, use_reloader=False)
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
