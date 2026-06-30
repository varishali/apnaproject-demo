import shutil
from datetime import datetime

time = datetime.now().strftime(
    "%Y-%m-%d__%H-%M-%S"
)
backup = f"backup_{time}.txt"

shutil.copy(
    "TextFiles/log.txt",
    backup
)
print("Backup Created")