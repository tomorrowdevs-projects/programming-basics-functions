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
    array = string.split()
    newarray = [array[0].capitalize()]
    #for index, letter in enumerate(array[1:]):
    for i in range(1,len(array)):
        #print(f"{array[i-1]=}")
        if array[i-1][-1] in [".", "!", "?"]: 
            newarray.append(array[i].capitalize())
        elif array[i] == "i":
            newarray.append(array[i].capitalize())
        elif array[i][0] == "i":
            if array[i][1] in [".", "!", "?", "'"]:
                newarray.append(array[i].capitalize())
        else:
            newarray.append(array[i])
    return " ".join(newarray)


def main():        
    string = "what time do i have to be there? what's the address? i'll be there i.ll in a minute"
    capitalizedstring = capitalize_it(string)
    print("The correct string is: ", capitalizedstring)


if __name__ == '__main__':
    main()