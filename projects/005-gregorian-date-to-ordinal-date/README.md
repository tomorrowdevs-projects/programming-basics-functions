# Gregorian Date to Ordinal Date

An ordinal date consists of a year and a day within it, both of which are integers.   
The year can be any year in the Gregorian calendar while the day within the year ranges from one, 
which represents January 1, through to 365 (or 366 if the year is a leap year) which represents December 31. 

Ordinal dates are convenient when computing differences between dates that are a 
specific number of days(rather than months).    
For example, ordinal dates can be used to easily determine whether a customer is within a 90-day return period, 
the sell-by date for a food-product based on its production date, and the due date for a baby.

Write a function named **gregorian_to_ordinal_date** that takes three **integers** as parameters:
- day
- month
- year

The function should return the day within the year for that date as its only result.   

Create a main program that reads a day, month and year from the user and displays the day within the year for that date.    
Also, your program must also consider the leap year.  
Your main program should only run when your file has not been imported into another program. 

# Documentation
[The Gregorian Calendar](https://www.timeanddate.com/calendar/gregorian-calendar.html)   
[Ordinal Day Calendar](https://landweb.modaps.eosdis.nasa.gov/browse/calendar.html)

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
python -m unittest python/test_gregorian_date_to_ordinal_date.py
```

or run the command from the terminal  
`python -m unittest projects/005-gregorian-date-to-ordinal-date/python/test_gregorian_date_to_ordinal_date.py`



# Deadline

This project requires to be completed in a maximum of **2 hours**
