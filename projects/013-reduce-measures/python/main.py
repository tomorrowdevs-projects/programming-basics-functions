
def reduce_measures(units:int, unit_of_measure:str)-> str:
    
    '''Returns, given a quantity in a specific unit of measurement, a string representing the measure using the largest units of measures possible (between cups, tablespoons and teaspoons).
            :parameters:
                    units(int): the number of unit.
                    unit_of_measures(str): the unit of measure(cup, tablespoon or teaspoon)
            :return: 
                    largest_unit_possible(str): a string with the largest unit/s possible.
    ''' 

    largest_units_possible = ''

    # if statement that changes the execution flow according to the unit of measurement
    if unit_of_measure == 'teaspoon':

        # calculate equivalent cups and add an appropriate message to the variable
        cup = units // 48
        if cup <= 1:
                largest_units_possible += f'{cup} cup, '
        else:
            largest_units_possible += f'{cup} cups, '

        # calculate tablespoon
        units = units % 48
        tablespoon = units // 3
        if tablespoon <= 1:
            largest_units_possible += f'{tablespoon} tablespoon, '
        else:
            largest_units_possible += f'{tablespoon} tablespoons, '

        #calculate teaspoon
        units = units % 3
        teaspoon = units
        if units <= 1:
            largest_units_possible += f'{teaspoon} teaspoon'
        else:
            largest_units_possible += f'{teaspoon} teaspoons'

    elif unit_of_measure == 'tablespoon':

        cup = units // 16
        if cup <= 1:
                largest_units_possible += f'{cup} cup,'
        else:
            largest_units_possible += f'{cup} cups, '

        units = units % 16
        tablespoon = units
        if tablespoon <= 1:
            largest_units_possible += f'{tablespoon} tablespoon, 0 teaspoon'
        else:
            largest_units_possible += f'{tablespoon} tablespoons, 0 teaspoon'

    elif unit_of_measure == 'cup':
        cup = units
        if cup <= 1:
                largest_units_possible += f'{cup} cup, 0 tablespoon, 0 teaspoon'
        else:
            largest_units_possible += f'{cup} cups, 0 tablespoon, 0 teaspoon'
    
    return largest_units_possible


def main():
     print(reduce_measures(59,'teaspoon'))
     

if __name__ == '__main__':
     main()