import os

def center_string(string,width):
    if len(string)<width:
        add_spaces=(len(string)-width)//2*(-1)
        new_string=" "*add_spaces+string
        return new_string
    else:
        return string

input_string=input("Enter a string: ")
width=os.get_terminal_size().columns

while input_string!="":
    new_string=center_string(input_string,width)
    print(new_string)
    input_string=input("Enter a string (blank to quit):")