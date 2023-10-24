def reduce_measures(num_units, unit):
    unit_values = { 
                    'cup': 48,          #1 cup = 16 tablespoon and 48 teaspoons
                    'tablespoon': 3,    #1 tablespoon = 3 teaspoon
                    'teaspoon': 1
                   }
    
    result = []

    if unit != 'teaspoons':
        if unit in unit_values:
            num_units = num_units * unit_values[unit]
    
    for key in unit_values:
        biggest_unit = num_units // unit_values[key]
        num_units = num_units % unit_values[key]
        result.append(f'{biggest_unit} {key}' if biggest_unit <= 1 else f'{biggest_unit} {key}s')
    return ', '.join(result)

 

def main():
    num_units = int(input('Enter the number of units that you want to use: '))
    unit = input('Enter the type of unit: ')    
    print(reduce_measures(num_units, unit))


if __name__ == '__main__':
    main()