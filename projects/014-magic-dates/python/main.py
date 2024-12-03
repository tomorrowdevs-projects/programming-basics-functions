def is_magic_date(day: int, month: int, year: int) -> bool:
    date=day*month
    two_digit_year=year%100
    if date==two_digit_year:
        return True
    else:
        return False

for year in range(1901,2001):
    for month in range(1,13):
        if month==4 or month==6 or month==9 or month==11:
            for day in range(1,31):
                if is_magic_date(day,month,year):
                    print(f"{day:02}-{month:02}-{year}")
        elif month==2:
            for day in range(1,29):
                if is_magic_date(day,month,year):
                    print(f"{day:02}-{month:02}-{year}")
        else:
            for day in range(1,32):
                if is_magic_date(day,month,year):
                    print(f"{day:02}-{month:02}-{year}")