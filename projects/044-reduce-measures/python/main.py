def reduce_measures(number, unit_of_measures):

    if unit_of_measures.lower() == 'teaspoons':
        cup = int(number // 48)
        rest_teaspoon = number % 48
        tablespoons = int(rest_teaspoon // 3)
        teaspoons = rest_teaspoon % 3
    elif unit_of_measures.lower() == 'tablespoons':
        cup = int(number // 16)
        tablespoons = number % 16
        teaspoons = 0
    elif unit_of_measures.lower() == 'cups':
        cup = int(number)
        tablespoons = 0
        teaspoons = 0

    result = []
    if cup > 1:
        result.append(f'{cup} cups')
    elif cup == 1:
        result.append(f'{cup} cup')

    if tablespoons > 1:
        result.append(f'{tablespoons} tablespoons')
    elif tablespoons == 1:
        result.append(f'{tablespoons} tablespoon')

    if teaspoons > 1:
        result.append(f'{teaspoons} teaspoons')
    elif teaspoons == 1:
        result.append(f'{teaspoons} teaspoon')

    return ', '.join(result)