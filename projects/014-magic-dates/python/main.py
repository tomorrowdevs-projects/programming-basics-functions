
def is_magic_date(day, month, year):

    day_per_month = day * month

    if str(year)[-2:] == str(day_per_month) or str(year)[-2] == '0' and str(year)[-1] == str(day_per_month):
        return True




def main():
    leap_year = None

    result = ''
    for year in range(1900,2001):
        if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
            leap_year = True
        else:
            leap_year == False
        for month in range(1,13):
            if month == 2 and leap_year == True:
                for day in range(1,30):
                    if is_magic_date(day, month, year):
                        result += f'{day} - {month} - {year}\n' 
            elif month == 2 and leap_year == False:
                for day in range(1,29):
                    if is_magic_date(day, month, year):
                        result += f'{day} - {month} - {year}\n'   
            elif 0 < month <= 7 and month % 2 != 0:
                for day in range(1,32):
                    if is_magic_date(day, month, year):
                        result += f'{day} - {month} - {year}\n'
            elif 8 <= month <= 12 and month % 2 == 0:
                for day in range(1,32):
                    if is_magic_date(day, month, year):
                        result += f'{day} - {month} - {year}\n'
            elif 0 < month <= 7 and month % 2 == 0:
                for day in range(1,31):
                    if is_magic_date(day, month, year):
                        result += f'{day} - {month} - {year}\n'
            elif 8 <= month <= 12 and month % 2 != 0:
                for day in range(1,31):
                    if is_magic_date(day, month, year):
                        result += f'{day} - {month} - {year}\n'
    print(result)
    

main()