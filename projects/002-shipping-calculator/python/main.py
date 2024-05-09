def shipping_calculator(ItemQty):
    FirstItemPrice=10.99
    FurtherItemPrice=2.99
    if ItemQty<2:
        ExpeditionPrice=10.99
    else:
        ExpeditionPrice=FirstItemPrice+(ItemQty-1)*FurtherItemPrice
    return ExpeditionPrice

def main():
    ItemQty=input('Please, enter the quantity of item that you want to ship (only integer numbers):')
    ExpeditionPrice=shipping_calculator(ItemQty)
    print('The item number is {}, so the expedition price is {}'.format(ItemQty,ExpeditionPrice))

if __name__=='__main__':
    main()