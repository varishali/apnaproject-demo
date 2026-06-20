users = {
    "varish" : "1234",
    "ali" : "pass123"
}

print("=== LOGIN SYSTEM ===")

username = input("Enter Username : ")
password = input("Enter Password : ")

if username in users:
    if users[username] == password:
        print("Login Successful!")
    else:
        print("Wrong Password!")
else:
    print("Username Not Found!")            