'''
Many recipe books still use cups, tablespoons and teaspoons to describe the volumes of ingredients used when cooking or baking.

While such recipes are easy enough to follow if you have the appropriate measuring cups and spoons, they can be difficult to double, triple or quadruple when cooking Christmas dinner for the entire extended family.

For example, a recipe that calls for 4 tablespoons of an ingredient requires 16 tablespoons when quadrupled.
However, 16 tablespoons would be better expressed (and easier to measure) as 1 cup.

Write a function named reduce measures that expresses an imperial volume using the largest units possible.
The function will take the number of units as its first parameter, and the unit of measure (cup, tablespoon or teaspoon) as its second parameter. It will return a string representing the measure using the largest possible units as its only result.

Example
units: 59
unit_measure: teaspoons
output: 1 cup, 3 tablespoons, 2 teaspoons
'''

def reduce_measures(userunits, userunitmeasure):
    if userunitmeasure == "teaspoons":
        teaspoons = userunits
        print("Teaspoons: ", teaspoons)
    elif userunitmeasure == "tablespoons":
        tablespoons = userunits // 4
        teaspoons = userunits - (4 * tablespoons)
        print("Tablespoons: ", tablespoons, "teaspoons: ", teaspoons)
    elif userunitmeasure == "cups":
        cups = userunits // 16
        newunits = userunits - (16 * cups)
        tablespoons = newunits // 4
        teaspoons = newunits - (4 * tablespoons)
        print("Cups: ", cups, "tablespoons: ", tablespoons, "teaspoons: ", teaspoons)
   
userunits = int(input("Please input how many units you need to create: "))
userunitmeasure = str(input("Please input the unit measure you want to use (cups, tablespoons, teaspoons): "))
finalconversion = reduce_measures(userunits, userunitmeasure)
