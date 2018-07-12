##Lesson 11 Unit 24

def sum_list(x):
    a = 0
    for e in x:
        a = e + a
    return a



def measure_udacity(U):
    count = 0
    for e in U:
        if e[0] == 'U':
            count = count + 1
    return count

def find_second(string,target):
    first = string.find(target)
    second = string.find(target,first+1)
    return second

def find_element(p,t):
    i = o
    while i < len(p):
        if p[i] == t:
            return i
        i = i + 1
    return -1

def find_element(p,t):
    i = 0
    for e in p:
        if e == t:
            return i
        i = i + 1
    return -1

"""Index Operation"""
<list>.index(<value>)
returns error when value is not found

p = [0,1,2]
print p.index(2)
>>> 2
print p.index(3)
>>> 3 is not in the list

<value> in <list>

p = [0,1,2]
print 2 in p
>>> True
print 3 in p
>>> False


Unit 27
"""
Define a procedure, find_element,
using index that takes as its
inputs a list and a value of any
type, and returns the index of
the first element in the input
list that matches the value.
If there is no matching element,
return -1."""

def find_element(l,v):
    i=0
    #for each element in the list, assign the element to the name

    for e in l:
        if e == v:
            return l.index(e)
        i = i + 1
    return -1

def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1

def find_element(p,t):
    if t not in p:
        return -1
    return p.index(t)

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

Unit 29
"""
Define a procedure, union,
that takes as inputs two lists.
It should modify the first input
list to be the set union of the two
lists. You may assume the first list
is a set, that is, it contains no
repeated elements.

a = [1,2,3]
remember that plus does not mutate the list
therefore
a = a + [4,5]
means take list a, cat 4 and 5 to it
and assign the name a to the new list
therefore
len(a) = 5

this is not the same as append!!!!!
a = [1,2,3]
q = [4,5]
a.append(q)
this changes a to
a = [[1,2,3],[4,5]]
len(a) = 2

"""

def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)


a = [1,2,3]
b = [2,4,6]

#union(a,b)
#print a
#>>> [1,2,3,4,6]
#print b
#>>> [2,4,6]


##Lesson11Unit30
"
<list>.pop()
mutates the list by removing and returning its last element
a = [1,2,3]
b = a
x = a.pop()

this means that now
a = [1,2]
and because b refers to a,
b = [1,2]
"


##Lesson11Unit31
