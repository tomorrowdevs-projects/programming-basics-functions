def arbitrary_to_base_10(number:str,base:int)->int:

    '''Returns a number from an arbitrary base between 2 and 16 to a base number 10
            :parameter: 
                number(str): the number as string to convert.
                base(int): base of the number.
            :return:
                result(int): the converted number.
    '''
    
    if base > 16 or base < 2:
         return 'base out of range'
    
    number = number.upper()

    number_converted = 0

    exponent = 0

    letter_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    # loops trough the string "number" and for each character: first checks if it is a valid one, second if it is a letter translate it to a number using "letter_dict" and computes the value adding it to variable "result", otherwise simply computes the value itself adding it to the variable.
    for digit in number[::-1]:
       if digit.isalpha() and digit not in letter_dict:
           return 'not a valid number'
       elif digit.isalpha()and digit in letter_dict:
           number_converted += letter_dict[digit] * base ** exponent
           exponent += 1
       else:
            number_converted += int(digit) * base ** exponent
            exponent += 1
    
    return number_converted


def base_10_to_arbitrary_base(number:int,base:int)-> str:

    '''Returns a number in the required base from a base number 10.
            :parameter:
                    number(int): the 10 base number.
                    base(int): the base required.
            :return:
                    converted_number(str): the result of the conversion.
    '''

    if base > 16 or base < 2:
         return 'base out of range'
    
    base_dict = {10 : 'A', 11 :'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    
    converted_number = ''

    #
    while number != 0:
        remainder = number % base
        number = number // base

        if 11 <= base <= 16 and remainder in base_dict and remainder >= 10:
            converted_number += base_dict[remainder]
        else:
            converted_number += str(remainder)
    converted_number = converted_number[::-1]

    return converted_number


        
def main():

    '''Main program that allows the user to make coversions from any base to base 10 and from base 10 to any base'''

    number_with_base_x, from_base_x_to_10 = input('Enter any number and a base from 2 to 16 separated by a whitespace to convert it into a base 10 number: ').split()
    print(f'The number "{number_with_base_x}" with base {from_base_x_to_10} is {arbitrary_to_base_10(number_with_base_x,int(from_base_x_to_10))} with base 10')

    decimal_number, from_base_10_to_x = input('Enter any decimal number and a base from 2 to 16 separated by a whitespace to convert it: ').split()
    print(f'The number "{decimal_number}" with base {from_base_10_to_x} is {base_10_to_arbitrary_base(int(decimal_number),int(from_base_x_to_10))} with base 10')

if __name__ == '__main__':
    main()