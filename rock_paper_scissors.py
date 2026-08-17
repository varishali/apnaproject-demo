import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1

    levels = {1: "Bahut Kamzor", 2: "Kamzor", 3: "Theek Thaak", 4: "Strong", 5: "Bahut Strong"}
    return levels.get(score, "Bahut Kamzor")

def main():
    print("1. Naya Password Generate Karo")
    print("2. Apne Password ki Strength Check Karo")
    choice = input("Choose karein (1/2): ")

    if choice == "1":
        length = int(input("Password ki length daaliye: "))
        pwd = generate_password(length)
        print(f"Generated Password: {pwd}")
        print(f"Strength: {check_strength(pwd)}")
    elif choice == "2":
        pwd = input("Apna password daaliye: ")
        print(f"Strength: {check_strength(pwd)}")
    else:
        print("Galat choice!")

main()