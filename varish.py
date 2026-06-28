import shutil 
from datetime import datetime

class BackupSystem:
    def __init__(self,original_backup):
        self.original_file = original_backup

    def create_backup(self):
        time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = f"backup_{time}.txt"    

        shutil.copy(self.original_file,backup_file)
        print("Backup Created : ",backup_file)

backup = BackupSystem("log.txt")
backup.create_backup()        