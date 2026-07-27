import csv
import os

FILE = "passwords.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Website", "Username", "Password"])

def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([website, username, password])

    print("Password Saved Successfully!")

def view_passwords():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def search_password():
    website = input("Enter Website: ")
    found = False

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if row[0].lower() == website.lower():
                print("\nWebsite :", row[0])
                print("Username:", row[1])
                print("Password:", row[2])
                found = True

    if not found:
        print("No Record Found!")

def delete_password():
    website = input("Website to Delete: ")

    rows = []

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)

        for row in rows:
            if row and row[0].lower() != website.lower():
                writer.writerow(row)

    print("Deleted Successfully!")

while True:
    print("\n===== Smart Password Vault =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        delete_password()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")