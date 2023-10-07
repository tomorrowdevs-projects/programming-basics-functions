def taxi_fare(distance):

    """Compute total taxi fare (including additional fare) 
    taking distance (in km) entered by user as parameter"""

    base_fare = 4.00
    rate_per_140m = 0.25
    meters_for_plus = 140
    distance_m = distance * 1000          #convert km to meters 
    total_fare = (distance_m / meters_for_plus) * rate_per_140m + base_fare
    return total_fare


def main():
    check_value = False
    
    while not check_value:
        try:
            distance = float(input("Enter the distance (in km) that you want to cross: "))
            while distance < 0:
                print('Error. Distance cannot be a negative value.')
                distance = float(input("Please enter the distance (in km) that you want to cross: "))
            check_value = True
        except ValueError:
            print('Please enter a numeric data.')

    total_fare = taxi_fare(distance)
    print(f'Total fare: €{total_fare: .2f}')


if __name__ == '__main__':
    main()