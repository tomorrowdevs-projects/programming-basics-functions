def center_a_string(s, w):
    if len(s) >= w:
        return s
    else:
        spaces_number = (w - len(s)) // 2
        new_string = " " * spaces_number + s
        return new_string
