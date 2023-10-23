# defines a function that express an imperial volume using the largest units of measures possible between cups, tablespoons and teaspoons. 
def reduce_measures(units, unit_of_measure):
    result = ''
# conditionals that modify execution of flow in base of unit of measure
    if unit_of_measure == 'cup':
        cup = units
        tablespoon = 0
        teaspoon = 0
# conditional that correct grammar to the answer
        if cup <= 1 :
            result += f'{units} cup, {tablespoon} tablespoon, {teaspoon} teaspoon'
        else: 
            result += f'{units} cups, {tablespoon} tablespoon, {teaspoon} teaspoon'
    elif unit_of_measure == 'tablespoon':
# conditional that permorms computation in base of the number of units and adds step by step a string to result's variable      
        if units > 16:
            cup = units // 16
            tablespoon = units - (cup * 16)
            teaspoon = 0
            if cup <= 1 :
                result += f'{cup} cup,'
            else: 
                result += f'{cup} cups,'
            if tablespoon <= 1:
                result += f' {tablespoon} tablespoon, {teaspoon} teaspoon'
            else:
                result += f' {tablespoon} tablespoons, {teaspoon} teaspoon'
        else:
            cup = 0
            tablespoon = units
            teaspoon = 0
            if tablespoon <= 1:
                result += f'{cup} cup, {tablespoon} tablespoon, {teaspoon} teaspoon'
            else:
                result += f'{cup} cup, {tablespoon} tablespoons, {teaspoon} teaspoon'

    elif unit_of_measure == 'teaspoon':

        if units > 48:
            cup = units // 48
            tablespoon = (units - cup * 48 ) // 3
            teaspoon = (units - cup * 48) - ((units - cup * 48) // 3)
            if cup <= 1 :
                result += f'{cup} cup,'
            else: 
                result += f'{cup} cups,'

            if tablespoon <= 1:
                result += f' {tablespoon} tablespoon,'
            else:
                result += f' {tablespoon} tablespoons,'

            if teaspoon < 1:
                result += f' {teaspoon} teaspoon'
            else: 
                result += f' {teaspoon} teaspoons'

        elif 16 < units < 48:
            cup = 0
            tablespoon = units // 3
            teaspoon = units - tablespoon * 3 
            result += f' {cup} cup,'

            if tablespoon <= 1:
                result += f' {tablespoon} tablespoon,'
            else:
                result += f' {tablespoon} tablespoons,'

            if teaspoon <= 1:
                result += f' {teaspoon} teaspoon'
            else: 
                result += f' {teaspoon} teaspoons'
        else:
            cup = 0
            tablespoon = 0
            teaspoon = units
            if teaspoon <= 1 :
                result += f'{cup} cup, {tablespoon} tablespoon, {units} teaspoon'
            else: 
                result += f'{cup} cups, {tablespoon} tablespoon, {units} teaspoon' 
    return result

