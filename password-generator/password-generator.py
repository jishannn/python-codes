import random
import string

def generated_password(length, use_special_chars=False, use_numbers=True, use_uppercase=True):
    char_pool = string.ascii_lowercase       # Always include lowercase letters

    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_numbers:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation

    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


# Input from user
length = int(input('Enter password length: '))
use_special_chars = input('Include special characters? (yes/no): ').lower() == 'yes'
use_numbers = input('Include numbers? (yes/no): ').lower() == 'yes'
use_uppercase = input('Include uppercase letters? (yes/no): ').lower() == 'yes'

# Generate and display password
password = generated_password(length, use_special_chars, use_numbers, use_uppercase)
print(f'Generated Password: {password}')

