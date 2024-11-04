def capitalize_it(string):
    new_string=""

    first_index_capitalize=len(string)-len(string.lstrip())
    index=0
    while index<len(string):
        character=string[index]

        if index==first_index_capitalize:
            character=character.upper()

        elif index!=0 and (string[index-1]=="." or string[index-1]=="?" or string[index-1]=="!"):
            is_capitalize=False 
            while not(is_capitalize) and index<len(string):
                character=string[index]
                if character!=" ":
                    character=character.upper()
                    is_capitalize=True
                else:    
                    new_string+=character
                    index+=1
        
        elif character=="i" and index!=len(string)-1:
            if string[index-1]==" " and (string[index+1]==" " or string[index+1]=="." or string[index+1]=="!" or string[index+1]=="?" or string[index+1]=="'"):
                character=character.upper() 
                
        new_string+=character
        index+=1
    return new_string

input_string=input("Enter a string: ")

new_string=capitalize_it(input_string)
print(new_string)