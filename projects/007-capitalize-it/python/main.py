
#defines a function that capitalize the first non-space character of a string, first non-space character after a period, question mark or exclamation mark, and lowercase 'i' preceded by a space and followed by a space, period, exclamation mark, question mark or apostrophe
def capitalize_it(string):

# for loop that capitalizes the first non-space character
    first_letter = ''
    counter = 0
    for i in string:
        if i == ' ' and counter == 0:
            first_letter += i
        elif i != ' ':
            counter += 1
        if counter == 1:
            first_letter += i.upper()
        elif counter > 1:
            first_letter += i

# for loop that capitalizes the first non space character after a period, a question or exclamation mark
    punctuation_string = ''

    question_counter = 0

    for e in first_letter:
        if e == '?' or e == '!' or e == '.':
            question_counter += 1
            punctuation_string += e
        elif question_counter == 1 and e == ' ':
            punctuation_string += e
        elif question_counter == 1 and e != ' ':
            punctuation_string += e.upper()
            question_counter -= 1
        elif question_counter == 0:
            punctuation_string += e

# for loop that capitalizes a lowercase 'i' preceded by a space and followed by a space or a period or question and exclamation mark
    string_i = ''

    for a in range(0, len(punctuation_string)):
        if punctuation_string[a] == 'i' and punctuation_string[a - 1] == ' ' and punctuation_string[a + 1] == ' ':
            string_i += punctuation_string[a].upper()
        elif punctuation_string[a] == 'i' and punctuation_string[a - 1] == ' ' and punctuation_string[a + 1] == "'":
            string_i += punctuation_string[a].upper()
        elif punctuation_string[a] == 'i' and punctuation_string[a - 1] == ' ' and punctuation_string[a + 1] == '!':
            string_i += punctuation_string[a].upper()
        elif punctuation_string[a] == 'i' and punctuation_string[a - 1] == ' ' and punctuation_string[a + 1] == '?':
            string_i += punctuation_string[a].upper()
        else:
            string_i += punctuation_string[a]


    return(string_i)


# main program that asks a string to the user then print it on screen capitalized
def main():
    string = input('Enter a string: ')
    print(capitalize_it(string))

main()
