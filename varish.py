import os
import shutil

# Folder path
path = input("Enter Folder Path: ")

if not os.path.exists(path):
    print("Folder not found!")
    exit()

# Categories
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".cpp", ".c", ".html", ".css", ".js"],
    "Archives": [".zip", ".rar", ".7z"],
    "Others": []
}

for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isdir(file_path):
        continue

    ext = os.path.splitext(file)[1].lower()
    moved = False

    for folder, extensions in folders.items():
        if ext in extensions:
            folder_path = os.path.join(path, folder)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f" {file} -> {folder}")
            moved = True
            break

    if not moved:
        folder_path = os.path.join(path, "Others")
        os.makedirs(folder_path, exist_ok=True)
        shutil.move(file_path, os.path.join(folder_path, file))
        print(f" {file} -> Others")

print("\nFile organization completed successfully!")