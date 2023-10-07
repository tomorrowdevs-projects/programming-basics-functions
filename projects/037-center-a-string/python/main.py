def centered_string(string, window_width):
    string_width = len(string)

    if string_width >= window_width:
        return f'The string\'s width is larger then window\'s size : {string_width}'
    else:
        leading_space = (window_width - string_width) // 2
        centered_string = ' ' * leading_space + string

    return centered_string
    
def main():
    user_string = input('Type a string: ')
    window_width = int(input('Type window\'s width: '))
    print(centered_string(user_string,window_width))

main()