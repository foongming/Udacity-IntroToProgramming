def product_list(list_of_numbers):
    multipler = 1
    while list_of_numbers:
        hold = list_of_numbers.pop()
        multipler = multipler * hold
    return multipler
