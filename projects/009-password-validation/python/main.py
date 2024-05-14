def is_valid_password(password):
    #--Checking password lenght--#
    if len(password)<8:
        return False

    #--Checking digit quantity--#
    digit_counter=0
    for i in password:
        if i.isdecimal():
            digit_counter+=1
    if digit_counter==0:
        return False

    #--Checking uppercase and lowercase quantity--#
    upper_counter=0
    lower_counter=0
    for i in password:
        if i.isupper():
            upper_counter+=1
        elif i.islower():
            lower_counter+=1
    if upper_counter==0 or lower_counter==0:
        return False

    return True

def main():
    password=input('Please, enter a password of a minimum lenght of 8, at least an uppercase, a lowercase character and a digit:')
    if is_valid_password(password):
        print('The password is good')
    else:
        print('The password is not good')

if __name__=='__main__':
    main()

