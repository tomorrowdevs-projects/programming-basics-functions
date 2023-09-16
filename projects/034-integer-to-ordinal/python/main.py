def get_ordinal_number(integer):
    ordinal_numbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    
    if 1 <= integer <= 12:
        return ordinal_numbers[integer - 1]
    else:
        return ""
