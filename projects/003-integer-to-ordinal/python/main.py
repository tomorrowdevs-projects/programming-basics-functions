'''
Words like *first*, *second* and *third* are referred to as ordinal numbers. 

Write a function named **integer to ordinal** that: 
- takes an integer as its only parameter, between 1 and 12 (inclusive). 
- returns a string containing the appropriate English ordinal number as its only result.    

It should return an empty string if the function is called with an argument outside of this range. 

Include a main program that demonstrates your function by displaying each integer from 1 to 12 and its ordinal number.    
Your main program should only run when your file has not been imported into another program.
'''

def integer_to_ordinal(intnumber):

    if intnumber == 1:
        englishresult = "First1"
    elif intnumber == 2:
        englishresult = "Second"
    elif intnumber == 3:
        englishresult = "Third"
    elif intnumber == 4:
        englishresult = "Fourth"
    elif intnumber == 5:
        englishresult = "Fifth"
    elif intnumber == 6:
        englishresult = "Sixth"
    elif intnumber == 7:
        englishresult = "Seventh"
    elif intnumber == 8:
        englishresult = "Eighth"
    elif intnumber == 9:
        englishresult = "Ninenth"
    elif intnumber == 10:
        englishresult = "Tenth"
    elif intnumber == 11:
        englishresult = "Eleventh"
    elif intnumber == 12:
        englishresult = "Twelveth"
    elif intnumber < 1 & intnumber > 12:
        englishresult = " "

    return englishresult

intnumber = int(input("Please input a number from 1 to 12: "))
finalresult = integer_to_ordinal(intnumber)
print("Ordinal number input in english: ", finalresult)