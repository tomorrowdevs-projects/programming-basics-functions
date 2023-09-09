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

        elif letter == 'i' and message[i - 1] == ' ' or letter == 'i' and message[i + 1] in ['!', '?', '.', "'", ' ']:
            new_message = new_message[:-1] + 'I'

    return new_message
