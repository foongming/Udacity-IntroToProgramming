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

#quiz 5
"""
Define a procedure, total_enrollment,
that takes as an input a list of elements,
where each element is a list containing
three elements: a university name,
the total number of students enrolled,
and the annual tuition fees.
The procedure should return two numbers,
not a string,
giving the total number of students
enrolled at all of the universities
in the list, and the total tuition fees
(which is the sum of the number
of students enrolled times the
tuition fees for each university).
"""

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(x):
    enrollment = 0
    money = 0
    for e in x:
        enrollment = enrollment + e[1]
        money = money + e[1]*e[2]
        return enrollment, money

#print total_enrollment(udacious_univs)
#>>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside
# interpreter you might not see it.

#print total_enrollment(usa_univs)
#>>> (77285,3058581079)
