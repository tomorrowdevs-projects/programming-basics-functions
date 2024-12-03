def arbitrary_to_base_10(string: str, base: int) -> int:
    number_base_10=0
    exponent=0
    for character in string[::-1]:
        if character.isdecimal(): 
            partial_sum=int(character)*base**exponent
            number_base_10+=partial_sum
            exponent+=1
        elif ord(character)>=65 and ord(character)<=70:
            integer=(ord(character)-65)+10
            partial_sum=integer*base**exponent
            number_base_10+=partial_sum
            exponent+=1
        else:
            integer=(ord(character)-97)+10
            partial_sum=integer*base**exponent
            number_base_10+=partial_sum
            exponent+=1
    return number_base_10

def base_10_to_arbitrary_base(number_base_10: int, base: int) -> str:
    quotient=number_base_10
    number_string=""
    while quotient!=0:
        remainder=quotient%base
        quotient//=base
        if remainder>9:
            remainder=chr((remainder-10)+65)
        number_string+=str(remainder)
    return number_string[::-1]


while True:
    try:
        start_base=int(input("Enter a start base (between 2 and 16): "))
        break
    except ValueError:
        print("Invalid input!")

while True:
    try:
        destination_base=int(input("Enter a destination base (between 2 and 16): "))
        break
    except ValueError:
        print("Invalid input!")

if (start_base>=2 and start_base<=16) and (destination_base>=2 and destination_base<=16): 

    number_string=input("Enter a number: ")
    if start_base<=10:
        is_valid_input=False
        while not(is_valid_input):
            for character in number_string:
                if character.isdecimal() and int(character)<start_base:
                    is_in_range=True
                else:
                    is_in_range=False
                    break
            if is_in_range==True:
                is_valid_input=True
            else:           
                number_string=input("Invalid input! Enter a new number: ")
    else:
        is_valid_input=False
        while not(is_valid_input):
            for character in number_string:
                if character.isdecimal():
                    is_in_range=True
                elif (ord(character)>=65 and ord(character)<=70) and (ord(character)-65)+10<start_base:
                    is_in_range=True
                elif (ord(character)>=97 and ord(character)<=102) and (ord(character)-97)+10<start_base:
                    is_in_range=True
                else:
                    is_in_range=False
                    break
            if is_in_range==True:
                is_valid_input=True
            else:
                number_string=input("Invalid input! Enter a new number: ")         

    number_base_10=arbitrary_to_base_10(number_string, start_base)
   
    result_number=base_10_to_arbitrary_base(number_base_10,destination_base)
    
    print(f"{number_string} (base {start_base}) = {result_number} (base {destination_base})")

else:
    print("You chose a base outside of expected range!")