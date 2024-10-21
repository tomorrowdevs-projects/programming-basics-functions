from datetime import datetime

def gregorian_to_ordinal_date(day,month,year):
    start_date=datetime(year,1,1)
    input_date=datetime(year,month,day)
    difference_date=input_date-start_date
    ordinal_number=difference_date.days+1
    ordinal_date=f"{year}-{ordinal_number:03}"
    return ordinal_date

def is_leap_year(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    else:
        return False

def main():
    is_valid_year=False
    while not(is_valid_year):
        input_year=input("Enter year of the date: ")
        if input_year.isnumeric() and int(input_year)>0:
            input_year=int(input_year)
            is_valid_year=True

    is_valid_month=False
    while not(is_valid_month):
        input_month=input("Enter month of the date: ")
        if input_month.isnumeric() and int(input_month)>0 and int(input_month)<13:
            input_month=int(input_month)
            is_valid_month=True

    is_valid_day=False
    while not(is_valid_day):
        input_day=input("Enter day of the date: ")
        if input_day.isnumeric():
            if input_month==2:
                if is_leap_year(input_year) and int(input_day)>0 and int(input_day)<30:
                    input_day=int(input_day) 
                    is_valid_day=True
                else:
                    if int(input_day)>0 and int(input_day)<29:
                        input_day=int(input_day) 
                        is_valid_day=True
            elif input_month==4 or input_month==6 or input_month==9 or input_month==11:
                if int(input_day)>0 and int(input_day)<31:
                    input_day=int(input_day)
                    is_valid_day=True
            else:
                if int(input_day)>0 and int(input_day)<32:
                    input_day=int(input_day)
                    is_valid_day=True

    ordinal_date=gregorian_to_ordinal_date(input_day,input_month,input_year)
    print(f"{input_year}-{input_month:02}-{input_day:02} = {ordinal_date:03}")

if __name__=="__main__":
    main()