# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

danton = "De l'audace, encore de l'audace, toujours de l'audace"
def find_second(string,target):
    first = string.find(target)
    second = string.find(target,first+1)
    return second


#def find_second(string,target):
#    return string.find(target)[secondary:]

print find_second(danton, 'audace')

#print find_second(danton, 'audace')
#>>> 25

#twister = "she sells seashells by the seashore"
#print find_second(twister,'she')
#>>> 13

if <test expression>:
  <block>

i = 32

def absolute(x):
  if x< 0:
    x = -x
  return x


def
