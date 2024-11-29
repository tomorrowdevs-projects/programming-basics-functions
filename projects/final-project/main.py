from datetime import datetime, date
from pytz import timezone, all_timezones
from threading import Thread, Event
from msvcrt import getwch
from os import system

input_event=Event()
pause_event=Event()
reset_event=Event()
exit_event=Event()

def current_time(tz=None):
    dt=datetime.now()
    if tz!=None:
        if len(tz)==1 and type(tz)=='str':
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
    padding='{:>'+str(len(str(timer_duration))+1)+'}'
    i=0
    while input_event.is_set() and i<timer_duration:
        if input_event.is_set():
            if not reset_event.is_set():
                print(padding.format(timer_duration-i),end='\r')
                i+=1
                if pause_event.is_set():
                    exit_event.wait(delay)
                else:
                    while not pause_event.is_set() and not exit_event.is_set():
                        pass
            else:
                reset_event.clear()
                i=0
                print(padding.format(timer_duration-i),end='\r')
                i+=1
                if pause_event.is_set():
                    exit_event.wait(delay)
                else:
                    while not exit_event.is_set():
                        pause_event.wait()
    if input_event.is_set():
        print('Time finished!')

def main():
    print('Wellcome to the time utility app! You can perform these operations:\n[1] - Show current time\n[2] - Set a countdown timer')
    operation=input('Input the number relevant to the operation you want to perform: ')
    if operation=='1':
        print(all_timezones)
        tz_list=list()
        tz=input('Please, input the time zone name or "None" for local time: ')
        while tz!='' and tz!='None':
            tz_list.append(tz)
            tz=input('Please, input another time zone name or press enter to continue: ')
        
        if tz=='None':
            date=current_time()
            print(date)
        else:
            date=current_time(tz_list)
            for dt in date:
                print(dt)
    elif operation=='2':
        days=int(input('Please, enter the number of days: '))
        hours=int(input('Please, enter the number of hours: '))
        minutes=int(input('Please, enter the number of minutes: '))
        seconds=int(input('Please, enter the number of seconds: '))
        output_format=input('Please, enter the ouput format ([dd] days, [hh] hours, [mm] minutes or [ss] seconds): ')
        timer_thread=Thread(group=None,target=countdown_timer,args=(days,hours,minutes,seconds,output_format))
        input_event.set()
        pause_event.set()
        timer_thread.start()
        while input_event.is_set():
            print('Press 0 to exit, 1 to pause or restart the countdown, 2 to reset the countdown')
            key=getwch()
            if key=='0':
                input_event.clear()
                exit_event.set()
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