import random

def generate_username(first_name, last_name, include_numbers):
    if len(first_name) < 2 or len(last_name) < 2:
        return "Error: First name and Last name should have at least 2 letters."

    # Pick random characters from first and last name
    first_part = ''.join(random.choice(first_name) for _ in range(2))
    last_part = ''.join(random.choice(last_name) for _ in range(2))

    username = first_part + last_part

    # Add random number if user wants
    if include_numbers:
        username += str(random.randint(10, 99))

    return username


# User input
first_name = input('Enter your first name: ').strip().capitalize()
last_name = input('Enter your last name: ').strip().capitalize()
include_numbers = input('Include numbers? (yes/no): ').lower() == 'yes'


username = generate_username(first_name, last_name, include_numbers)
print(f'Generated Username: {username}')