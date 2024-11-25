'''
Write a program that allows the user to convert a number from one base to another.
Your program should support bases between 2 and 16 for both the input number and the result number.

If the user chooses a base outside of this range then an appropriate error message should be displayed and the program should exit.

Divide your program into several functions:

a function named arbitrary to base 10 that converts from an arbitrary base to base 10
a function that base 10 to arbitrary base converts from base 10 to an arbitrary base
a main program that reads the bases and input number from the user
'''

def arbitrary(usernumber, userbase):
    if userbase == "2":
        convertedvalue = int(usernumber, 2)
        return convertedvalue
    elif userbase == "8":
        convertedvalue = int(usernumber, 8)
        return convertedvalue
    elif userbase == "16":
        convertedvalue = int(usernumber, 16)
        return convertedvalue
    else:
        return userbase
       
def arbitrary_base_converts(convertedvalue, basechoice):
    if basechoice == "10":
        return convertedvalue
    elif basechoice == "2":
        newvalue = bin(convertedvalue)
        return newvalue
    elif basechoice == "8":
        newvalue = oct(convertedvalue)
        return newvalue
    elif basechoice == "16":
        newvalue = hex(convertedvalue)
        return newvalue

usernumber = int(input(("Please insert number: "))
userbase = int(input("Please insert the base of the number: "))
convertedvalue = arbitrary(usernumber, userbase)
basechoice = int(input("Please choose a base to convert the number into from 2, 8, 10, 16: "))
finalvalue = arbitrary_base_converts(convertedvalue, basechoice)
print("Here's the number converted: ", finalvalue)