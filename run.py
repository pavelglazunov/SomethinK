from app import application, db_session
from app.generator.remove_zips import start_removing
from SomethinKTelegramBot import dp
from app.utils.auntifications import remove_authentication_code
from aiogram.utils import executor
from threading import Thread

if __name__ == '__main__':
    db_session.global_init("app/db/db.db")

    Thread(target=start_removing).start()
    Thread(target=remove_authentication_code).start()

    # Flask app
    # application.run(host="94.198.216.152", port=80, debug=True, use_reloader=False)
    Thread(target=lambda: application.run(host="94.198.216.152", port=80, debug=False, use_reloader=False)).start()

    # Telegram bot
    executor.start_polling(dp, skip_updates=True)

"""
remember_token	"8|63e046a1d6042677136ff3294f3679a5f040540b8730567b10419db7231c231f37ad417f99367d622f15838f58449cab3be8465db5c46d897aa7f89228cf7421"
session	".eJwdzjtuA0EIANC7TB1ZMB9g9jIrGEBJ4UTajSvLd_fK9Wves-x5xPldtv_jEV9l__GylZFtYGWuSH3YCl1ixFhXks-JDnFRiuSiTupgDblnUyFMTTRznIhaGdJkDK1G0WJphEs69CbEbeocYAGM02sHgGgEyKzE5YoccY-7xbGfsf5-_SwbQReAG1z4OC_4VKW83povOAk.ZMwXBg._QkI1bgCwAO5UHDx9MwYEpGM23c"
user_jwt	"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3ODIyNzI4MCwianRpIjoiMjlkMzlkZGYtZmQxZi00OWY0LWIyOTktYmQ2ZTk4YTA2Nzk5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjc4MjI3MjgwLCJleHAiOjE2Nzg0MDAwODB9.qc55iStURPuWgUmetibk5ZS3liFZ3sX5hFMT9uc3Yio"
visits_count	"5"
./config.py
/config.py
config.py

./app/ds_config.py
/app/ds_config.py
app/ds_config.py
"""
