from shutil import get_terminal_size

def center_string(s, w):
    if len(s) >= w:
        return s
    else:
        center = (w - len(s)) // 2
        centered_string = ' ' * center + s
        return centered_string
    

def main():
    string_to_print = ['On the twelfth day of Christmas, my true love gave (sent) to me two turtle doves', 'Hello, world!']
    window_width = get_terminal_size().columns

    for string in range(len(string_to_print)):
        print(center_string(string_to_print[string], window_width))


if __name__ == '__main__':
    main()