def hex2int(hexadecimal):

    hexadecimal = hexadecimal.upper()

    letter_list = 'ABCDEF'

    exponent = 0

    result_decimal = 0

    for digit in hexadecimal[::-1]:

        if (digit.isalpha() and not (digit in letter_list)):
            return 'Invalid value'
        
        if digit == 'A':
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



def int2hex(decimal):

    result_hexadecimal_letter = ''

    result_hexadecimal_number = 0

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



