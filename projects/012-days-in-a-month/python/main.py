'''
Write a function called days in a month that determines how many days there are in a particular month.
Your function will take two parameters:

the month as an integer between 1 and 12
the year as a four digit integer
Ensure that your function reports the correct number of days in February for leap years. Include a main program that reads a month and year from the user and displays the number of days in that month.
'''

def days_in_a_month(usermonth, useryear):
    if useryear % 400 ==  0 and useryear % 100 == 0:
        totaldays = 366
    elif useryear % 100 != 0 and useryear % 4 == 0:
        totaldays = 366
    else: totaldays = 365
   
    if usermonth == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        daysinmonth = 31
        return daysinmonth
    elif usermonth == 4 or 6 or 9 or 11:
        daysinmonth = 30
        return daysinmonth
    elif usermonth == 2:
        if totaldays == 365:
            daysinmonth = 28
            return daysinmonth
        else:
            daysinmonth = 29
            return daysinmonth
   
usermonth = int(input("Please insert a month in integer: "))
useryear = int(input("Please insert a 4-digit year: "))
daysinmonth = days_in_a_month(usermonth, useryear)
print("The days in the month, and year, selected are: ", daysinmonth)