def is_it_a_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def ordinal_date(day, month, year):
    month -= 1
    leap_year = is_it_a_leap_year(year)
    day_within_the_year = day

    if leap_year == True: #366 days
        while month != 0:
            if month < 8 and month % 2 != 0:
                day_within_the_year += 31
            elif month >= 8 and month % 2 == 0:
                day_within_the_year += 31
            elif month == 2:
                day_within_the_year += 29
            else:
                day_within_the_year += 30

            month -= 1

    else: #365 days
        while month != 0:
            if month < 8 and month % 2 != 0:
                day_within_the_year += 31
            elif month >= 8 and month % 2 == 0:
                day_within_the_year += 31
            elif month == 2:
                day_within_the_year += 28
            else:
                day_within_the_year += 30

            month -= 1

    return day_within_the_year
