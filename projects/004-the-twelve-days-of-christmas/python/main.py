def integer_to_ordinal(integer):
    if integer==1:
        result="first"
    elif integer==2:
        result="second"
    elif integer==3:
        result="third"
    elif integer==4:
        result="fourth"
    elif integer==5:
        result="fifth"
    elif integer==6:
        result="sixth"
    elif integer==7:
        result="seventh"
    elif integer==8:
        result="eighth"
    elif integer==9:
        result="ninth"
    elif integer==10:
        result="tenth"
    elif integer==11:
        result="eleventh"
    elif integer==12:
        result="twelfth"
    return result

def twelve_days_of_christmas(verse_number):
    global gift
    if verse_number==1:
        gift="A partridge in a pear tree."
    elif verse_number==2:
        gift="Two turtle doves, And a partridge in a pear tree."
    elif verse_number==3:
        gift="Three French hens, "+gift
    elif verse_number==4:
        gift="Four calling birds, "+gift
    elif verse_number==5:
        gift="Five gold rings, "+gift
    elif verse_number==6:
        gift="Six geese a-laying, "+gift
    elif verse_number==7:
        gift="Seven swans a-swimming, "+gift
    elif verse_number==8:
        gift="Eight maids a-milking, "+gift
    elif verse_number==9:
        gift="Nine ladies dancing, "+gift
    elif verse_number==10:
        gift="Ten lords a-leaping, "+gift
    elif verse_number==11:
        gift="Eleven pipers piping, "+gift
    elif verse_number==12:
        gift="Twelve drummers drumming, "+gift
    return gift

for i in range(1,13):
    ordinal_number=integer_to_ordinal(i)
    gift=twelve_days_of_christmas(i)
    print(f"On the {ordinal_number} day of Christmas my true love sent to me: {gift}\n")