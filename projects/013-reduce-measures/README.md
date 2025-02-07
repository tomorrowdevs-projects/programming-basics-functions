# Reduce Measures

Many recipe books still use cups, tablespoons and teaspoons 
to describe the volumes of ingredients used when cooking or baking. 

While such recipes are easy enough to follow if you have the appropriate measuring cups and spoons, 
they can be difficult to double, triple or quadruple when cooking Christmas dinner for the entire extended family. 

For example, a recipe that calls for 4 tablespoons of an ingredient requires 16 tablespoons when quadrupled.   
However, 16 tablespoons would be better expressed (and easier to measure) as 1 cup.

Write a function named **reduce measures** that expresses an imperial volume using the largest units possible.  
The function will take the number of units as its first parameter, 
and the unit of measure (**cup, tablespoon or teaspoon**) as its second parameter.
It will return a string representing the measure using the largest possible units as its only result. 

**Example**   
units: 59   
unit_measure: teaspoons   
output: 1 cup, 3 tablespoons, 2 teaspoons

# Documentation

For this project solution you may use:

- Functions
- Conditionals and recursion

# Test
Execute the test to validate your solution.  

**VSCODE**   
To run the test command from the README.md install the extension **runme**. 
Press Ctrl+Shift+x search and install the **runme** extension. 


**Python**

```sh
python -m unittest python/test_reduce_measures.py
```

or run the command from the terminal  
`python -m unittest projects/013-reduce-measures/python/test_reduce_measures.py`



# Deadline

This project requires to be completed in a maximum of **2 hours**