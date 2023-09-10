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

p = password_validation('cC11111111')
print(p)

