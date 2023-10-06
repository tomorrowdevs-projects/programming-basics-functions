def capitalize_it(string):
    string = list(string)
    for index in range(len(string)):
        
        string[0] = string[0].upper()

        if string[index] == ' ':
            if string[index - 1] in ['.', '?', '!'] and string[index] != string[-1]:
                string[index + 1] = string[index + 1].upper()
            
        if string[index] == 'i' and string[index - 1] == ' ' and (string[index + 1] == "'" or string[index + 1] == ' '):
            string[index] = string[index].upper()
    
    new_string = ''
    for element in string:
        new_string += element
    
    return new_string


def main():
    string = (input('Enter a phrase: '))
    print(capitalize_it(string))


if __name__ == '__main__':
    main()