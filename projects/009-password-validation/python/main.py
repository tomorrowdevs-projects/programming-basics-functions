'''
In this exercise you will write a function named is valid password
that determines whether a password is good.
We will define a good password to be a one that is:

at least 8 characters long
contains at least one uppercase letter
contains at least one lowercase letter
contains at least one number
Your function should return True if the password passed to it as its
only parameter is good.
Otherwise it should return False.

Include a main program that reads a password from the user and reports
whether it is good.
Ensure that your main program only runs when your solution has not
been imported into another file.
'''

def valid_password(userpassword, uppercase, lowercase, numbers):
    if len(userpassword) >= 8 and uppercase in userpassword and lowercase in userpassword and numbers in userpassword:
        return True
    else:
        return False
   
userpassword = input("Please enter a password: ")
uppercase = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
lowercase = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
passwordcheck = valid_password(userpassword, uppercase, lowercase, numbers)
if passwordcheck == True:
    print("The password inserted is correct!")
else:
    print("The password inserted is WRONG!\nIt needs to contain at least one uppercase letter, at least one lowercase letter, at least one number and it should be at least 8 characters long!")