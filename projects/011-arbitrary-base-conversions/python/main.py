
def arbitrary_to_base_10(base, number_to_convert_to_10):
    converted_number_to_10 = 0
    letter_hex = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    inverted_string = number_to_convert_to_10[::-1]
    
    for exponent in range(0, len(number_to_convert_to_10)):
        
        if inverted_string[exponent] in letter_hex.keys():
            char_to_number = letter_hex[inverted_string[exponent]]
            converted_number_to_10 += (base ** exponent) * char_to_number
        else:
            converted_number_to_10 += (base ** exponent) * int(inverted_string[exponent]) 

    return converted_number_to_10


def base_10_to_arbitrary_base(number, arbitrary_base):
    converted_to_arbitrary = ''
    letter_hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    number = int(number)
    while number > 0:
        remainder = number % arbitrary_base
        if remainder in letter_hex:
            converted_to_arbitrary += letter_hex[remainder]
        else:
            converted_to_arbitrary += str(remainder)
        number = number // arbitrary_base
    return converted_to_arbitrary[::-1]


def main():
    bases = list(range(2,17))

    arbitrary_base = int(input('Please enter a base you want to start with: '))
    number_to_convert_to_10 = str(input('Enter the number that you want to convert to base 10: '))
    print(arbitrary_to_base_10(arbitrary_base, number_to_convert_to_10))
    if arbitrary_base not in bases:
        raise Exception('Error. Base out of range.')

  
    base10_number = str(input("Enter a number in base 10: "))    
    base_to_convert = int(input("Enter the base you want to convert it to: "))
    print(base_10_to_arbitrary_base(base10_number, base_to_convert))
    if base_to_convert not in bases:
        raise Exception('Error. Base out of range.')


if __name__ == '__main__':
    main()
