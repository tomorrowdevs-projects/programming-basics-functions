def integer_to_ordinal(num):
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    if num >= 1 and num <= 12:
        for index_ordinal in range(len(ordinal)):
            if (num - 1) == index_ordinal:
                ordinal_number_str = str(ordinal[index_ordinal])
        return ordinal_number_str
    else:
        return ''


def main():
    num = int(input('Enter an integer between 1 and 12: '))
    int_to_ord = integer_to_ordinal(num)
    print(f'Your number as literal ordinal number: {int_to_ord}')
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    for ordinal_index in range(0, len(ordinal)):
        print(f'{ordinal_index + 1}: {ordinal[ordinal_index]}')

if __name__ == '__main__':
    main()