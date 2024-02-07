def hex2int(hexadecimal: str)->int:

    '''Returns a decimal number from a hexadecimal number.
            :parameter:
                    hexadecimal(str): a hexadecimal number.
            :return:
                    result_decimal(int): decimal number resulting from conversion.
    '''
    
    hexadecimal = hexadecimal.upper()
     
    letter_list = 'ABCDEF'

    exponent = 0

    result_decimal = 0

    # loops the hexadecimal backwards, for every character checks if is a valid letter and if so converts it in a decimal number (otherwhise if a number converts it in a integer), then adds it to "result_decimal" after multiplying it by "exponent" that is increased by 1 each cycle.

    for digit in hexadecimal[::-1]:

        if (digit.isalpha() and not (digit in letter_list)):
            return 'Invalid value'
        elif digit == 'A':
            digit = 10
        elif digit == 'B':
            digit = 11
        elif digit == 'C':
            digit = 12
        elif digit == 'D':
            digit = 13
        elif digit == 'E':
            digit = 14
        elif digit == 'F':
            digit = 15
        else:
            digit = int(digit)

        result_decimal += digit * 16**exponent

        exponent += 1

    return result_decimal



def int2hex(decimal:int)-> str:

    '''Returns a hexadecimal number from a decimal number between 0 and 15.
            :parameter:
                    decimal(int): a decimal number.
            :return:
                    result_decimal(str): hexdecimal number resulting from conversion.
    '''

    result_hexadecimal_letter = ''

    result_hexadecimal_number = 0

    # checks if number is between 0 and 15, if not return an error message, otherwise checks if is it lower or equal then 9 and return the number itself. If between 9 to 15 converts it in a letter and then returns the results.

    if 0 <= decimal <= 15:

        if decimal <= 9:

            result_hexadecimal_number += decimal

            return result_hexadecimal_number

        else:
            if decimal == 10:
                result_hexadecimal_letter += 'A'
            elif decimal == 11:
                result_hexadecimal_letter += 'B'       
            elif decimal == 12: 
                result_hexadecimal_letter += 'C'
            elif decimal == 13:
                result_hexadecimal_letter += 'D'
            elif decimal == 14:
                result_hexadecimal_letter += 'E'
            elif decimal == 15:
                result_hexadecimal_letter += 'F'

            return result_hexadecimal_letter
    else: 
        return 'Invalid value'
