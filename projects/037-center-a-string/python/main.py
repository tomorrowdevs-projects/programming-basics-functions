def center_a_string(s, w):
    if len(s) >= w:
        return s
    else:
        spaces_number = (w - len(s)) // 2
        new_string = " " * spaces_number + s
        return new_string

def main():
    user_string = input("Enter your string here:\n")
    window_width = int(input('Enter the width of the window:\n'))
    centered_string = center_a_string(user_string, window_width)
    print(centered_string)

if __name__ == '__main__':
    main()
