import random
import string

urls = {}

while True:

    print("\n===== URL Shortener =====")
    print("1. Shorten URL")
    print("2. View URLs")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        long_url = input("Enter Long URL: ")

        short_code = ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=6
            )
        )

        urls[short_code] = long_url

        print("\nShort URL:")
        print(f"https://short.ly/{short_code}")

    elif choice == "2":

        if len(urls) == 0:
            print("No URLs Found!")

        else:

            print("\nSaved URLs:")

            for code, url in urls.items():
                print(f"{code} -> {url}")

    elif choice == "3":
        break

    else:
        print("Invalid Choice!")