def add_time(start_time,duration,start_day=None):
    week_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if start_day!=None:
        start_day_number=week_days.index(start_day)+1
    start_day_half=start_time.split(' ')[1]
    start_hour=int(start_time.split(' ')[0].split(':')[0])
    start_minutes=int(start_time.split(' ')[0].split(':')[1])
    duration_hour=int(duration.split(':')[0])
    duration_minutes=int(duration.split(':')[1])
    end_day_half=start_day_half
    next_day_mex=''

    #--Minutes calculation--#
    end_minutes=(start_minutes+duration_minutes)%60
    q=(start_minutes+duration_minutes)//60

    #--Hours calculation--#
    end_hour=(start_hour+duration_hour+q)%12
    if end_hour==0:
        end_hour=12

    q=(start_hour+duration_hour+q)//12
    if q==0 and end_hour==12:
        if start_day_half=='AM':
            end_day_half='PM'
        else:
            end_day_half='AM'
            next_day_mex='next day'
        end_day_number=(start_day_number+1)%7
        end_day=week_days[end_day_number-1]
    elif q%2>0 and end_hour!=12:
        if start_day_half=='AM':
            end_day_half='PM'
        else:
            end_day_half='AM'

        next_day_number=q//2    
        if next_day_number>1:
            next_day_mex='{} days later'.format(next_day_number)
        elif next_day_number==1:
            next_day_mex='next day'

        end_day_number=(start_day_number+next_day_number)%7
        end_day=week_days[end_day_number-1]
    elif q%2>0 and end_hour==12 and start_hour==12:
        next_day_number=q//2    
        if next_day_number>1:
            next_day_mex='{} days later'.format(next_day_number)
        elif next_day_number==1:
            next_day_mex='next day'
        end_day_number=(start_day_number+next_day_number)%7
        end_day=week_days[end_day_number-1]
    elif q%2>0 and end_hour==12:
        next_day_number=q//2+1    
        if next_day_number>1:
            next_day_mex='{} days later'.format(next_day_number)
        elif next_day_number==1:
            next_day_mex='next day'

        end_day_number=(start_day_number+next_day_number)%7
        end_day=week_days[end_day_number-1]
    else:
        next_day_number=q//2    
        if next_day_number>1:
            next_day_mex='{} days later'.format(next_day_number)
        elif next_day_number==1:
            next_day_mex='next day'

        end_day_number=(start_day_number+next_day_number)%7
        end_day=week_days[end_day_number-1]   

    if start_day!=None and len(next_day_mex)>0: 
        end_time='{}:{:02} {}, {} ({})'.format(end_hour,end_minutes,end_day_half,end_day,next_day_mex)
    elif start_day!=None and len(next_day_mex)==0:
        end_time='{}:{:02} {}, {}'.format(end_hour,end_minutes,end_day_half,end_day)
    elif start_day==None and len(next_day_mex)>0:
        end_time='{}:{:02} {} ({})'.format(end_hour,end_minutes,end_day_half,next_day_mex)
    elif start_day==None and len(next_day_mex)==0:
        end_time='{}:{:02} {}'.format(end_hour,end_minutes,end_day_half)  
    
    return end_time

def main():
    start_time=input('Please, enter the start time (xx:xx AM/PM):')
    duration=input('Please, enter the duration (xx:xx):')
    start_day=input('Please, enter the start day of the week or give a void input:')
    if len(start_day)==0:
        end_time=add_time(start_time,duration)
    else:
        end_time=add_time(start_time,duration,start_day)
    print(end_time)

if __name__=='__main__':
    main()
        

