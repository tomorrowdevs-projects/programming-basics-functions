import string
import random

def generate_password() -> str:
    """
    Generates a secure password using a combination of alphanumeric characters and symbols

    return: A secure password with user-defined length
    """
    # Ask the user to enter the desired password length and store it in a numeric variable.
    lenght = int(input("Enter the length of your password:\n"))

    """
    - Using a for loop, generate a random password of desired length.
    
    - Use a combination of alphanumeric characters and symbols to create a strong and secure password.
    
    - Store the generated password in a string type variable.
    """
    password = ''
    for character in [string.digits + string.ascii_letters + string.punctuation]:

        while lenght != 0:
            password += random.choice(character)
            lenght -= 1

    return password


# Using a function to hide the displayed password, print the generated password for the user to the screen.
def hide_password(password) -> str:
    """
    A function that allows to hide your password

    param password: Password containing various alphanumeric characters and symbols

    return: The password hidden by stars
    """
    new_password = ''

    for element in password:
        new_password += "*"

    return new_password


def main():
    password = generate_password()
    print(hide_password(password))

    # Ask the user whether it want to view the password or not
    show_password = input('Press 1 to show the password or enter to exit:\n')

    if show_password == "1":
        # print the result
        print(password)
    else:
        while show_password != '':
            show_password = input('Press 1 to show the password or enter to exit:\n')


if __name__ == '__main__':
    main()
