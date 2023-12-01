
def gregorian_date_to_ordinal(day,month,year):

    if year % 400 == 0:
        leap_year = True
    elif year % 400 != 0 and year % 100 != 0 and year % 4 == 0:
        leap_year = True
    else:
        leap_year = False

    if (day > 28 and month == 2 and leap_year == False) or (day > 29 and month == 2 and leap_year == True) or (day > 31 and (1 <= month <= 7 and month % 2 != 0)) or (day > 31 and (7 < month <= 12 and month % 2 == 0)) or (day > 30 and (1 <= month <= 7 and month % 2 == 0)) or  (day > 30 and (7 < month <= 12 and month % 2 != 0)) or  month > 12 or month < 1 :
        return 'invalid date'
    else:    
        ordinal_day = 0

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
    
    user_day = int(input('Enter a day (as integer): '))
    user_month = int(input('Enter a month (as integer): '))
    user_year = int(input('Enter a year (as integer): '))
    print(f'Year: {user_year}\nOrdinal day: {gregorian_date_to_ordinal(user_day,user_month,user_year)}')

if __name__ == "__main__":
    main()