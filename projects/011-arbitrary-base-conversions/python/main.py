def arbitrary_to_base_10(number,base):
    letters={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    decimal=0
    exp=len(number)-1
    for i in number:
        if not i.isdecimal():
            decimal+=letters[i]
        else:
            decimal+=int(i)*base**exp
        exp-=1
    return decimal

def base_10_to_arbitrary_base(number,base):
    letters={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    result=''
    while number>0:
        if base>10:
            r=number%base
            if 10<=r<=base:
                r=letters[r]
            result=str(r)+result
            number=number//base
        else:
            r=number%base
            result=str(r)+result
            number=number//base
    return result

def main():
    input_base=input('Please, enter the input base:')
    input_base=int(input_base)
    if not input_base in range(2,17):
        print('Please enter a base between 2 and 16')
        return
    
    input_number=input('Please, enter the input number:')

    output_base=input('Please, enter the output base:')
    output_base=int(output_base)
    if not output_base in range(2,17):
        print('Please enter a base between 2 and 16')
        return
    
    decimal=arbitrary_to_base_10(input_number,input_base)
    result=base_10_to_arbitrary_base(decimal,output_base)
    print('{} in base {} equals {} in base {}'.format(input_number,input_base,result,output_base))

if __name__=='__main__':
    main()