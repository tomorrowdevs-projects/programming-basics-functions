def shipping_calculator(items):
    shipping_charge=10.99+(items-1)*2.99
    return shipping_charge

is_valid_input=False
while not(is_valid_input):
    number_items=input("Enter the number of items purchased: ")
    if number_items.isnumeric() and int(number_items)>0:
        number_items=int(number_items)
        is_valid_input=True

shipping_charge=shipping_calculator(number_items)
print(f"Shipping charge: {shipping_charge:.2f} €")