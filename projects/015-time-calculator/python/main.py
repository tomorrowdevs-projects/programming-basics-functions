
# defines a function that takes 2 mandatory parameter (a starting time and a duration time, and an optional parameter for the current day)

def add_time(start_time, duration_time, day=''):
# slices the parameters to extrapolates current hours, minutes and period (am or pm) from the starting time
    if len(start_time) == 8:
        hour = int(start_time[0:2])
        minutes = int(start_time[3:5])
        am_pm = start_time[-2:]
    elif len(start_time) == 7:
        hour = int(start_time[0])
        minutes = int(start_time[2:4])
        am_pm = start_time[-2:]

# slices the parameters to extrapolates hours, minutes from the duration time
    for i in range(0, len(duration_time)):
        if duration_time[i] == ':':
            index_hour = i
    hour_to_add = int(duration_time[0:index_hour])
    minutes_to_add = int(duration_time[-2:])

# makes the day name uppercase
    day = day.upper()

# assigns day's number to a variable, if parameter not been assigned variables assumes the value of 0
    if day == 'MONDAY':
        day_number = 1
    elif day == 'TUESDAY':
        day_number = 2
    elif day == 'WEDNESDAY':
        day_number = 3
    elif day == 'THURSDAY':
        day_number = 4
    elif day == 'FRIDAY':
        day_number = 5
    elif day == 'SATURDAY':
        day_number = 6
    elif day == 'SUNDAY':
        day_number = 7
    elif day == '':
        day_number = 0


    new_day_number = day_number

# adding minutes of duration time to starting time
    new_minutes = minutes + minutes_to_add

    counter_days = 0

# if total minutes are greater than 60, adds a unit to the current hour then store minutes left into a variable
    if new_minutes >= 60:
        hour = hour + 1
        if hour == 12:
            if am_pm == 'AM':
                am_pm = 'PM'
            elif am_pm == 'PM':
                am_pm = 'AM'
                counter_days += 1
        minutes_left = new_minutes % 60
        new_minutes = minutes_left

# foor loop that adds hour by hour to current hour the hours of duration time
    new_hour = hour

    for i in range(0, hour_to_add):
        new_hour += 1
        if new_hour == 12:
            if am_pm == 'AM':
                am_pm = 'PM'
            elif am_pm == 'PM':
                am_pm = 'AM'
                counter_days += 1
        if new_hour == 13:
            new_hour = 1

# adds a leading zero to minutes
    if 10 > new_minutes >= 0:
        new_minutes = str(new_minutes).zfill(2)

# if the optional parameter has not been used, no name will be assigned, otherwise a for loop will runs adding the days and so getting a number that corresponds to the name wanted
    if day_number == 0:
        new_day = None
    else:
        for i in range(0,counter_days):
            if new_day_number == 7:
                new_day_number = 1 
            else:
                new_day_number += 1



        if new_day_number == 1:
            new_day = 'Monday'
        elif new_day_number == 2:
            new_day = 'Tuesday'
        elif new_day_number == 3:
            new_day = 'wednesday'
        elif new_day_number == 4:
            new_day = 'Thursday'
        elif new_day_number == 5:
            new_day = 'Friday'
        elif new_day_number == 6:
            new_day = 'Saturday'
        elif new_day_number == 7:
            new_day = 'Sunday'

# composes an appropriate message and so return it as output   
    message = f'{new_hour}:{new_minutes} {am_pm}' 

    if counter_days == 0 and day_number == 0:
        return message
    elif counter_days == 1 and day_number == 0:
        message += ' (next day)'
    elif counter_days > 1 and day_number == 0:
        message += f' ({counter_days} days later)'
    elif counter_days == 0 and day_number != 0:
        message += f', {new_day}'
    elif counter_days == 1 and day_number != 0:
        message += f' (next day) {new_day}'
    elif counter_days > 1 and day_number != 0:
        message += f', {new_day} ({counter_days} days later) '

    return message

print(add_time("3:00 PM", "3:10",))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))