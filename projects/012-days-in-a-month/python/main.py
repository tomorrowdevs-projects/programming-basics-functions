def days_in_a_month(month,year):
    #--Defining general variables--#
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    month_days_leap=[31,29,31,30,31,30,31,31,30,31,30,31]

    #--Checking inputs--#
    if not type(year)==int or not type(month)==int:
        print('You have to insert an integer value year and month parameters')
        return
    
    if len(str(year))<4:
        print('Year parameter has to be 4 digits long')
        return
    
    if month<1 or month>12:
        print('Month parameter has to be between 1 and 12')
        return

    #--Checking if year is leap--#
    if year%400==0:
        leap_year=True
    elif year%100==0:
        leap_year=False
    elif year%4==0:
        leap_year=True
    else:
        leap_year=False
    
    #--Returning the number of days--#
    if leap_year:
        days_number=month_days_leap[month-1]
    else:
        days_number=month_days[month-1]
    
    return days_number

def main():
    year=input('Please, enter an integer of four digit for year:')
    month=input('Please, enter an integer between 1 and 12 for month:')
    year=int(year)
    month=int(month)
    day_number=days_in_a_month(month,year)
    print('The number of days of month {} of {} is {}:'.format(month,year,day_number))

if __name__=='__main__':
    main()