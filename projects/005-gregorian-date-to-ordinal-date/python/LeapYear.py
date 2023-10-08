def isleap(year):
    if year % 4 == 0:
        days = 366
        if year % 100 == 0 and year % 400 == 0:
            days = 366
        else:
            days = 365
    else:
        days = 365
    
    if days == 366:
        return True
