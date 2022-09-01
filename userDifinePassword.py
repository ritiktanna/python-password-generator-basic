import random
from string import ascii_letters, ascii_lowercase, ascii_uppercase
import string
from tokenize import Special
from unicodedata import digit

# Creating list from which we can select password characters

alphabets = list(string.ascii_letters)
digit = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# Creating method that we can call to generate password


def generate_password():

    # asking for password length
    password_length = int(input('Enter Password Length:'))

    # We allow user to make max of 20 characters long password

    if password_length >= 20:
        print(
            f"Password length is {password_length} character long add less then 40")
        generate_password()

    # Checking that user input in not below zero

    elif password_length <= 0:
        print(
            f'Password length is {password_length},that is not valid!! Enter again')
        generate_password()

    alphabets_length = int(input('Enter alphabets Length:'))
    digits_length = int(input('Enter digits Length:'))
    special_characters_length = int(input('Enter special characters Length:'))

    input_character_length = alphabets_length + \
        digits_length+special_characters_length

    if password_length < input_character_length:
        print("Enter value is greter then password length!! Enter again")
        generate_password()

    password = []

    for i in range(alphabets_length):
        password.append(random.choice(alphabets))

    for i in range(digits_length):
        password.append(random.choice(digit))

    for i in range(special_characters_length):
        password.append(random.choice(special_characters))

    if password_length > input_character_length:
        random.shuffle(password)
        for i in range(password_length-input_character_length):
            password.append(random.choice(characters))
    random.shuffle(password)
    final_password =''
    final_password = final_password.join(password)
    print(final_password)

    user_input = input("Do you want to Generat again?(Y/N):").upper()

    if user_input == 'Y':
        generate_password()
    
    elif user_input == 'N':
        print(f"""
        ----------------------------------------
        Thank you for using Password Generator!!
        ----------------------------------------

        ****************************************
        Your Password is : {final_password}
        ****************************************
        """)
        


generate_password()
