import re
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "=" * 45)
print(Fore.YELLOW + Style.BRIGHT + "   PASSWORD STRENGTH CHECKER")
print(Fore.CYAN + "=" * 45)

password = input(Fore.GREEN + "\nEnter Password: ")

score = 0

if len(password) >= 8:
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[a-z]", password):
    score += 1
if re.search(r"\d", password):
    score += 1
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print()

if score == 5:
    print(Fore.GREEN + "🟢 Password Strength: VERY STRONG")
elif score == 4:
    print(Fore.CYAN + "🔵 Password Strength: STRONG")
elif score == 3:
    print(Fore.YELLOW + "🟡 Password Strength: MEDIUM")
elif score == 2:
    print(Fore.MAGENTA + "🟠 Password Strength: WEAK")
else:
    print(Fore.RED + "🔴 Password Strength: VERY WEAK")

print(Fore.CYAN + "\nPassword Analysis")
print("-" * 30)
print("✔ Length >= 8 :", len(password) >= 8)
print("✔ Uppercase   :", bool(re.search(r"[A-Z]", password)))
print("✔ Lowercase   :", bool(re.search(r"[a-z]", password)))
print("✔ Number      :", bool(re.search(r"\d", password)))
print("✔ Special Char:", bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)))