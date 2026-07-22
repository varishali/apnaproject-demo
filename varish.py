from colorama import Fore, Style, init
import time
import os

init(autoreset=True)

os.system("cls" if os.name == "nt" else "clear")

name = input(Fore.CYAN + " Enter Her Name: ")

print(Fore.YELLOW + "\nLoading Your Surprise", end="")

for i in range(8):
    print(Fore.MAGENTA + " ", end="", flush=True)
    time.sleep(0.3)

print("\n")

messages = [
    (Fore.RED, f" Dear {name},"),
    (Fore.GREEN, " Tum meri life ka sabse beautiful part ho."),
    (Fore.YELLOW, " Tumhari smile meri favourite cheez hai."),
    (Fore.BLUE, " Har din tumhare saath aur bhi special lagta hai."),
    (Fore.MAGENTA, " Thank You meri life me aane ke liye."),
    (Fore.CYAN, " I Love You So Much "),
]

for color, msg in messages:
    print(color + Style.BRIGHT + msg)
    time.sleep(2)

heart = [
"      ❤❤❤     ❤❤❤",
"    ❤     ❤ ❤     ❤",
"   ❤       ❤       ❤",
"   ❤               ❤",
"    ❤             ❤",
"      ❤         ❤",
"        ❤     ❤",
"          ❤ ❤",
"           ❤"
]

colors = [
    Fore.RED, Fore.YELLOW, Fore.GREEN,
    Fore.CYAN, Fore.BLUE, Fore.MAGENTA
]

print()

for i, line in enumerate(heart):
    print(colors[i % len(colors)] + Style.BRIGHT + line)
    time.sleep(0.3)

print(Fore.RED + Style.BRIGHT + f"\n {name}, You Are My Happiness ")
print(Fore.YELLOW + " Forever Together ")
print(Fore.MAGENTA + " Made With Love By Varish Ali ")