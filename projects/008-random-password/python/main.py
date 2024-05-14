from random import randint

def random_password():
    pass_len=randint(7,10)
    password=[]
    for i in range(pass_len+1):
        password.append(chr(randint(33,126)))
    password=''.join(password)
    return password

def main():
    password=random_password()
    print('Here\'s your new password: {}'.format(password))

if __name__=='__main__':
    main()
