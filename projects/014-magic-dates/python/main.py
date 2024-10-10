'''
A magic date is a date where the day multiplied by the month is equal to the two digit year.

For example, June 10, 1960 is a magic date because June is the sixth month, and 6 times 10 is 60, which is equal to the two digit year.

Write a function named is magic date that determines whether a date is a magic date. Your function will take two parameters:

the day as integer
the month as an integer between 1 and 12
the year as a four digit integer And should return True if the date is a magic date otherwise it should return False.
Use your function to create a main program that finds and displays all the magic dates in the 20th century.
'''

def magic_date(userday, usermonth, useryear):
    magicdaymonth = userday * usermonth
    trueyear = useryear % 100
    if magicdaymonth < 100:
        if magicdaymonth == trueyear:
            print("The date it's a magic date!")
        else:
            print("The date it's NOT a magic date!")
    else:
        print("Error: the sum of the integer inserted ")
   
userday = int(input("Please insert day of the month as integer: "))
usermonth = int(input("Please insert a month as integer: "))
useryear = int(input("Please insert a year as a 4-digit integer: "))
finalresult = magic_date(userday, usermonth, useryear)