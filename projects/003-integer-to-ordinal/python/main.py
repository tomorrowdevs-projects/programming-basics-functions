def integer_to_ordinal(number):
    if not number in range(1,13):
        number=''
    if number==1:
        number='first'
    elif number==2:
        number='second'
    elif number==3:
        number='third'
    elif number==4:
        number='fourth'
    elif number==5:
        number='fifth'
    elif number==6:
        number='sixth'
    elif number==7:
        number='seventh'
    elif number==8:
        number='eighth'
    elif number==9:
        number='ninth'
    elif number==10:
        number='tenth'
    elif number==11:
        number='eleventh'
    elif number==12:
        number='twelfth'
    return number

def main():
    for i in range(1,13):
        number=int(i)
        ordinal=integer_to_ordinal(number)
        print('{} - {}'.format(number,ordinal))

if __name__=='__main__':
    main()