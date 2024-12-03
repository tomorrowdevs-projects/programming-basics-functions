from datetime import datetime, date
import time
import pytz

def display_current_time() -> None:
    date_time=datetime.now()
    current_date=date_time.strftime("%d-%m-%Y")
    current_time = date_time.strftime("%H:%M:%S")    
    print(f"Current date is: {current_date}")
    print(f"Current time is: {current_time}")

def display_date_information() -> None:
    today_date=date.today()
    day_week=today_date.strftime("%A")
    print(f"Day of the week is: {day_week}")

    start_date=date(today_date.year,1,1)
    end_date=date(today_date.year,today_date.month,today_date.day)
    date_difference=end_date-start_date
    day_year=date_difference.days+1
    print(f"Day of the year is: {day_year}")

    week_number=today_date.strftime("%U")
    print(f"Week number is: {week_number}")

def countdown_timer(hours: int, minutes: int, seconds: int) -> None:
    total_seconds=(hours*3600)+(minutes*60)+seconds
    for timer in range(total_seconds, 0, -1):
        hour=timer//3600
        minute=(timer%3600)//60
        second=timer%60
        print(f"Countdown Timer: {hour:02}:{minute:02}:{second:02}", end="\r")
        time.sleep(1)
    print("\nTime's up!")

def customizable_output(hours: int, minutes: int, seconds: int, customizable_output: str) -> None:
    if customizable_output=="days":
        total_seconds=(hours*3600)+(minutes*60)+seconds
        for timer in range(total_seconds, 0, -1):
            days=timer//86400
            hour=(timer%86400)//3600
            minute=(timer%3600)//60
            second=timer%60
            print(f"Countdown Timer: {days} days, {hour:02}:{minute:02}:{second:02}", end="\r")
            time.sleep(1)
        print("\nTime's up!")

    elif customizable_output=="hours":
        total_seconds=(hours*3600)+(minutes*60)+seconds
        for timer in range(total_seconds, 0, -1):
            hour=timer//3600
            minute=(timer%3600)//60
            second=timer%60
            print(f"Countdown Timer (hh:mm:ss): {hour:02}:{minute:02}:{second:02}", end="\r")
            time.sleep(1)
        print("\nTime's up!")
       
    elif customizable_output=="minutes":
        total_seconds=(hours*3600)+(minutes*60)+seconds
        for timer in range(total_seconds, 0, -1):
            minute=timer//60
            second=timer%60
            print(f"Countdown Timer (mm:ss): {minute:02}:{second:02}", end="\r")
            time.sleep(1)
        print("\nTime's up!")
    else:
        total_seconds=(hours*3600)+(minutes*60)+seconds
        for timer in range(total_seconds, 0, -1):
            print(f"Countdown Timer (ss): {timer:02} seconds", end="\r")
            time.sleep(1)
        print("\nTime's up!")     

def stopwatch() -> None:
    try:
        print("Started stopwatch! Press 'Ctrl+c' to stop it!")
        start_time=time.time()
        while True:
            end_time=time.time()
            print("Elapsed time:",int(end_time-start_time),"seconds",end='\r')
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopped stopwatch")
        user_input=input("Do you want reset stopwatch? Enter 'reset' or a blank line to quit: ")
        while user_input!="":    
            if user_input=="reset":
                stopwatch()
                break
            else:
                user_input=input("Do you want reset stopwatch? Enter 'reset' or a blank line to quit: ")

def time_zone_conversion(time_zone_input: str) -> None:
    time_zone=pytz.timezone(time_zone_input)    
    date_time=datetime.now(time_zone)    
    current_time=date_time.strftime("%H:%M:%S")    
    print(f"Current time in {time_zone_input} is: {current_time}")

def world_clock_display(time_zones_list: list) -> None:
    for item in time_zones_list:
        time_zone_conversion(item)

def main():
    # Display Current Time
    # The program should display the current time and date based on the system clock.
    display_current_time()

    # Display Date Information
    # Include additional date information such as day of the week, day of the year, and week number.
    display_date_information()

    # Countdown Timer
    # Enable the user to set a countdown timer for a specific amount of time (in hours, minutes, and seconds) 
    # and display the remaining time.
    while True:
        try:
            hours=int(input("\nEnter an amount of time in hours: "))
            if hours>=0:
                break
        except ValueError:
            print("Invalid input!")
    while True:
        try:
            minutes=int(input("Enter an amount of time in minutes: "))
            if minutes>=0 and minutes<=59:
                break
        except ValueError:
            print("Invalid input!")
    while True:
        try:
            seconds=int(input("Enter an amount of time in seconds: "))
            if seconds>=0 and seconds<=59:
                break
        except ValueError:
            print("Invalid input!")

    # Customizable Countdown Output
    # Allow the user to choose how they want the countdown displayed (e.g., days, hours, minutes).
    ask_change=input("Do you want customizable the countdown output? (Enter yes/no): ")
    while ask_change!="yes" and ask_change!="no":
        print("Invalid input!")
        ask_change=input("Do you want customizable the countdown output? (Enter yes/no): ")

    if ask_change=="yes":
        ask_user=input("Choose how you want the countdown displayed (days/hours/minutes/seconds): ")

        while ask_user!="days" and ask_user!="hours" and ask_user!="minutes" and ask_user!="seconds":
            print("Invalid input!")
            ask_user=input("Choose how you want the countdown displayed (days/hours/minutes/seconds): ")

        customizable_output(hours,minutes,seconds,ask_user)

    else:
        countdown_timer(hours, minutes, seconds)

    # Stopwatch
    # Implement a stopwatch feature that allows the user to start, stop, and reset the timer.
    ask_user=input("\nDo you want to start stopwatch? (Enter start/no): ")
    while ask_user!="start" and ask_user!="no":
        print("Invalid input!")
        ask_user=input("Do you want to start stopwatch? (Enter start/no): ")

    if ask_user=="start":
        stopwatch()

    # Time Zone Conversion
    # Allow the user to input a specific time zone, and then display the current time in that time zone.
    time_zone=input("\nEnter a specific time zone (e.g. Europe/Rome): ")
    while not(time_zone in pytz.all_timezones):
        print("Invalid input!")
        time_zone=input("Enter a specific time zone (e.g. Europe/Rome): ")

    time_zone_conversion(time_zone)

    # World Clock Display
    # Allow the user to add and display multiple clocks for different time zones simultaneously.
    time_zones=[]
    time_zone=input("\nAdd a specific time zone (e.g. Europe/Rome) or blank to quit: ")
    while time_zone!='':
        if time_zone in pytz.all_timezones:
            time_zones.append(time_zone)

        time_zone=input("Add a specific time zone (e.g. Europe/Rome) or blank to quit: ")

    world_clock_display(time_zones)


if __name__=="__main__":
    main()