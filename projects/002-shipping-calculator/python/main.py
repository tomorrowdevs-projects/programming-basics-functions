'''
An online retailer provides express shipping for many of its items at a rate of: 
- €10.99 for the first item in an order
- €2.99 for each subsequent item in the same order. 

Write a function named **shipping calculator** that takes the number of items in the order as its **only parameter**. 

Return the shipping charge for the order as the function’s result. 

Include a main program that reads the number of items purchased from the user 
and displays the shipping charge.
'''

def shipping_calculator(itemlist):
    itemlist -= 1
    shippingcharge = 10.99 + (2.99 * itemlist)
    return shippingcharge

itemlist = int(input("Number of items you wanna purchase: "))
totalcharge = shipping_calculator(itemlist)
print("Total cost is: ", totalcharge)