'''
Write a function named **center string** that takes:    
- string, *s*, as its first parameter,  
- width of the window in characters, *w*, as its second parameter. 

Your function will return a new string that includes whatever leading spaces are needed 
so that s will be centered in the window when the new string is printed.   

The new string should be constructed in the following manner:
- If the length of s is greater than or equal to the width of the window then s should be returned.
- If the length of s is less than the width of the window then a string containing *(len(s) - w) // 2* spaces followed by s should be returned.

Write a main program that demonstrates your function by displaying multiple strings centered in the window.
'''

def center_string(s, w):
    lenghts = len(s)
    if lenghts >= w:
        return s
    elif lenghts < w:
        newstring = (len(s) - w) // 2
        return newstring

s = str(input("Please insert a string: "))
w = int(input("Please insert an integer to determine the width of the window: "))
finalstring = center_string(s, w)
print("Final string: ", finalstring)