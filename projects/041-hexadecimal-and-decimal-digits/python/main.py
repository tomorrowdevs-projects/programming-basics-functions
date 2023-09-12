def hex2int(string):
    hexadecimal_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if string.upper() not in hexadecimal_digits:
        return ValueError("Invalid digit! It must include one of these digits: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F)")
    else:
        return int(string, 16)

def int2hex(integer):
    if integer not in range(0, 16):
        return ValueError('Invalid digit! It must be between 0 and 15')
    else:
        return hex(integer)