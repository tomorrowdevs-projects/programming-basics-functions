# defines a function to calculate shipping costs
def shipping_cost(items):
# conditional that returns the shipping costs based on the number of item purchased
    items = int(items)
    if items == 1:
        return 10.99
    else: 
        total = 10.99 + (items * 2.99)
        return total

# defines a main function that asks to user the number of items, and return shpping costs
def main():
    user_input = input('Insert items: ')
    if user_input == '0':
        print('insert at least one item')
    else:
        print(f'Shipping cost is: {round(shipping_cost(user_input), 2)} euro')

# sets a conditional statement so the program run main() only if has not been imported in a another file.
if __name__ == '__main__':
    main()

