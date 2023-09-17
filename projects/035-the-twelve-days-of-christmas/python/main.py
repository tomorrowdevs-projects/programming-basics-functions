# defines a function that gived an integer between one and twelve, return the ordinal number
def integer_to_ordinal(integers):
    if integers == 1:
        return 'first'
    elif integers == 2:
        return 'second'
    elif integers == 3:
        return 'third'
    elif integers == 4:
        return 'fourth'
    elif integers == 5:
        return 'fifth'
    elif integers == 6:
        return 'sixth'
    elif integers == 7:
        return 'seventh'
    elif integers == 8:
        return 'eighth'
    elif integers == 9:
        return 'nineth'
    elif integers == 10:
        return 'tenth'
    elif integers == 11:
        return 'eleventh'
    elif integers == 12:
        return 'twelfth'
    
# defines a function that display a single verse of the song "The twelve days of Christmas" with hte only parameter a number between one and twelve 

def christmas_song_verse(verse):

    first_part = f'On the {integer_to_ordinal(verse)} day of Christmas my true love sent to me:'

    ending_part = ' and a partridge in a pear tree.'

    if verse == 1:
        print(f'{first_part} A partridge in a pear tree.\n')
    elif verse == 2:
        print(f'{first_part} two turtle doves,{ending_part}\n')
    elif verse == 3:
        print(f'{first_part} three French hens, two turtle doves,{ending_part}\n')
    elif verse == 4:
        print(f'{first_part} four calling birds, three French hens, two turtle doves,{ending_part}\n')
    elif verse == 5:
        print(f'{first_part} five golden rings, four calling birds, three French hens, two turtle doves,{ending_part}\n')
    elif verse == 6:
        print(f'{first_part} six geese-a-laying, four calling birds, three French hens, two turtle doves,{ending_part}\n')
    elif verse == 7:
        print(f'{first_part} seven swans a-swimming, six geese-a-laying, four calling birds, three French hens, two turtle doves,{ending_part}\n')
    elif verse == 8:
        print(f'{first_part} eight maids a-milking, seven swans-a-swimming, six geese-a-laying, four calling birds, three French hens, two turtle doves,{ending_part}\n')
    elif verse == 9:
        print(f'{first_part} nine ladies dancing, eight maids-a-milking, seven swans-a-swimming, six geese-a-laying, four calling birds, three French hens, two turtle doves,{ending_part}\n')
    elif verse == 10:
        print(f'{first_part} ten lords a leaping, nine ladies dancing,eight maids-a-milking, seven swans-a-swimming, six geese-a-laying, four calling birds, three French hens, two turtle doves,{ending_part}\n')
    elif verse == 11:
        print(f'{first_part} eleven pipers piping, ten lords a leaping, nine ladies dancing, eight maids-a-milking, seven swans-a-swimming, six geese-a-laying, four calling birds, three French hens, two turtle doves,{ending_part}\n')
    elif verse == 12:
        print(f'{first_part}  Twelve drummers drumming, eleven pipers piping, ten lords a leaping, nine ladies dancing,eight maids-a-milking, seven swans-a-swimming, six geese-a-laying, four calling birds, three French hens, two turtle doves,{ending_part}\n')

#for loop that displays the whole song using the function already defined
   
for i in range(1,13):

    christmas_song_verse(i)


    