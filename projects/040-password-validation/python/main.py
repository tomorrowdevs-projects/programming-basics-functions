import string
def password_validation(password):
    valid_upper = False
    valid_lower = False
    valid_digit = False

    if len(password) >= 8:
        for character in password:
            if character in string.ascii_uppercase:
                valid_upper = True
            elif character in string.ascii_lowercase:
                valid_lower = True
            elif character in string.digits:
                valid_digit = True

    return valid_upper and valid_lower and valid_digit

# Include a main program that reads a password from the user and reports whether it is good.
def main():
    user_password = input('Enter password:\n')
    check_password = password_validation(user_password)
    print(check_password)
# Ensure that your main program only runs when your solution has not been imported into another file.
if __name__ == '__main__':
    main()
