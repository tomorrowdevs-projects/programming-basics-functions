def gregorian_to_ordinal_date(day,month,year):
    #--Defining general variables--#
    MonthDays_leap=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MonthDays=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #--Checking parameters--#
    if not (type(day)==int or type(month)==int or type(year)==int): #Parameters type check
        return
    
    #--Checking if year is leap--#
    if year%400==0:
        LeapYear=True
    elif year%100==0:
        LeapYear=False
    elif year%4==0:
        LeapYear=True
    else:
        LeapYear=False

    #--Checking for parameters correctness--#
    if month>12:
        return
    
    if LeapYear:
        if day>MonthDays_leap[month-1]:
            return
        
        OrdinalDate=day
        if LeapYear:
            for i in range(month-1):
                OrdinalDate+=MonthDays_leap[i]
        else:
            for i in range(month-1):
                OrdinalDate+=MonthDays[i]
        return OrdinalDate 
    else:
        if day>MonthDays[month-1]:
            return
        
        OrdinalDate=day
        if LeapYear:
            for i in range(month-1):
                OrdinalDate+=MonthDays_leap[i]
        else:
            for i in range(month-1):
                OrdinalDate+=MonthDays[i]
        return OrdinalDate

def main():
    year=input('Please, enter the year you are interested in (only integers):')
    while not year.isdecimal():
        year=input('Please, enter the year you are interested in (only integers):')
    year=int(year)

    month=input('Please, enter the month you are interested in (only integers between 1 and 12):')
    while not month.isdecimal():
        month=input('Please, enter the month you are interested in (only integers between 1 and 12):')
    month=int(month)

    day=input('Please, enter the day you are interested in (only integers):')
    while not day.isdecimal():
        day=input('Please, enter the day you are interested in (only integers):')
    day=int(day)

    OrdinalDate=gregorian_to_ordinal_date(day,month,year)
    if OrdinalDate==None:
        print('Please, check carefully your input data and retry')
    else:
        print('The ordinal date corresponding to {}/{:02d}/{} is: {}'.format(day,month,year,OrdinalDate))

if __name__=='__main__':
    main()