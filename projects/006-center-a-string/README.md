# Center a String in the Terminal Window

Write a function named **center string** that takes:    
- string, *s*, as its first parameter,  
- width of the window in characters, *w*, as its second parameter. 

Your function will return a new string that includes whatever leading spaces are needed 
so that s will be centered in the window when the new string is printed.   

The new string should be constructed in the following manner:
- If the length of s is greater than or equal to the width of the window then s should be returned.
- If the length of s is less than the width of the window then a string containing *(len(s) - w) // 2* spaces followed by s should be returned.

Write a main program that demonstrates your function by displaying multiple strings centered in the window.


# Documentation

For this project solution you may use:

- Functions
- Iterations
- Conditionals and recursion


# Test
Execute the test to validate your solution.  

**VSCODE**   
To run the test command from the README.md install the extension **runme**. 
Press Ctrl+Shift+x search and install the **runme** extension. 


**Python**

```sh
python -m unittest python/test_center_a_string.py
```

or run the command from the terminal  
`python -m unittest projects/006-center-a-string/python/test_center_a_string.py`


# Deadline

This project requires to be completed in a maximum of **2 hours**
