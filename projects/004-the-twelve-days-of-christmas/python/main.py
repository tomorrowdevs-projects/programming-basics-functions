'''
The Twelve Days of Christmas is a repetitive song that describes an increasingly long list of gifts sent to one’s true love on each of 12 days.
A single gift is sent on the first day. A new gift is added to the collection on each additional day, and then the complete collection is sent. The first three verses of the song are shown below.
The complete lyrics are available on the Internet.

*On the first day of Christmas my true love sent to me:
A partridge in a pear tree.*

*On the second day of Christmas my true love sent to me:
Two turtle doves,
And a partridge in a pear tree.*

*On the third day of Christmas my true love sent to me: 
Three French hens,
Two turtle doves,
And a partridge in a pear tree.*

Write a program that displays the complete lyrics for The Twelve Days of Christmas.  

Your program should include a function that displays one verse of the song.   
It will take the verse number as its only parameter.   
Then your program should call this function 12 times with integers that increase from 1 to 12.   

Each item that is sent to the recipient in the song should only appear in your program once,
with the possible exception of the partridge. 

It may appear twice if that helps you handle the difference between 
“A partridge in a pear tree” in the first verse and “And a partridge in a pear tree” 
in the subsequent verses.    
You can even import your solution to Exercise 034 to help you complete this exercise.
'''

def lyrics(verse):
    if verse == 1:
        print("On the first day of Christmas my true love sent to me: \nA partridge in a pear tree.")
    elif verse == 2:
        print("On the second day of Christmas \nMy true love sent to me \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 3:
        print("On the third day of Christmas \nMy true love sent to me \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 4:
        print("On the fourth day of Christmas \nMy true love sent to me \nFour calling birds \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 5:
        print("On the fifth day of Christmas \nMy true love sent to me \nFive golden rings! \nFour calling birds \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 6:
        print("On the sixth day of Christmas \nMy true love sent to me \nSix geese a layin' \nFive golden rings! \nFour calling birds \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 7:
        print("On the seventh day of Christmas \nMy true love sent to me \nSeven swans a swimmin' \nSix geese a layin' \nFive golden rings! \nFour calling birds \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 8:
        print("On the eighth day of Christmas \nMy true love sent to me \nEight maids a milkin' \nSeven swans a swimmin' \nSix geese a layin' \nFive golden rings! \nFour calling birds (calling birds) \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 9:
        print("On the ninth day of christmas \nMy true love sent to me \nNine ladies dancin' \nEight maids a milkin' \nSeven swans a swimmin' \nSix geese a layin' \nFive golden rings! \nFour calling birds \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 10:
        print("On the tenth day of Christmas \nMy true love sent to me \nTen lords a leapin' \nNine ladies dancin' \nEight maids a milkin' \nSeven swans a swimmin' \nSix geese a layin' \nFive golden rings! \nFour calling birds \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 11:
        print("On the eleventh day of Christmas \nMy true love sent to me \nEleven pipers pipin' \nTen lords a leapin' \nNine ladies dancin' \nEight maids a milkin' \nSeven swans a swimmin' \nSix geese a layin' \nFive golden rings! \nFour calling birds \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")
    elif verse == 12:
        print("On the twelfth day of Christmas \nMy true love sent to me \nTwelve drummers drummin' \nEleven pipers pipin' \nTen lords a leapin' \nNine ladies dancin' \nEight maids milkin' \nSeven swans a swimmin' \nSix geese a layin' \nFive golden rings! \nFour calling birds \nThree french hens \nTwo turtle doves \nAnd a partridge in a pear tree!")

verse = 1
for n in range(12):
    lyrics(verse)
    verse += 1
