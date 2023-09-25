def shipping_calculator(number_of_items):
    counter = 1
    shipping_charge = 10.99

    while number_of_items != counter:
        counter += 1
        shipping_charge += 2.99

    return shipping_charge

def main():
    number_of_items = int(input('Enter the number of items purchased: '))
    shipping_charge = shipping_calculator(number_of_items)
    print(f"{shipping_charge:.2f} $")

if __name__ == '__main__':
    main()
