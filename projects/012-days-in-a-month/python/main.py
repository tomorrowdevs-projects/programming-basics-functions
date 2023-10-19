# defines a function that takes month and year as parameter and return how many days has that month.
def days_in_a_month(month,year):

# return an error message if year isn't a 4 digit number
    if len(str(year)) < 4:
        return('Error, the year must have a 4-digit length')
    
# return an error message if month isn't between 1 and 12
    if month > 12 or month < 1:
        return('Error, the month must be between 1 and 12')
    
# determinates if year is or not a leap year
    if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
        leap_year = True
    else:
        leap_year = False

# determinates days in month and returns it
    if month == 2 and leap_year == True:
        days = 29
    elif month == 2 and leap_year == False:
        days = 28
    elif month <= 7 and not month % 2 == 0 or month > 7 and month % 2 == 0:
        days = 31
    else: 
        days = 30

    return days

# main function that asks to user a day and a month, then with the fuction above print how many days has the month to screen
def main():
    user_month = int(input('Enter a month: '))
    user_year = int(input('Enter a year: '))

    print(days_in_a_month(user_month,user_year))


main()