import random

def  random_password():
    password_length=random.randint(7,10)
    random_password=""

    for i in range(password_length):
        character=chr(random.randint(33,126))
        random_password+=character

    return random_password

print(f"The randomly generated password is: {random_password()}")