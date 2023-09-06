def calculate_distance(kilometers_travelled):
    service_price = 4

    conversion_metres = kilometers_travelled * 1000
    service_price += (conversion_metres / 140) * 0.25

    return print("{:.2f}".format(service_price))



