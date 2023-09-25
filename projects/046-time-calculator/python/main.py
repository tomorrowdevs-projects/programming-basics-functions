def add_time(start_time, duration_time, starting_day_of_the_week=None):
    time_format = ''
    hour = ''
    duration_hour = ''
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = 0
    index_list = 0

    for character in start_time:

        if character.isalpha():
            time_format += character

        elif character.isdigit():
            hour += character

    minutes = int(hour[-2:])
    hour = int(hour[:-2])

    for character in duration_time:
        if character.isdigit():
            duration_hour += character

    minutes += int(duration_hour[-2:])
    total_minutes = minutes % 60
    hour += (minutes // 60) + int(duration_hour[:-2])

    if time_format == 'PM':
        hour += 12

    while hour > 24:
        hour -= 24
        day += 1


    if 0 <= hour < 12:
        time_format = 'AM'
    elif hour == 24:
        time_format = 'AM'
        hour -= 12
    elif hour != 12:
        hour = hour % 12
    else:
        time_format = 'PM'


    if starting_day_of_the_week is not None:
        index_list = days_of_the_week.index(starting_day_of_the_week.lower().capitalize())

        if hour >= 12:
            day += 1

    if day < 1:
        result = f"{hour:02}:{total_minutes:02} {time_format}"
    elif day == 1:
        result = f"{hour:02}:{total_minutes:02} {time_format}, {days_of_the_week[(index_list + day) % 7]} (next day)"
    else:
        result = f"{hour:02}:{total_minutes:02} {time_format}, {days_of_the_week[(index_list + day) % 7]} ({day} days later)"

    return result