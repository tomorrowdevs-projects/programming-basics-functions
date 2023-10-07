from IntOrd import integer_to_ordinal

def gift(num_verse):
    gift_ls = ['a partridge in a pear tree.', 'two turtle doves.', 'three french hens.', 'four calling (colly) birds.', 
               'five golden (gold) rings.', 'six geese a-laying.', 'seven swans a-swimming.', 'eight maids a-milking.', 
               'nine ladies dancing.', 'ten lords a-leaping.', 'eleven pipers piping.', 'twelve drummers drumming.']
    
    return gift_ls[num_verse - 1]


def print_verse(num_verse):
    print(f'On the {integer_to_ordinal(num_verse)} day of Christmas, my true love sent to me {gift(num_verse)}')


def main():
    for num_verse in range(1, 13):
        print_verse(num_verse)


if __name__ == '__main__':
    main()