# Shutil module
import shutil


# Time module
import time


while True:


    # Copy file
    shutil.copy(

        "data.txt",

        "backup_data.txt"
    )


    print("Backup Created")


    # Wait 10 seconds
    time.sleep(10)