import os

KEY = 25

def encrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) + KEY)
    return result

def decrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) - KEY)
    return result

def create_file():
    name = input("Enter file name: ") + ".txt"
    text = input("Enter secret message: ")

    with open(name, "w") as file:
        file.write(encrypt(text))

    print("File created and encrypted successfully.")

def read_file():
    name = input("Enter file name: ") + ".txt"

    if not os.path.exists(name):
        print("File not found.")
        return

    with open(name, "r") as file:
        data = file.read()

    print("\nDecrypted Message:")
    print(decrypt(data))

def list_files():
    files = [f for f in os.listdir() if f.endswith(".txt")]

    if not files:
        print("No text files found.")
    else:
        print("\nAvailable Files:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

while True:
    print("\n===== Secure File Locker =====")
    print("1. Create Secure File")
    print("2. Read Secure File")
    print("3. Show Files")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_file()

    elif choice == "2":
        read_file()

    elif choice == "3":
        list_files()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")