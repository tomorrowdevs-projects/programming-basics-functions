def is_magic_date(day,month,year):
    year_digit=int(str(year)[2:])
    if day*month==year_digit:
        return True
    else:
        return False

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
    magic_dates=[]
    years=range(1900,2000)
    months=range(1,13)
    for year in years:
        for month in months:
            last_day=days_in_a_month(month,year)
            days=range(1,last_day)
            for day in days:
                if is_magic_date(day,month,year):
                    date='{:02}/{:02}/{}'.format(day,month,year)
                    magic_dates.append(date)
    print('\n'.join(magic_dates))

if __name__=='__main__':
    main()