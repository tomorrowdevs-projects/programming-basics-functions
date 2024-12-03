def add_time(start_time: str, duration_time: str, day_week="") -> str:

    time,am_pm=start_time.split()

    start_hours,start_minutes=map(int, time.split(":"))
    if start_hours==12:
        start_hours=0

    duration_hours,duration_minutes=map(int, duration_time.split(":"))

    add_hours=start_hours+duration_hours
    add_minutes=start_minutes+duration_minutes

    if add_minutes>=60:
        add_hours+=add_minutes//60
        add_minutes%=60

    half_day=add_hours//12

    if add_hours>12:
        add_hours%=12

    if am_pm=="AM":
        if half_day%2==0:
            format_am_pm="AM"
        else:
            format_am_pm="PM"

    elif am_pm=="PM":
        if half_day%2==0:
            format_am_pm="PM"
        else:
            format_am_pm="AM"

    #If the result will be the next day, it should show (next day) after the time. 
    #If the result will be more than one day later, it should show (n days later) after the time, 
    #where "n" is the number of days later.

    if am_pm=="AM":
        if half_day==0 or half_day==1:
            n_days=0
            days_later=""
        elif half_day==2:
            n_days=1
            days_later="(next day)"
        else:
            if half_day%2==0:
                n_days=half_day//2
                days_later=f"({n_days} days later)"
            else:
                n_days=(half_day-1)//2
                days_later=f"({n_days} days later)"

    if am_pm=="PM":
        if half_day==0:
            n_days=0
            days_later=""
        elif half_day==1 or half_day==2:
            n_days=1
            days_later="(next day)"
        else:
            if half_day%2==0:
                n_days=half_day//2
                days_later=f"({n_days} days later)"
            else:
                n_days=(half_day+1)//2
                days_later=f"({n_days} days later)"

    if add_hours==0:
        add_hours=12
    
    #If the function is given the optional starting day of the week parameter, 
    #then the output should display the day of the week of the result.
    #The day of the week in the output should appear after the time and before the number of days later.
         
    days_of_week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    day_week=day_week.capitalize()
    if day_week in days_of_week:
        day_week=days_of_week[(days_of_week.index(day_week)+n_days)%7]
        day_week=f", {day_week.capitalize()}"
    else:
        day_week=""

    return f"{add_hours}:{add_minutes:02} {format_am_pm}{day_week} {days_later}"


start_time=input("Enter a start time in the 12-hour clock format (example 12:00 AM/PM): ")
duration_time=input("Enter a duration time (hh:mm): ")
day_of_week=input("Enter a starting day of the week, case insensitive: ")

result=add_time(start_time, duration_time)
print(result)