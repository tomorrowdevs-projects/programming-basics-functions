def is_valid_password(password):
    has_least_eight_characters=True
    if len(password)>7:    
        for character in password:
            if ord(character)<33 or ord(character)>126:
                has_least_eight_characters=False
    else:
        return False
    if has_least_eight_characters:
        
        has_least_one_uppercase=False
        index=0
        while not(has_least_one_uppercase) and index<len(password):
            character=password[index]
            if ord(character)>64 and ord(character)<91:
                has_least_one_uppercase=True
            index+=1

        has_least_one_lowercase=False
        index=0
        while not(has_least_one_lowercase) and index<len(password):
            character=password[index]
            if ord(character)>96 and ord(character)<123:
                has_least_one_lowercase=True
            index+=1

        has_least_one_number=False
        index=0
        while not(has_least_one_number) and index<len(password):
            character=password[index]
            if ord(character)>47 and ord(character)<58:
                has_least_one_number=True
            index+=1

        if has_least_one_uppercase and has_least_one_lowercase and has_least_one_number:
            return True
        else:
            return False
    else:
        return False

def main():
    password=input("Enter a password: ")
    result=is_valid_password(password)

    if result==True:
        print("The entered password is valid.")
    else:
        print("The entered password is not valid.")

if __name__=="__main__":
    main()