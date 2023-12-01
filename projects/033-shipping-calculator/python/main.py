def shipping_costs(items):
# conditional that checks if user enter one or more items,then returns shipping costs
    items = int(items)
    if items == 1:
        return 10.99
    else: 
        total = 10.99 + ((items - 1) * 2.99)
        return total

# defines a main function that asks to user number of items, and print shipping costs using the previous function
def main():
    user_input = int(input('Insert items: '))
    if user_input == 0 :
        print('insert at least one item')
    else:
        print(f'Shipping costs are: {round(shipping_costs(user_input), 2)} €')

# conditional that run main program only if the script has not been imported
if __name__ == '__main__':
    main()

