def shipping_costs(items: int)-> float:
    '''Returns shipping costs based on number of items gived, costs consist of a fixed of 10.99€ and 2.99€ for each item more than the first .
            :parameter: 
                    items(int): integer that represents the number of items shipped.
            :return:
                    total(float): floating point number, the total for shipping costs.
    '''
    items = int(items)
    if items == 1:
        return 10.99
    else: 
        total = 10.99 + ((items - 1) * 2.99)
        return total

def main():
    '''Asks item's number and prints a message with the amount for shipping costs, if items are less than one prints an error message.
    '''
    user_input = int(input('Insert items: '))
    if user_input < 1:
        print('insert at least one item')
        main()
    else:
        print(f'Shipping costs are: {round(shipping_costs(user_input), 2)} €')

# entry point,the program runs only if file has not been imported. 
if __name__ == '__main__':
    main()

