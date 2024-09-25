'''
Many people do not use capital letters correctly, especially when typing on small devices like smartphones.
To help address this situation, you will create a function named capitalize it that takes a string as its only parameter and returns a new copy of the string that has been correctly capitalized.

In particular, your function must:

Capitalize the first non-space character in the string,
Capitalize the first non-space character after a period, exclamation mark or question mark,
Capitalize a lowercase “i” if it is preceded by a space and followed by a space, period, exclamation mark, question mark or apostrophe.
Implementing these transformations will correct most capitalization errors.

Example:
input:
“what time do I have to be there? what’s the address? this time I’ll try to be on time!”
output:
“What time do I have to be there? What’s the address? This time I’ll try to be on time!”.

Include a main program that reads a string from the user, capitalizes it using your function, and displays the result.
'''

def capitalize_it(string):
    array = list(string)
    newarray = []
    newarray.append(array[0].upper())
    del array[0]
    for letter in array:
        if letter == "." "!" "?":
            nextletter =
            newarray.append(nextletter.upper())
        elif letter == "i":
            newarray.append(letter.upper())
        else:
            newarray.append(letter)
    return newarray
   
string = str(input("Please insert a string without capitalizing anything: "))
capitalizedstring = capitalize_it(string)
print("The correct string is: ", capitalizedstring)