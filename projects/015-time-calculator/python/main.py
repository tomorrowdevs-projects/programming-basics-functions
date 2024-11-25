'''
Write a function named `add_time` that takes in two required parameters and one optional parameter:
* a start time in the 12-hour clock format (ending in AM or PM) 
* a duration time that indicates the number of hours and minutes
* (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show `(next day)` after the time. If the result will be more than one day later, it should show `(n days later)` after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result.
The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.
```py
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.'''

import datetime

def add_time(userstarttime, userdurationtime):
    array = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
    daycounter = 0
    hourscounter = 0

    splitteduserstarttime = userstarttime.split()
    doublesplitteduserstarttime = splitteduserstarttime[0].split(":")
    splitteduserdurationtime = userdurationtime.split(":")

    hoursstarttime = int(doublesplitteduserstarttime[0])
    minutesstarttime = int(doublesplitteduserstarttime[1])
    hoursdurationtime = int(splitteduserdurationtime[0])
    minutesdurationtime = int(splitteduserdurationtime[1])

    totalhours = hoursstarttime + hoursdurationtime
    totalminutes = minutesstarttime + minutesdurationtime

    if totalhours >= 24:
        newtotalhours = totalhours % 24
        daycounter = totalhours // 24
    else:
        newtotalhours = totalhours
        daycounter = 0
    
    finalhours = newtotalhours + daycounter

    if finalhours > 12:
        PMfinalhours = finalhours - 12
        print(f"{PMfinalhours:03d} : {totalminutes:02d} PM")
    else:
        print(f"{finalhours:03d} : {totalminutes:02d} {splitteduserstarttime[1]}")

def main():
    userstarttime = input("Please input a starting time (indicate AM or PM): ")
    userdurationtime = input("Please input how many hours and minutes you wanna add: ")
    add_time(userstarttime, userdurationtime)

if __name__ == '__main__':
    main()