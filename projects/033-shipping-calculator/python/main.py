def shipping_calculator(number_of_items):
    counter = 1
    shipping_charge = 10.99

    while number_of_items != counter:
        counter += 1
        shipping_charge += 2.99

    return print(shipping_charge)