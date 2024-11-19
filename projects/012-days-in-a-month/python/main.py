def is_leap_year(year: int) -> bool:
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    else:
        return False
  
def days_in_a_month(month: int, year: int) -> int:
    if month==4 or month==6 or month==9 or month==11:
        days=30
    elif month==2:
        if is_leap_year(year):
            days=29
        else:
            days=28
    else:
        days=31
    return days


is_valid_input=False
while not(is_valid_input):
    try: 
        input_month=int(input("Enter a month (integer between 1 and 12): "))
        if input_month>=1 and input_month<=12:
            is_valid_input=True
    except ValueError:
        print("The integer you entered is not valid!")

is_valid_input=False
while not(is_valid_input):
    try: 
        input_year=int(input("Enter a year (four digit integer): "))
        if input_year>=1000 and input_year<=9999:
            is_valid_input=True
    except ValueError:
        print("The integer you entered is not valid!")

days=days_in_a_month(input_month, input_year)

print(f"{input_year}-{input_month:02} -> {days} days")