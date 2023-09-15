import string


def get_bases_information():
    number_to_convert = input('Enter number to convert:\n')
    starting_base = int(input('Enter the starting base:\n'))
    arrival_base = int(input('Enter the arrival base:\n'))

    return number_to_convert, starting_base, arrival_base

def convert_to_base_10(number, base):
    return int(number, base)

def convert_to_base_to_get(quotient, base):
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
    get_info = get_bases_information()

    if get_info[1] not in range(2, 17) or get_info[2] not in range(2, 17):
        return ValueError("Invalid digit! The base must be between 2 and 16 inclusive")
    elif get_info[2] == 10:
        return convert_to_base_10(get_info[0], get_info[1])
    else:
        return convert_to_base_to_get(convert_to_base_10(get_info[0], get_info[1]), get_info[2])

print(main())
