import string

def convert_to_base_10(number, base):
    converted_number = int(number, base)
    return converted_number

def convert_to_arbitrary_base(quotient, base):
    converted_base = []

    while quotient != 0:
        rest = quotient % base
        if rest > 9:
            rest = string.ascii_uppercase[rest - 10]

        converted_base.append(str(rest))
        quotient = quotient // base
    converted_base.reverse()

    return ''.join(converted_base)

def main():
    number_to_convert = input('Enter number to convert:\n')
    starting_base = int(input('Enter the starting base:\n'))
    arrival_base = int(input('Enter the arrival base:\n'))

    if starting_base > 16 or starting_base < 2 or arrival_base > 16 or arrival_base < 2:
        raise ValueError("Invalid digit! The base must be between 2 and 16 inclusive")

    base_10 = convert_to_base_10(number_to_convert, starting_base)
    arbitrary_base = convert_to_arbitrary_base(base_10, arrival_base)

    if arrival_base == 10:
        print(base_10)
    elif starting_base == 10:
        print(arbitrary_base)
    else:
        print(arbitrary_base)

if __name__ == '__main__':
    main()
