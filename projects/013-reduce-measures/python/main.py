def reduce_measures(units: int, unit_measure: str) -> str:
    if unit_measure=="teaspoon":
        cup=units//48
        units%=48
        tablespoon=units//3
        units%=3 
        return f"{cup} cups, {tablespoon} tablespoons, {units} teaspoons."

    elif unit_measure=="tablespoon":
        cup=units//16
        units%=16
        return f"{cup} cups, {units} tablespoons."

    else:
        return f"{units} cups."


is_valid_input=False
while not(is_valid_input):
    try: 
        input_units=int(input("Enter the number of units: "))
        if input_units>=0:
            is_valid_input=True
        else:
            print("Negative nymber!")
    except ValueError:
        print("The integer you entered is not valid!")

is_valid_input=False
while not(is_valid_input):
    unit_measure=input("Enter the unit of measure (cup/tablespoon/teaspoon): ")
    if unit_measure=="cup" or unit_measure=="tablespoon" or unit_measure=="teaspoon":
        is_valid_input=True
    else:
        print("Invalid input!")

result=reduce_measures(input_units, unit_measure)

print(f"{input_units} {unit_measure} = {result}")