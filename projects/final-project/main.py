from datetime import datetime, date
from pytz import timezone
from time import sleep
from threading import Thread, Event
from msvcrt import getwch
from os import system

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

pause_event=Event()
reset_event=Event()
input_event=Event()

def countdown_timer(days=0,hours=0,minutes=0,seconds=0,output_format='ss'):
    if output_format=='dd':
        timer_duration=days+hours/24+minutes/(24*60)+seconds/(24*60*60)
        delay=24*60*60
    elif output_format=='hh':
        timer_duration=days*24+hours+minutes/60+seconds/(60*60)
        delay=60*60
    elif output_format=='mm':
        timer_duration=days*24*60+hours*60+minutes+seconds/60
        delay=60
    elif output_format=='ss':
        timer_duration=days*24*60*60+hours*60*60+minutes*60+seconds
        delay=1
    
    i=0
    while input_event.is_set() and i<timer_duration:
        pause_event.wait()
        if input_event.is_set():
            if not reset_event.is_set():
                print(i,end='\r')
                i+=1
                sleep(delay)
            else:
                reset_event.clear()
                i=0
                print(i,end='\r')
                i+=1
                sleep(delay)
    if input_event.is_set():
        print('Time finished!')

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
        output_format=input('Please, enter the ouput format ([dd] days, [hh] hours, [mm] minutes or [ss] seconds):')
        timer_thread=Thread(group=None,target=countdown_timer,args=(days,hours,minutes,seconds,output_format))
        input_event.set()
        pause_event.set()
        timer_thread.start()
        while input_event.is_set():
            print('Press 0 to exit, 1 to pause or restart the countdown, 2 to reset the countdown')
            key=getwch()
            if key=='0':
                input_event.clear()
                pause_event.set()
                system('cls')
            elif key=='1':
                if pause_event.is_set():
                    pause_event.clear()
                else:
                    pause_event.set()
            elif key=='2':
                reset_event.set()
                pause_event.set()
            print('\033[2A')

if __name__=='__main__':
    main()