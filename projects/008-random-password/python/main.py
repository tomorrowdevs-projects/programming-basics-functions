import random

def random_psw():
    gen_password = ''
    password_len = random.randrange(7,11)
    for num in range(password_len):
        gen_char = random.randint(33, 126)
        gen_password += chr(gen_char)
    return gen_password


def main():
    print(random_psw())


if __name__ == '__main__':
    main()