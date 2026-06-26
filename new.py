import os

class SafeFileUpdater:
    def __init__(self, filename): self.filename = filename
    def __enter__(self):
        self.temp_filename = self.filename + ".tmp"
        self.file = open(self.temp_filename, "w")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is None: os.replace(self.temp_filename, self.filename)
        else: os.remove(self.temp_filename)
