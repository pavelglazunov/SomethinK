import datetime
import json
import time


def remove_codes():
    while True:
        print("removing..")
        with open("./telegramAuthBot/api/tokens.json", "r") as f:
            data = json.load(f)

        new_data = {}
        for code, value in data.items():

            # print(datetime.datetime.strptime(value["time_over"], "%Y-%m-%d %H:%M:%S.%f") > datetime.datetime.now())
            if datetime.datetime.strptime(value["time_over"], "%Y-%m-%d %H:%M:%S.%f") < datetime.datetime.now():
                print(code)
                continue
            new_data[code] = value

        with open("./telegramAuthBot/api/tokens.json", "w") as file:
            json.dump(new_data, file)

        time.sleep(60)


# remove_codes()
