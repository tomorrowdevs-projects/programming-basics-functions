def add_time(start, duration, day=None):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    start_time, h_format = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))
    
    total_minutes = (start_hour + duration_hour) * 60 + start_minute + duration_minute

    end_hour = (total_minutes // 60) 
    end_minutes = total_minutes % 60

    day_counter = 0
    if end_hour >= 12:
        end_hour %= 12
        if end_hour == 0:
            end_hour = 12
        if h_format == "AM":
            h_format = "PM"
        elif h_format == "PM":
            h_format = "AM"
            day_counter += 1
    
    new_day_counter = day_counter + total_minutes // 1440

    if day != None:
        day = day.lower()
        if day in days:
            index_days = days.index(day)
            total_index = (index_days + new_day_counter) % 7
            new_day = days[total_index]
        if new_day_counter > 1:
            message = f'{end_hour}:{end_minutes:02} {h_format}, {new_day} ({new_day_counter} days later)' 
        elif new_day_counter < 1:
            message = f'{end_hour}:{end_minutes:02} {h_format}, {day}' 
    elif new_day_counter == 1:
        message = f'{end_hour}:{end_minutes:02} {h_format} (next day)' 
    elif new_day_counter < 1: 
        message = f'{end_hour}:{end_minutes:02} {h_format}'
    else:
        message = f'{end_hour}:{end_minutes:02} {h_format} ({new_day_counter} days later)' 

    return message
    

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))

    