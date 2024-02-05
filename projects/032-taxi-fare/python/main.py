def taxi_fares(km: int)-> float: 
    '''returns the price for a ride by taxi that costs a base fare of 4.00€ and 0.25€ every 140 meters travelled.
            :parameter:
                    km (int): a decimal integer.
            :return:
                    total (float): rounded floating point number of two digits.
    '''
    meters = km * 1000
    meters_costs = (meters / 140) * 0.25
    total = round((meters_costs + 4.00), 2)
    return total


def main(): 
    print(f'Total amount is {taxi_fares(5)} euros')
    
 
if __name__ == '__main__':
    main()
