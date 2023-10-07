# Capitalize It

Many people do not use capital letters correctly, especially when typing on small devices like smartphones.   
To help address this situation, you will create a function named **capitalize it** that 
takes a string as its only parameter and returns a new copy of the string that has been correctly capitalized. 

In particular, your function must:
- Capitalize the first non-space character in the string,
- Capitalize the first non-space character after a period, exclamation mark or question mark,
- Capitalize a lowercase “i” if it is preceded by a space and followed by a space, period, exclamation mark, question mark or apostrophe.

Implementing these transformations will correct most capitalization errors. 

Example:   
input:   
“what time do I have to be there? what’s the address? this time I’ll try to be on time!”   
output:   
“What time do I have to be there? What’s the address? This time I’ll try to be on time!”. 

Include a main program that reads a string from the user, 
capitalizes it using your function, and displays the result.


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
python -m unittest python/test_capitalize_it.py
```

or run the command from the terminal  
`python -m unittest projects/007-capitalize-it/python/test_capitalize_it.py`



# Deadline

This project requires to be completed in a maximum of **2 hours**
