import string
import random

def random_password():
    characters = string.ascii_letters + string.punctuation + string.digits
    password_length = random.choice(range(7, 11))

    return ''.join(random.choices(characters, k = password_length))