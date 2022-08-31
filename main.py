import random
from string import ascii_letters
import string

def password():
    characters = ascii_letters + string.digits + "!@#$%^&*()"
    password_length = int(input("Enter password length: "))
    #empty list to store password
    pass_store = []
    #choose password from all_char
    for i in range(password_length):
        pass_store.append(random.choice(characters))
    #shuffle again to make it more random
    random.shuffle(pass_store)
    #join list with space
    print("".join(pass_store))

#calling method to create password
password()