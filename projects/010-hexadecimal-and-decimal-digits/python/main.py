'''
Write two functions, hex2int and int2hex, that convert between hexadecimal digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and decimal (base 10) integers.
The hex2int function is responsible for converting a string containing a single hexadecimal digit to a base 10 integer.
The int2hex function is responsible for converting an integer between 0 and 15 to a single hexadecimal digit.
Each function will take the value to convert as its only parameter and return the converted value as its only result.
Ensure that the hex2int function works correctly for both uppercase and lowercase letters.
Your functions should display a meaningful error message and end the program if the parameter’s value is outside the expected range.
'''

def hex2int(initialvalue):
    convertedvalue = int(initialvalue, 16)
    return convertedvalue

def int2hex(initialvalue):
    newvalue = int(initialvalue)
    convertedvalue = hex(newvalue)
    return convertedvalue
   
initialvalue = input("Please insert a value: ")
question = input("In which base do you want to convert the precedent string? (hex/dec)")
if question == "hex":
    finalvalue = int2hex(initialvalue)
    print("The initial value converted into hexadecimal is: ", finalvalue)
else:
    finalvalue = hex2int(initialvalue)
    print("The initial value converted into decimal is: ", finalvalue)