
def center_string(string, window_width):
    '''
    given a string and an integer as window width, returns a centered string if the window width is greater than the string length, or the same string if equal or lower
    '''
    string_width = len(string)

    if string_width >= window_width:
        return string
    else:
        space = (window_width - string_width) // 2
        centered_string = ' ' * space + string

    return centered_string

def main():
    '''
    main program printing on the screen some examples 
    '''
    print(center_string('coding', 10))
    print(center_string('hello', 15))
    print(center_string('python', 2))

main()