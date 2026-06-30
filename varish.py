import schedule
import time
from datetime import datetime


def logger():

    with open("logs.txt", "a") as file:

        file.write(

            f"{datetime.now()} -> Running\n"
        )

    print("Log Saved")


schedule.every(5).seconds.do(logger)


while True:

    schedule.run_pending()

    time.sleep(1)