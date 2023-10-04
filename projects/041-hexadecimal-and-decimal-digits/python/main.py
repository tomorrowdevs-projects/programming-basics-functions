import string
def hex2int(string):
    hexadecimal_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if string.upper() not in hexadecimal_digits:
        raise ValueError("Invalid digit! It must include one of these digits: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F)")
    else:
        return int(string, 16)

def int2hex(integer):
    if integer not in range(0, 16):
        raise ValueError('Invalid digit! It must be between 0 and 15')
    else:
        hexadecimal_digits = 0

        while integer != 0:
            rest = integer % 16
            if rest > 9:
                rest = string.ascii_uppercase[rest - 10]

            hexadecimal_digits = str(rest)
            integer = integer // 16

        return hexadecimal_digits
