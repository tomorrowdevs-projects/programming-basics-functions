
def center_string(string: str, window_width: int)-> str:
    '''Returns a new centered string given a string and a value representing the width of a screen as parameters. Returns the string itself if string is larger than the screen.
            :parameter: 
                    string(str): any string.
                    window_width(int): a number representing the width.
            :return: 
                    centered_string(str): the new centered string.
    '''
    string_width = len(string)
    
    if string_width >= window_width:
        return string
    else:
        space = (window_width - string_width) // 2
        centered_string = ' ' * space + string

    return centered_string

def main():
    '''main program that prints some examples'''
    print(center_string('coding', 10))
    print(center_string('hello', 15))
    print(center_string('python', 2))


if __name__ == '__main__':
    main()