import schedule
import time
import shutil

def backup():
    shutil.copy(
        "backup.txt",
        "autobackup.txt"
    )

    print("Backup Created")
schedule.every(3).seconds.do(backup)    
while True:
    schedule.run_pending()
    time.sleep(1)