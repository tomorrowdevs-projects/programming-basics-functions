
def gregorian_to_ordinal_date(day: int,month: int,year: int)-> int:
    '''Returns the ordinal day gived a gregorian date. 
            :parameters: 
                    day(int): a integer for the day.
                    month(int): a integer for the month.
                    year: a integer for the year. 
            :return:
                    ordinal date(int): the corresponding ordinal day.  
    '''
    
    if year % 400 == 0:
        leap_year = True
    elif year % 400 != 0 and year % 100 != 0 and year % 4 == 0:
        leap_year = True
    else:
        leap_year = False

    # checks whether the date is real or not
    if (day > 28 and month == 2 and leap_year == False) or (day > 29 and month == 2 and leap_year == True) or (day > 31 and (1 <= month <= 7 and month % 2 != 0)) or (day > 31 and (7 < month <= 12 and month % 2 == 0)) or (day > 30 and (1 <= month <= 7 and month % 2 == 0)) or  (day > 30 and (7 < month <= 12 and month % 2 != 0)) or  month > 12 or month < 1 :
        return 'invalid date'
    else:    
        ordinal_day = 0

    # loop that adds month by month days into a variable to get the ordinal day.
        if month == 1:
            ordinal_day = day
        else:
            for i in range(1, month):
                if i == 2 and leap_year == True: 
                    ordinal_day += 29
                elif i == 2 and leap_year == False:
                    ordinal_day += 28 
                elif 1 <= i <= 7 and i % 2 != 0:
                    ordinal_day += 31
                elif 7 < i <= 12 and i % 2 == 0:
                    ordinal_day += 31
                elif 1 <= i <= 7 and i % 2 == 0:
                    ordinal_day += 30
                elif 7 < i <= 12 and i % 2 != 0:
                    ordinal_day += 30
            ordinal_day += day

        return ordinal_day

def main():
    '''Asks a gregorian date and prints the corresponding ordinal day'''    
    user_day = int(input('Enter a day (as integer): '))
    user_month = int(input('Enter a month (as integer): '))
    user_year = int(input('Enter a year (as integer): '))
    print(f'Ordinal day: {gregorian_to_ordinal_date(user_day,user_month,user_year)}')


#runs the program only if file has not been imported
if __name__ == "__main__":
    main()