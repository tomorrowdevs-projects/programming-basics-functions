from LeapYear import isleap

def ordinal_date(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap(year) == True:
        days_in_month[2] = 29

    new_days_in_month = days_in_month[:month + 1]
    new_days_in_month[-1] = day
    
    return sum(new_days_in_month)


def main():
    day = int(input('Please enter a day: '))
    month = int(input('Please enter a month: '))
    year = int(input('Please enter a year: '))
    day_within_year = ordinal_date(day, month, year)
    print(f'Day within the year for {day:02d}/{month:02d}/{year}: {day_within_year}')


if __name__ == '__main__':
    main()