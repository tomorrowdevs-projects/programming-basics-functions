'''
In a particular jurisdiction, taxi fares consist of: 
- base fare of €4.00, 
- plus €0.25 for every 140 meters travelled. 

Write a function named **taxi fare** that takes the distance travelled (in kilometers) as its only parameter 
and returns the total fare as its only result. 
Write a main program that demonstrates the function.
'''

def taxi_fare(kilometers):
    addedtaxes = kilometers // 140
    taxfare = 0.25 *  addedtaxes
    totalfare = 4.00 + taxfare
    return totalfare

kilometers = int(input("Kilometers: "))
totalfare = taxi_fare(kilometers)
print("Total fare = ", totalfare)