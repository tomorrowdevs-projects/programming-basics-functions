def shipping_calculator(num_item):
    first_item_charge = 10.99
    other_items_charge = 2.99
    
    if num_item > 1:
        total_charge = first_item_charge + (other_items_charge * (num_item - 1))
    else:
        total_charge = first_item_charge
    
    return total_charge

def main():
    num_item = int(input('Enter the number of item(s) you wish to ship: \n'))
    
    while num_item <= 0:
        print('Error. You should enter a positive value.')
        num_item = int(input('Enter the number of item(s) you wish to ship: \n'))

    total_charge = shipping_calculator(num_item)
    print(f'Total charge for {num_item} item(s): €{total_charge}')

if __name__ == '__main__':
    main()