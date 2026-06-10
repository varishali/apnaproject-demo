import random
import string

length = int(input("Enter Password Length: "))

password = "".join(
    random.choices(
        string.ascii_letters +
        string.digits +
        string.punctuation,
        k=length
    )
)

print("Password:", password)