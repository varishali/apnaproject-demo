password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(not char.isalnum() for char in password):
    score += 1

if score == 4:
    print("Strong Password 💪")
elif score >= 2:
    print("Medium Password 👍")
else:
    print("Weak Password ❌")