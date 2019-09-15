# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


"""
this method fails when consecutive items are in the split list

def split_string(source,splitlist):
    # go through source until any of the split list characters
    words = []
    starting_position = 0
    end_position = 0
    word = ""
    for item in source:
    # for each character in a string
    # remember that you can loop through strings as well
        if item in splitlist:
            end_position = source.find(item,starting_position)
            word = source[starting_position:end_position]
            if len(word) > 0:
                words.append(word)
                starting_position = end_position + 1
        else:
                word = word + item
    return words
"""


def split_string(source,splitlist):
    words = []
    splitpoint = True
    # go through source until any of the split list characters
    for item in source:
        if item in splitlist:
            splitpoint = True
        else:
            if splitpoint == True :
                words.append(item)
                splitpoint = False
            else:
                words[-1] = words[-1] + item
    return words



out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
