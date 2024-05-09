def integer_to_ordinal(number):
    ordinal_number=['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
    if not number in range(1,13):
        number=''
    else:
        number=ordinal_number[number-1]
    return number

def main():
    for i in range(1,13):
        number=int(i)
        ordinal=integer_to_ordinal(number)
        print('{} - {}'.format(number,ordinal))

if __name__=='__main__':
    main()