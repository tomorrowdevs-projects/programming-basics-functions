def calculate_distance(kilometers_travelled):
    service_price = 4

    conversion_metres = kilometers_travelled * 1000
    service_price += (conversion_metres / 140) * 0.25
    service_price = round(service_price, 2)

    return service_price

def main():
    distance = float(input("Enter the distance traveled in kilometers: "))
    taxi_fare = calculate_distance(distance)
    print(f'{taxi_fare} $')

if __name__ == '__main__':
    main()
