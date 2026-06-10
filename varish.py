import os

files = os.listdir()

count = 1

for file in files:

    if file.endswith(".txt"):

        os.rename(file, f"file_{count}.txt")

        count += 1

print("Files Renamed Successfully!")