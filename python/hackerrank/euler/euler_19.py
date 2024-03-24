
# we're numbering days of the week Sun (0) .. Sat (6)

# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
def isLeapYear(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False

def daysInMonth(y, m):
    # Thirty days has September,
    # April, June and November.
    if m in [9, 4, 6, 11]:
        return 30
    # Saving February alone,
    # Which has twenty-eight, rain or shine.
    # And on leap years, twenty-nine.
    if m in [2]:
        if isLeapYear(y):
            return 29
        else:
            return 28
    # All the rest have thirty-one,
    return 31

# 1 Jan 1900 was a Monday.
DOW = {
    (1900, 1): 1
}
DOW_year_upto = 1900

def dayOfWeek(dateTuple):
    print("#DOW()", dateTuple)
    (yyyy, mm) = dateTuple
    global DOW, DOW_year_upto
    while DOW_year_upto < yyyy:
        yearTuple = (DOW_year_upto, 1)
        nextYearTuple = (DOW_year_upto + 1, 1)
        oldVal = DOW[yearTuple]   # not found -> error
        leapYear = isLeapYear(DOW_year_upto)
        yearDays = 365 + (1 if leapYear else 0)
        newVal = oldVal + yearDays
        newVal %= 7
        DOW[nextYearTuple] = newVal
        DOW_year_upto += 1
        print("#DOW year", yearTuple, oldVal, nextYearTuple, newVal)
    # look up question in cache
    cache = DOW.get((yyyy, mm), None)
    if cache is None:
        for month in range(1, 12):
            monthTuple = (yyyy, month)
            nextMonthTuple = (yyyy, month + 1)
            oldVal = DOW[monthTuple]   # not found -> error
            days = daysInMonth(yyyy, month)
            newVal = oldVal + days
            newVal %= 7
            DOW[nextMonthTuple] = newVal
            print("#DOW month", monthTuple, oldVal, nextMonthTuple, newVal)
    value = DOW[(yyyy, mm)]   # not found -> error
    print("#DOW ->", value)
    return value

def datesBetween(dateTuple1, dateTuple2):
    print("#DB()", dateTuple1, dateTuple2)
    BEGIN_YEAR = 1
    END_YEAR = 12+1
    (y1, m1) = dateTuple1
    (y2, m2) = dateTuple2
    retval = []
    if y1 > y2:
        raise ValueError(f"year1 ({y1}) > year2 ({y2})")
    elif y1 == y2:
        # just this piece of current year
        # inclusive of m2
        retval.extend([
            (y2, mm)
            for mm in range(m1, m2 + 1)
        ])
    elif y1 < y2:
        # add rest of year y1 starting at m1:
        retval.extend([
            (y1, mm)
            for mm in range(m1, END_YEAR)
        ])
        # add entire years from y1 to y2 NON-inclusive:
        retval.extend([
            (yyyy, mm)
            for yyyy in range(y1 + 1, y2)
            for mm in range(BEGIN_YEAR, END_YEAR)
        ])
        # add first part of y2
        # inclusive of m2
        retval.extend([
            (y2, mm)
            for mm in range(BEGIN_YEAR, m2 + 1)
        ])
    else:
        msg = f"y1 ({y1}) <=> y2 ({y2}) returns neither <, >, or =="
        raise ValueError(msg)
    return retval

# How many Sundays fell on the first of the month between two dates(both inclusive)?
def euler_19(date1, date2):
    (y1, m1, d1) = date1
    if d1 != 1:
        print("#date1 not on first of month!", date1)
        # move forward
        m1 += 1
        d1 = 1
        if m1 > 12:
            print("#... rolling over to next year", (y1, m1))
            m1 -= 12
            y1 += 1
        print("#new date:", (y1, m1, d1))
    (y2, m2, d2) = date2
    if d2 != 1:
        print("#date2 not on first of month!", date2)
        # move backward
        d2 = 1
        print("#new date:", (y2, m2, d2))
    print("#checking dates:", (y1, m1, d1), (y2, m2, d2))
    datesList = datesBetween(
        (y1, m1),
        (y2, m2),
    )
    # print("#dates:", datesList)
    days = [
        dayOfWeek(D)
        for D in datesList
    ]
    print("#days of week", days)
    sundays = [
        d
        for d in days
        if d == 0
    ]
    print("#sundays", sundays)
    return len(sundays)

T = int(input().strip())
for _ in range(T):
    (DateTuple1) = tuple(map(int, input().strip().split(' ')))
    (DateTuple2) = tuple(map(int, input().strip().split(' ')))
    print(euler_19(DateTuple1, DateTuple2))

