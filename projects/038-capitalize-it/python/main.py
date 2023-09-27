def capitalize_it(message):
    capitalize = True
    new_message = ''

    for i, letter in enumerate(message):

        if capitalize:
            if letter.isalpha():
                new_message += letter.upper()
                capitalize = False
            else:
                new_message += letter
        else:
            new_message += letter.lower()

        if letter in ['!', '?', '.']:
            capitalize = True

        elif letter == 'i' and message[i - 1] == ' ' and message[i - 2] in ['!', '?', '.', "'", ' '] or letter == 'i' and message[i + 1] in ['!', '?', '.', "'", ' ']:
            new_message = new_message[:-1] + 'I'

    return new_message

def main():
    user_string = input("Enter your message:\n")
    correct_message = capitalize_it(user_string)
    print(correct_message)

if __name__ == '__main__':
    main()
