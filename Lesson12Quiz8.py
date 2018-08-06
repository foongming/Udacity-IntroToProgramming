# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

##strategy one

def check_sudoku(x):
    n = len(x)
    #checking the elements in each row
    present_elements_in_row = []
    present_elements_in_column = []
    for e in x:
        while len(present_elements_in_row) < n:
            hold = e.pop()
            #check if integer
            if hold % 1 != 0:
                return False
            #check if within range
            if hold > n:
                return False
            #check for duplicate in row
            if hold in present_elements_in_row:
                return False
            #get element last of column
            hold_column = x[hold][hold]
            #check for duplicate in column
            if hold_column in present_elements_in_column:
                return False
            present_elements_in_row.append(hold)
            present_elements_in_column.append(hold_column)
        print present_elements_in_row
        print present_elements_in_column
        return True

"""stuck with the queing of the looping. if the number in top right is != len,
then the column looping does not work"""

##strategy two
"""initiate check in a (1,1) (2,2) etc pattern. diagonal down"""
def check_sudoku(x):
    n = len(x)
    i = 0
    while i < n:
        # checking x and y positions down the grid
        present_elements_in_row = []
        present_elements_in_column = []
        increment = 0
        position_column = x[i][increment]
        print position_column
        position_row = x[increment][i]
        print position_row
        # check if integer
        if position_column % 1 != 0 or position_row % 1 != 0:
            return False
        """type error because a string was input instead of a number"""
        # check if within range
        if position_column > n or position_row > n:
            return False
        # check for duplicate in column
        if position_column in present_elements_in_column:
            return False
        # check for duplicate in row
        if position_row in present_elements_in_row:
            return False
        i = i + 1
        increment = increment + 1
        present_elements_in_row.append(position_row)
        present_elements_in_column.append(position_column)
        return True

"""instead of checking if integers. allow only integers"""

##strategy three. after checking the solution for a hint
def check_sudoku(x):
    n = len(x)
    i = 0
    while i < n:
        # checking x and y positions down the grid
        present_elements_in_row = []
        present_elements_in_column = []
        second_coordinate = 0
        position_column = x[i][second_coordinate]
        position_row = x[second_coordinate][i]
        print position_column, position_row
        # check if digit here
        # check if within range
        if position_column > n or position_row > n:
            return False
        # check for duplicate in column
        if position_column in present_elements_in_column:
            return False
        # check for duplicate in row
        if position_row in present_elements_in_row:
            return False
        i = i + 1
        increment = increment + 1
        present_elements_in_row.append(position_row)
        present_elements_in_column.append(position_column)
        return True




#print check_sudoku(incorrect)
#>>> False

#print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False
