
def hex2int(hexadecimal):
    hex_numbers = {
            '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
        }

    hexadecimal = hexadecimal.upper()
    if hexadecimal in hex_numbers.keys():
        integer = hex_numbers[hexadecimal]
        return integer
    else: 
        raise ValueError("Entered value out of range.")
        

def int2hex(integer):
    int_numbers = {
            1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
        }
    
    if integer in int_numbers.keys():
        hex = int_numbers[integer]
        return hex
    else:
        raise ValueError("Entered value out of range.")


def main():
    hexadecimal = input('Enter a hexadecimal number: ')
    converted_value = hex2int(hexadecimal)
    print(f'Hex value converted to decimal: {converted_value}')

    integer = input('\nEnter an integer in input: ')
    converted_to_hex = int2hex(integer)
    print(f'Decimal value converted to hexadecimal: {converted_to_hex}')
    
        

if __name__ == '__main__':
    main()