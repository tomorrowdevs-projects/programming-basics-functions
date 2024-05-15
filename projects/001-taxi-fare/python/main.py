def taxi_fare(TravelDistance):
    if TravelDistance*1000<140:
        fare=4.00
    else:
        fare=4.00+0.25*(TravelDistance*1000/140)
        fare=round(fare,2)
    return fare

if __name__=='__main__':
    TravelDistance=280
    fare=taxi_fare(TravelDistance)
    print(fare)