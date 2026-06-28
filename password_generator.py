import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    required = []

    if use_uppercase:
        characters += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        characters += string.digits
        required.append(random.choice(string.digits))
    if use_symbols:
        characters += string.punctuation
        required.append(random.choice(string.punctuation))

    if length < len(required) + 1:
        length = len(required) + 1

    remaining = [random.choice(characters) for _ in range(length - len(required))]
    password_list = required + remaining
    random.shuffle(password_list)
    return ''.join(password_list)


def main():
    print("=" * 40)
    print("       Python Password Generator")
    print("=" * 40)

    try:
        length = int(input("Enter password length (default 12): ") or 12)
        if length < 4:
            print("Minimum length is 4. Setting to 4.")
            length = 4
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    uppercase = input("Include uppercase letters? (y/n, default y): ").strip().lower() != 'n'
    digits    = input("Include digits?           (y/n, default y): ").strip().lower() != 'n'
    symbols   = input("Include symbols?          (y/n, default y): ").strip().lower() != 'n'

    try:
        count = int(input("How many passwords to generate? (default 1): ") or 1)
    except ValueError:
        count = 1

    print("\n" + "-" * 40)
    print(f"Generated Password{'s' if count > 1 else ''}:")
    print("-" * 40)
    for i in range(count):
        pwd = generate_password(length, uppercase, digits, symbols)
        print(f"  {i+1}. {pwd}")
    print("-" * 40)


if __name__ == "__main__":
    main()
