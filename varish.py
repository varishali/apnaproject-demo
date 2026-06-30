# File handling
import os

# Automatic scheduling
import schedule

# Time delay
import time

# Current time
from datetime import datetime


# Cleaner function
def clean_temp_files():

    # Current folder ki files
    files = os.listdir()


    # Har file check
    for file in files:


        # TMP file check
        if file.endswith(".tmp"):


            # File delete
            os.remove(file)


            print(file, "Deleted")


            # Log save
            with open(

                "cleaner_logs.txt",

                "a"
            ) as log:


                log.write(

                    f"{datetime.now()} -> {file} Deleted\n"
                )


# Every 10 seconds
schedule.every(10).seconds.do(clean_temp_files)


print("Cleaner Running...")


# Infinite loop
while True:


    # Scheduled tasks run
    schedule.run_pending()


    # CPU rest
    time.sleep(1)