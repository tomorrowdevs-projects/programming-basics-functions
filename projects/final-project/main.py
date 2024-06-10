from datetime import datetime, date
from pytz import timezone
from time import monotonic, sleep
from threading import Thread, Event

def current_time(tz=None):
    dt=datetime.now()
    if tz!=None:
        if len(tz)==1:
            tz=timezone(tz)
        else:
            date_list=list()
            for i in tz:
                dt_tz=dt.astimezone(timezone(i))
                date_tz=dt_tz.strftime('%A %d/%m/%Y %H:%M:%S %Z')
                year_month_day=date(dt_tz.year,dt_tz.month,dt_tz.day).isocalendar()
                date_list.append('{} - Day {} of the year - Week {} of the year'.format(date_tz,(year_month_day.week-1)*7+year_month_day.weekday,year_month_day.week))
    else:
        date_list=dt.strftime('%A %d/%m/%Y %H:%M:%S %Z')

    if tz==None:
        date_list=date_list+'Local Time'
    return date_list

def countdown_timer(days=0,hours=0,minutes=0,seconds=0):
    timer_duration=days*24*60*60+hours*60*60+minutes*60+seconds
    print_time=start_time=monotonic()
    print(timer_duration)
    while monotonic()-start_time<timer_duration:
        if monotonic()-print_time==1:
            print(int(timer_duration-(monotonic()-start_time)))
            print_time=monotonic()

def main():
    print('Wellcome to the time utility app! You can perform these operations:\n[1] - Show current time\n[2] - Set a countdown timer')
    operation=input('Input the number relevant to the operation you want to perform:')
    if operation=='1':
        tz_list=list()
        tz=input('Please, input the time zone name or "None" for local time:')
        while tz!='' and tz!='None':
            tz_list.append(tz)
            tz=input('Please, input another time zone name or press enter to continue:')
        
        if tz=='None':
            date=current_time()
            print(date)
        else:
            date=current_time(tz_list)
            for dt in date:
                print(dt)
    elif operation=='2':
        days=int(input('Please, enter the number of days:'))
        hours=int(input('Please, enter the number of hours:'))
        minutes=int(input('Please, enter the number of minutes:'))
        seconds=int(input('Please, enter the number of seconds:'))
        countdown_timer(days,hours,minutes,seconds)
            
if __name__=='__main__':
    main()