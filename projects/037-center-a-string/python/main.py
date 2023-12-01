
def centered_string(string, window_width):
    string_width = len(string)

    if string_width >= window_width:
        return string
    else:
        space = (window_width - string_width) // 2
        centered_string = ' ' * space + string + ' ' * space

    return centered_string
    
def main():
    print(centered_string('coding', 10))
    print(centered_string('hello', 15))
    print(centered_string('python', 2))

main()