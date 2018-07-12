define starting_mark(height):
  grad = (10.67 - 9.45) / (1.83 - 1.52)
  c = 10.67 - m * 1.83
  return round(height * grad + c, 2)
###


def calculate_age(year_of_birth, current_year):
    out1 = current_year - year_of_birth
    if out1 > 0:
        print "you are %i years old" %out1
    elif out1 == 0:
        print "you are born this year"
    else:
        print "you will be born in %i years" %out1

def calculate_age(year_of_birth, current_year):
    out1 = current_year - year_of_birth
    if out1 > 0:
        print("you are %d years old") % out1
    elif out1 == 0:
        print "you are born this year"
    else:
        print ("you will be born in %d years") % out1

def calculate_age(year_of_birth, current_year):
    out1 = current_year - year_of_birth
    if out1 ==1:
        print "You are 1 year old"
    elif out1 == 0:
        print "You were born this very year!"
    elif out1 == -1:
        print "You will be born in 1 year."
    elif out1 >1:
        print "You are %i years old" %out1
    else:
        print "You will be born in %i years."
