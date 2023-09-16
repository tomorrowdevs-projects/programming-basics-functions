def is_it_a_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def date(month, year):
    leap_year = is_it_a_leap_year(year)

    if leap_year == True: #366 days
            if month < 8 and month % 2 != 0:
                days = 31
            elif month >= 8 and month % 2 == 0:
                days = 31
            elif month == 2:
                days = 29
            else:
                days = 30

    else: #365 days
            if month < 8 and month % 2 != 0:
                days = 31
            elif month >= 8 and month % 2 == 0:
                days = 31
            elif month == 2:
                days = 28
            else:
                days = 30

    return days

def days_in_a_month():
    month = int(input("Enter a month as a digit between 1 and 12:\n"))
    year = int(input("Enter an year as a 4 digit:\n"))

    return (f'{date(month, year)} days')