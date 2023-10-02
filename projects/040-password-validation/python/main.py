
def password_validation(password):
# declares a variable for every characteristic of a good password with a false value
    length = False

    upper_case_character = False

    lower_case_character = False

    number = False

# checks the length of password   
    if len(password) >= 8:
        length = True
# for loop that iterates through password and check if there is a number, a lowercase and a uppercase character updating relatives variables
    for character in password:
        if character.isupper():
            upper_case_character = True
        if character.islower():
            lower_case_character = True
        if character.isnumeric():
            number = True

# canditional that checks if a password is good or not and return True or False
    if length == True and upper_case_character == True and lower_case_character == True and number == True:
        return  True
    else:
        return False


def main():
    password = input('Enter a password: ')
    result = password_validation(password)
    if result == True:
        print('Password ok')
    else:
        print('The password is weak')

if __name__ == '__main__':
    main()
    