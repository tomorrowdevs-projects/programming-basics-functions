def get_ordinal_number(integer):
    ordinal_numbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    if 1 <= integer <= 12:
        return ordinal_numbers[integer - 1]
    else:
        return ""


def verse_of_the_song(verse_number):
    items = ["a partridge in a pear tree", "two turtle doves", "three French hens", "four calling birds",
             "five gold rings", "six geese a-laying", "seven swans a-swimming", "eight maids a-milking",
             "nine ladies dancing", "10 lords a-leaping", "11 pipers piping", "12 drummers drumming"]
    verse = []
    day = verse_number

    if verse_number > 1:
        while verse_number != 1:
            verse.append(items[verse_number - 1])
            verse_number -= 1
        print(f"On the {get_ordinal_number(day)} day of Christmas my true love sent to me:",', '.join(verse), 'and a partridge in a pear tree!\n')
    else:
        print(f"On the {get_ordinal_number(day)} day of Christmas my true love sent to me: a partridge in a pear tree!\n")

def the_twelve_days_of_christmas():
    for day in range(1, 13):
        print(f'{get_ordinal_number(day)} day')
        verse_of_the_song(day)

the_twelve_days_of_christmas()
