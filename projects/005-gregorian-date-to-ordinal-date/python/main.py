'''
An ordinal date consists of a year and a day within it, both of which are integers.   
The year can be any year in the Gregorian calendar while the day within the year ranges from one, 
which represents January 1, through to 365 (or 366 if the year is a leap year) which represents December 31. 

Ordinal dates are convenient when computing differences between dates that are a 
specific number of days(rather than months).    
For example, ordinal dates can be used to easily determine whether a customer is within a 90-day return period, 
the sell-by date for a food-product based on its production date, and the due date for a baby.

Write a function named **gregorian_to_ordinal_date** that takes three **integers** as parameters:
- day
- month
- year

The function should return the day within the year for that date as its only result.   

Create a main program that reads a day, month and year from the user and displays the day within the year for that date.    
Also, your program must also consider the leap year.  
Your main program should only run when your file has not been imported into another program.
'''

def gregorian_to_ordinal_date(day, month, year):
    if year % 400 ==  0 and year % 100 == 0:
        totaldays = 366
    elif year % 100 != 0 and year % 4 == 0:
        totaldays = 366
    else: totaldays = 365
    
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        totaldaysmonth = month * 31
    elif month == 4 or 6 or 9 or 11:
        totaldaysmonth = month * 30
    elif month == 2:
        if totaldays == 365:
            totaldaysmonth = month * 28
        else:
            totaldaysmonth = month * 29

    finalresult = (totaldays - totaldaysmonth) - day
    return finalresult

day = int(input("Please input a day in integers: "))
month = int(input("Please input a month in integers: "))
year = int(input("Please input a year in integers: "))
finalresult = gregorian_to_ordinal_date(day, month, year)
print("The result is: ", finalresult)