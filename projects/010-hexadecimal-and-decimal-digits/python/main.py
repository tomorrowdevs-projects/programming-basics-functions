def hex2int(hex_number):
    hex_number=hex_number.upper()
    hex_digits=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    dec_numbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    if hex_number in hex_digits:
        index=hex_digits.index(hex_number)
        dec_number=dec_numbers[index]
    else:
        print('You have entered a not expected input, please retry')
    return dec_number

def int2hex(dec_number):
    hex_digits=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if 0<=dec_number<=15:
        hex_number=hex_digits[dec_number]
    else:
        print('You have entered a not expected input, please retry')
    return hex_number