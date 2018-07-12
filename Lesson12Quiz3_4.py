#quiz3

def product_list(list_of_numbers):
    multipler = 1
    while list_of_numbers:
        hold = list_of_numbers.pop()
        multipler = multipler * hold
    return multipler

#quiz4
def greatest(list_of_numbers):
    greatest = 0
    while list_of_numbers:
        hold = list_of_numbers.pop()
        if hold > greatest:
            greatest = hold
    return greatest
