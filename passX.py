from itertools import permutations
import random

def generate_passwords(first_name, middle_name, last_name, nickname, phone, dob, username):
    name_variants = [
        first_name, first_name.lower(), first_name.upper(), first_name.capitalize(),
        middle_name, middle_name.lower(), middle_name.upper(), middle_name.capitalize(),
        last_name, last_name.lower(), last_name.upper(), last_name.capitalize(),
        nickname, nickname.lower(), nickname.upper(), nickname.capitalize()
    ]
    
    phone_variants = [phone, phone[-4:], phone[:4]]
    dob_variants = [dob, dob.replace('-', ''), dob[-4:]]
    username_variants = [username, username.lower(), username.upper()]
    symbols = ['@', '#', '$', '%', '&', '*', '!', '?']
    numbers = ['123', '321', '007', '999', '2024', '777']

    base_words = name_variants + phone_variants + dob_variants + username_variants + numbers

    passwords = set()

    for i in range(2, 4):  # Generate combinations of length 2 and 3
        for combo in permutations(base_words, i):
            plain = ''.join(combo)
            passwords.add(plain)
            passwords.add('_'.join(combo))
            passwords.add('-'.join(combo))
            passwords.add(plain.capitalize())
            passwords.add(plain + random.choice(symbols))
            passwords.add(random.choice(symbols) + plain)
            passwords.add(plain[:3] + random.choice(symbols) + plain[3:])
            passwords.add(plain + random.choice(numbers))
            passwords.add(random.choice(numbers) + plain)

    return list(passwords)  # <-- This return must be inside the function

# Prompting user for input
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")
nickname = input("Enter your nickname: ")
phone = input("Enter your phone number: ")
dob = input("Enter your date of birth (YYYY-MM-DD): ")
username = input("Enter your username: ")

password_list = generate_passwords(first_name, middle_name, last_name, nickname, phone, dob, username)

# Save passwords to file
password_file = "passwords.txt"
with open(password_file, "w") as file:
    file.write("\n".join(password_list))

print(f"Total passwords generated: {len(password_list)}")
print(f"Passwords saved in {password_file}")
