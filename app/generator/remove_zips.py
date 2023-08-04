import os
import time

REMOVING_PATH = f"{os.getcwd()}/app/generator"


def start_removing():
    while True:
        for filename in os.listdir(REMOVING_PATH):
            if filename.endswith('.zip'):
                file_path = os.path.join(REMOVING_PATH, filename)
                os.remove(file_path)
                print('Файл {} удален'.format(file_path))

        time.sleep(60 * 30)
