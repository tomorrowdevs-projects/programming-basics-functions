

def integer_to_ordinal(integers):
    '''
    defines a function that takes an integer between 1 and 12 as parameter, and returns the corresponding ordinal number. 
    '''
    integer_ordinal_dict = {

        1 : 'First',
        2 : 'Second',
        3 : 'Third',
        4 : 'Fourth',
        5 : 'Fifth',
        6 : 'Sixth',
        7 : 'Seventh',
        8 : 'Eighth',
        9 : 'Ninth',
        10 : 'Tenth',
        11 : 'Eleventh',
        12 : 'Twelfth'

    }

    return integer_ordinal_dict.get(integers, '')

def main():
    '''
    Main program that print on screen the ordinal number in a range between one and twelve.
    '''
    for i in range(1, 13):
       print(integer_to_ordinal(i))

if __name__ == "__main__":
    main()