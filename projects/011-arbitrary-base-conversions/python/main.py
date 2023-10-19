# defines a function that convert a number with a base between 2 and 16 to base 10.
def arbitrary_to_base_10(number,base):

    if base > 16 or base < 2:
        return 'base out of range'
   
    number = str(number)

    result = 0

    exponent = 0

    letter_list = 'ABCDEF'
# series of conditionals that, in base of the number system choosen, modify execution's flow.
    if base == 11:
# for loop that iterates the number typed, eventually translate letters in number and perform the conversion.
        for digit in number[::-1]:
            if digit.isalpha() and not digit.upper() == letter_list[0]:
                return 'error'
            elif digit.upper() == letter_list[0]:
                digit = 10
            result += int(digit) * base ** exponent
            exponent += 1
        return int(result)
    elif base == 12:
        for digit in number[::-1]:
            if digit.isalpha() and digit.upper() not in letter_list[0:2]:
                return 'error'
            elif digit.upper() == letter_list[0]:
                digit = 10
            elif digit.upper() == letter_list[1]:
                digit = 11
            result += int(digit) * base ** exponent
            exponent += 1
        return int(result),letter_list[0:2]
    elif base == 13:
        for digit in number[::-1]:
            if digit.isalpha() and digit.upper() not in letter_list[0:3]:
                return 'error'
            elif digit.upper() == letter_list[0]:
                digit = 10
            elif digit.upper() == letter_list[1]:
                digit = 11
            elif digit.upper() == letter_list[2]:
                digit = 12
            result += int(digit) * base ** exponent
            exponent += 1
        return int(result)
    elif base == 14:
        for digit in number[::-1]:
            if digit.isalpha() and digit.upper() not in letter_list[0:4]:
                return 'error'
            elif digit.upper() == letter_list[0]:
                digit = 10
            elif digit.upper() == letter_list[1]:
                digit = 11
            elif digit.upper() == letter_list[2]:
                digit = 12
            elif digit.upper() == letter_list[3]:
                digit = 13
            result += int(digit) * base ** exponent
            exponent += 1
        return int(result)
    elif base == 15:
        for digit in number[::-1]:
            if digit.isalpha() and digit.upper() not in letter_list[0:5]:
                return 'error'
            elif digit.upper() == letter_list[0]:
                digit = 10
            elif digit.upper() == letter_list[1]:
                digit = 11
            elif digit.upper() == letter_list[2]:
                digit = 12
            elif digit.upper() == letter_list[3]:
                digit = 13
            elif digit.upper() == letter_list[4]:
                digit = 14
            result += int(digit) * base ** exponent
            exponent += 1
        return int(result)
    elif base == 16:
        for digit in number[::-1]:
            if digit.isalpha() and digit.upper() not in letter_list:
                return 'error'
            elif digit.upper() == letter_list[0]:
                digit = 10
            elif digit.upper() == letter_list[1]:
                digit = 11
            elif digit.upper() == letter_list[2]:
                digit = 12
            elif digit.upper() == letter_list[3]:
                digit = 13
            elif digit.upper() == letter_list[4]:
                digit = 14
            elif digit.upper() == letter_list[5]:
                digit = 15
            result += int(digit) * base ** exponent
            exponent += 1
        return int(result)
# else statement that performs conversion if the number gived is not alphanumeric.
    else: 
        for digit in number[::-1]:
            if digit.isalpha():
                return 'error'
            result += int(digit) * base ** exponent
            exponent += 1
        return int(result)


# defines a function that convert a number with a base between 2 and 16 to base 10.
def base_10_to_arbitrary_base(number,base):

    if base > 16 or base < 2:
        return 'base out of range'

    result = ''
# series of conditionals that, in base of the number system choosen, control execution's flow.
    if base == 11:
# while loop that divides the number for the base, store the remainder as result and eventually translate letters to perform the conversion.
        while number != 0:
            remainder = int(number % base)
            if remainder == 10:
                remainder = 'A'
            result += str(remainder)
            number = number // base
# once while loop ends return the result inverted, so we have the number converted.
        return result[::-1]
    elif base == 12:
        while number != 0:
            remainder = int(number % base)
            if remainder == 10:
                remainder = 'A'
            elif remainder == 11:
                remainder = 'B'
            result += str(remainder)
            number = number // base
        return result[::-1]
    elif base == 13:
        while number != 0:
            remainder = int(number % base)
            if remainder == 10:
                remainder = 'A'
            elif remainder == 11:
                remainder = 'B'
            elif remainder == 12:
                remainder = 'C'
            result += str(remainder)
            number = number // base
        return result[::-1]
    elif base == 14:
        while number != 0:
            remainder = int(number % base)
            if remainder == 10:
                remainder = 'A'
            elif remainder == 11:
                remainder = 'B'
            elif remainder == 12:
                remainder = 'C'
            elif remainder == 13:
                remainder = 'D'
            result += str(remainder)
            number = number // base
        return result[::-1]
    elif base == 15:
        while number != 0:
            remainder = int(number % base)
            if remainder == 10:
                remainder = 'A'
            elif remainder == 11:
                remainder = 'B'
            elif remainder == 12:
                remainder = 'C'
            elif remainder == 13:
                remainder = 'D'
            elif remainder == 14:
                remainder = 'E'
            result += str(remainder)
            number = number // base
        return result[::-1]
    elif base == 16:
        while number != 0:
            remainder = int(number % base)
            if remainder == 10:
                remainder = 'A'
            elif remainder == 11:
                remainder = 'B'
            elif remainder == 12:
                remainder = 'C'
            elif remainder == 13:
                remainder = 'D'
            elif remainder == 14:
                remainder = 'E'
            elif remainder == 15:
                remainder = 'F'
            result += str(remainder)
            number = number // base
        return result[::-1]
    else:
# else statements that performs conversion if number gived is not alphanumeric.
        while number != 0:
            remainder = int(number % base)
            result += str(remainder)
            number = number // base
        return result[::-1]
    
# defines a main program that asks to user a number to convert ( with his base) and a base to perform the conversion, using the functions already defined. If user choose a base outside the range between 2 and 16 it displays an error message.
def main():

    number = int(input('Enter a number to convert: '))

    base_of_number = int(input('Enter base of number: '))

    if base_of_number > 16 or base_of_number < 2:
        return 'base out of range'
    
    base_conversion = int(input ('Enter base for conversion: '))

    if base_conversion > 16 or base_conversion < 2:
        return 'base out of range'

    first_step = arbitrary_to_base_10(number, base_of_number)
    
    result = base_10_to_arbitrary_base(first_step, base_conversion)
    
    print(result)


main()