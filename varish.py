import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"

    all_chars = lower + upper + digits + symbols

    password = ""

    password += random.choice(lower)
    password += random.choice(upper)
    password += random.choice(digits)
    password += random.choice(symbols)

    for _ in range(length - 4):
        password += random.choice(all_chars)

    password = list(password)
    random.shuffle(password)

    return "".join(password)

print("=" * 35)
print(" RANDOM PASSWORD GENERATOR ")
print("=" * 35)

while True:
    try:
        length = int(input("Enter password length (8-30): "))

        if length < 8:
            print("Password must be at least 8 characters.\n")
            continue

        print("\nGenerated Password:")
        print(generate_password(length))

        again = input("\nGenerate another? (y/n): ").lower()

        if again != "y":
            print("Thank You!")
            break

    except ValueError:
        print("Please enter a valid number.\n")