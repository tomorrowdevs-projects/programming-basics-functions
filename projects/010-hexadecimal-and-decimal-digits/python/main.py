import sys

def hex2int(hexadecimal_digit):     
    if len(hexadecimal_digit)==1:

        hexadecimal_digit=ord(hexadecimal_digit)

        if hexadecimal_digit>47 and hexadecimal_digit<58:
            integer=int(chr(hexadecimal_digit))
            return integer

        elif hexadecimal_digit>64 and hexadecimal_digit<71:
            integer=(hexadecimal_digit-65)+10
            return integer

        elif hexadecimal_digit>96 and hexadecimal_digit<103:
            integer=(hexadecimal_digit-97)+10
            return integer
           
        else:
            sys.exit("The parameter’s value is outside the expected range.")             
    else:
        sys.exit("The parameter’s value is outside the expected range.") 


def int2hex(integer):
    if integer.isdigit():

        integer=int(integer)
        if integer>-1 and integer<10:
            hexadecimal_digit=integer
            return hexadecimal_digit
        
        if integer>9 and integer<16:
            hexadecimal_digit=chr((integer-10)+65)
            return hexadecimal_digit
        else:
            sys.exit("The parameter’s value is outside the expected range.")
    else:
        sys.exit("The parameter’s value is outside the expected range.")


hexadecimal_digit=input("Enter a single hexadecimal digit to convert to a base 10 integer: ")
result_hex2int=hex2int(hexadecimal_digit)
print(f"{hexadecimal_digit} = {result_hex2int} (base 10 integer)")

integer=input("Enter an integer between 0 and 15 to convert to a single hexadecimal digit: ")
result_int2hex=int2hex(integer)
print(f"{integer} = {result_int2hex} (base hexadecimal)")