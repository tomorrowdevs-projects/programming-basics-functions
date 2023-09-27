import random

def random_password():
    characters = []
    password_length = random.choice(range(7, 11))

    for character in range(33, 127):
        characters.append(str(chr(character)))
    return ''.join(random.choices(characters, k = password_length))

def main():
    password = random_password()
    print(password)

if __name__ == '__main__':
    main()
