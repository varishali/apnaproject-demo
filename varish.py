import random
import string

def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
        )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def password_strength(password):
    score = 0
    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if len(password) >= 12:
        score += 1

    if score <= 2:
        return 'Weak'

    elif score == 3 or score == 4:
        return 'Medium'

    else:
        return 'Strong'
def main():
    print('=== Password Generator CLI ===')


while True:
    try:
        length = int(input('Enter password length (6-32): '))

        if 6 <= length <= 32:
            password = generate_password(length)

            print('\\nGenerated Password:')
            print(password)

            print('\\nStrength:')
            print(password_strength(password))

            again = input('\\nGenerate another password? (y/n): ').lower()

            if again != 'y':
                print('Goodbye!')
                break

        else:
            print('Please enter a number between 6 and 32.')

    except ValueError:
        print('Please enter a valid number.')


if __name__ == '__main__':
    main()
