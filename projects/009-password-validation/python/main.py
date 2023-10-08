def password_validation(password):
        if len(password) < 8:
            check_len = False
        else:
            check_len = True
        check_digit = any(chr.isdigit() for chr in password)
        check_lower = any(chr.islower() for chr in password)
        check_upper = any(chr.isupper() for chr in password)
        if check_digit and check_lower and check_upper and check_len:
            return True
        else:
            return False
            

def main():
    password = input("Enter a password: ")
    print(password_validation(password))


if __name__ == '__main__':
    main()

