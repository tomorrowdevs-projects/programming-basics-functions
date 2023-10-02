def is_it_a_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
def magic_dates():
    year = 1900
    month_of_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    result = []

    while year != 1999:
        year += 1

        for month in range(1, 13):

            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:

                for day in range(1, 32):
                    magic_dates = day * month
                    if magic_dates == (year - 1900):
                        result.append(f"{day}-{month_of_year[month - 1]}-{year}")

            elif month == 2:

                if is_it_a_leap_year(year):
                    for day in range(1, 30):
                        magic_dates = day * month
                        if magic_dates == (year - 1900):
                            result.append(f"{day}-{month_of_year[month - 1]}-{year}")

                else:

                    for day in range(1, 29):
                        magic_dates = day * month
                        if magic_dates == (year - 1900):
                            result.append(f"{day}-{month_of_year[month - 1]}-{year}")

            else:

                for day in range(1, 31):
                    magic_dates = day * month
                    if magic_dates == (year - 1900):
                        result.append(f"{day}-{month_of_year[month - 1]}-{year}")

    return ';\n'.join(result)

def main():
    magic_dates_list = magic_dates()
    print(f'Here all of the magic dates in the 20th century:\n{magic_dates_list}')

if __name__ == '__main__':
    main()
