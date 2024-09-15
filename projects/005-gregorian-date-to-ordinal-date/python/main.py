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
    if year % 400 == 0:

    elif IntYear % 100 != 0 and IntYear % 4 == 0:


day = int(input("Please input a day in integers: "))
month = int(input("Please input a month in integers: "))
year = int(input("Please input a year in integers: "))