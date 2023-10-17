def is_leap_year(year):
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
        

def feb_days(year):
    if is_leap_year(year) == True:
        return 29
    else:
        return 28


def days_in_a_month(month, year):
    month_days = [31, feb_days(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= month <= 12:
        return month_days[month - 1]


def main():
    year = input("Please enter a year (YYYY format): ")
    while len(year) < 4:
        print('Error. Year must be a four-digit input. ')
        year = input("Please enter a year (YYYY format): ")
    else:
        month = int(input('Please enter a month (1-12): '))
        if month < 1 or month > 12:
            print('Error. Entered invalid month.')
        else:
            days_in_month = days_in_a_month(month, year)
            print(f'Days in month {month}: {days_in_month}')


if __name__ == '__main__':
    main()


