def random_password():
    # generates a random number between 7 and 10 as password's length and declare a varaible where store it
    import random

    password_length = random.randint(7,10)

    password = ''

    # for loop that iterates many times as the password's length, generates a random number between 33 and 126 and convert it in a unicode character through chr(), then adds it to a variable to obtain the desired result
    for character in range(0,password_length + 1):
        ascii_number = random.randint(33,126)
        unicode_character = chr(ascii_number)
        password += unicode_character

    return password


def main():
    print(random_password())

main()

