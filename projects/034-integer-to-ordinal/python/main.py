def get_ordinal_number(integer):
    ordinal_numbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    for number in range(1, 13):
        if integer == number:
            number -= 1
            print(ordinal_numbers[number])
    else:
        print('')