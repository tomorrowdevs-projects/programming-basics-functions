'''
Write a function named random password that generates a random
password.

The password should have a random length of between 7 and 10
characters.
Each character should be randomly selected from positions 33 to 126 in
the ASCII table.
Your function will not take any parameters.
It will return the randomly generated password as its only result.
Display the randomly generated password in your file’s main program.
'''

import random
import string

def random_password():
    for n in range(lenght):
        character = random.randrange(33,126)
        asciichar = ''.join([chr(character)])
        lista.append(asciichar)
    return lista

lista = []
lenght = random.randrange(7, 11)
listapassword = random_password()
passwordfinale = "".join(listapassword)
print("Password: ", passwordfinale)