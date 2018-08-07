Udacity Number of Days Problem:


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2 and day1 < day2:
            return True
    return False


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    count = 0
    print count
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        count = count + 1
        return count

#######

Assert daysBetweenDates
Assert < Expression >
If Expression == False, assertion will stop with "Assertion Failure"


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3),
                  ((2013, 1, 1, 1999, 12, 31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)
test()


########### Final Step #######
def dateIsBefore(y1, m1, d1, y2, m2, d2):
    if y1 < y2:
        return True
    if y1 == y2:
        if m1 < m2:
            return True
        if m1 == m2:
            if d1 < d2:
                return True
    return False

dateIsBefore(2016,1,1,2017,1,1)
dateIsBefore(2016,1,1,2016,2,1)
dateIsBefore(2016,1,1,2016,1,2)
dateIsBefore(2016,1,1,2016,1,1)

def is_leap_year(x):
    if x % 4 == 0 and x % 100 != 0:
        return True
    if x % 400 == 0:
        return True
    return False

def nextDay(year, month, day):
    if month == 2:
        if is_leap_year(year) == True:
            if day < 29:
                return year, month, day + 1
            else:
                #               if day == 29:
                return year, month + 1, 1
        if is_leap_year(year) == False:
            if day < 28:
                return year, month, day + 1
            else:
                #               if day == 28:
                return year, month + 1, 1
    # 30daymonths = [4,6,9,11]
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day < 30:
            return year, month, day + 1
        else:
            return year, month + 1, 1
    # 31daymonths = [1,3,5,7,8,10,12]
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day < 31:
            return year, month, day + 1
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
