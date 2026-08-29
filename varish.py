import random
import string


def generate_password(length=12, include_symbols=True):
    # Characters defined
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if include_symbols else ""

    # Ensure password has at least one of each character set
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(digits),
    ]

    if include_symbols:
        password.append(random.choice(symbols))

    # Fill remaining length with random choices from all pool
    all_chars = letters + digits + symbols
    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))

    # Shuffle to remove any set patterns
    random.shuffle(password)
    return "".join(password)


# Example Usage
if __name__ == "__main__":
    new_password = generate_password(length=16, include_symbols=True)
    print(f"Generated Password: {new_password}")