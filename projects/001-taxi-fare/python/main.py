def taxi_fare(distance):
    distance*=1000
    total_fare=BASE_FARE+(distance//140)*0.25
    return total_fare

travel_distance=float(input("Enter the distance travelled (in kilometers): "))
BASE_FARE=4.00

total_fare=taxi_fare(travel_distance)
print(f"Total fare: €{total_fare:.2f}")