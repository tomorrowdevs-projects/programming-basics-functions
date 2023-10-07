# defines a function that return the ordinal number from integer
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

#assigns a variable for every single item of the song
gift_one =  ' a partridge in a pear tree'
gift_two =  ' two turtle doves'
gift_three = ' three French hens'
gift_four = ' four calling birds'
gift_five = ' five golden rings'
gift_six = ' six geese-a-laying'
gift_seven = ' seven swans-a-swimming'
gift_eight = ' eight maids-a-milking'
gift_nine = ' nine ladies dancing'
gift_ten = ' ten lords a leaping'
gift_eleven = ' eleven pipers piping'
gift_twelve = ' twelve drummers drumming'

#defines a function that take a integer as the number of the verse and return verse 
def verse(number):
    number = int(number)

    first_part = f'On the {integer_to_ordinal(number)} day of Christmas my true love sent to me:'

    if number == 1:
        return first_part + gift_one + '.'
    elif number == 2:
        return first_part + gift_two + ', and' + gift_one + '.'
    elif number == 3:
        return first_part + gift_three + ',' + gift_two + ', and' + gift_one + '.'   
    elif number == 4:
        return first_part + gift_four + ',' + gift_three + ',' + gift_two + ', and' + gift_one + '.'
    elif number == 5:
        return first_part + gift_five + ',' + gift_four + ',' + gift_three + ',' + gift_two + ', and' + gift_one + '.'
    elif number == 6:
        return first_part + gift_six + ',' + gift_five + ',' + gift_four + ',' + gift_three + ',' + gift_two + ', and' + gift_one + '.'
    elif number == 7:
        return first_part + gift_seven + ',' + gift_six + ',' + gift_five + ',' + gift_four + ',' + gift_three + ',' + gift_two + ', and' + gift_one + '.'
    elif number == 8:
        return first_part + gift_eight + ',' + gift_seven + ',' + gift_six + ',' + gift_five + ',' + gift_four + ',' + gift_three + ',' + gift_two + ', and' + gift_one + '.'
    elif number == 9:
        return first_part + gift_nine + ',' + gift_eight + ',' + gift_seven + ',' + gift_six + ',' + gift_five + ',' + gift_four + ',' + gift_three + ',' + gift_two + ', and' + gift_one + '.'
    elif number == 10:
        return first_part + gift_ten + ',' + gift_nine + ',' + gift_eight + ',' + gift_seven + ',' + gift_six + ',' + gift_five + ',' + gift_four + ',' + gift_three + ',' + gift_two + ', and' + gift_one + '.'
    elif number == 11:
        return first_part + gift_eleven + ',' + gift_ten + ',' + gift_nine + ',' + gift_eight + ',' + gift_seven + ',' + gift_six + ',' + gift_five + ',' + gift_four + ',' + gift_three + ',' + gift_two + ', and' + gift_one + '.'
    elif number == 12:
        return first_part + gift_twelve + ',' + gift_eleven + ',' + gift_ten + ',' + gift_nine + ',' + gift_eight + ',' + gift_seven + ',' + gift_six + ',' + gift_five + ',' + gift_four + ',' + gift_three  + ',' + gift_two + ', and' + gift_one + '.'

# defines a function that display the whole song using the previous function
def Christmas_song():
    for i in range(1,13):
        print(verse(i))


Christmas_song()