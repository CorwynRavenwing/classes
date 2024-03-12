#!/bin/python3

import os

month_days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def leap_year_julian(year):
    return year % 4 == 0

def leap_year_gregorian(year):
    even_400 = year % 400 == 0
    even_100 = year % 100 == 0
    even_4 = year % 4 == 0
    return even_400 or (even_4 and not even_100)

print("#M", month_days)

def dayOfProgrammer(year):
    if year == 1918:
        # transition year special handling
        leap_year = False
        february_days = (28 - 14 + 1)
    elif 1700 <= year <= 1917:
        # julian calendar
        leap_year = leap_year_julian(year)
        february_days = 29 if leap_year else 28
    elif 1919 <= year <= 2700:
        # gregorian calendar
        leap_year = leap_year_gregorian(year)
        february_days = 29 if leap_year else 28
    else:
        print("#error, invalid year", year)
        return "ERROR"
    print("#LY", leap_year)
    print("#F", february_days)
    month_days_actual = [
        february_days if i == 2 else d
        for i, d in enumerate(month_days)
    ]
    days = 0
    for i, d in enumerate(month_days_actual):
        if (days + d) >= 256:
            break
        else:
            days += d
            toolate = (days >= 256)
            print("#i,d", i, d, days, toolate)
            continue
    day = 256 - days
    dd = str(day).rjust(2, '0')
    mm = str(i).rjust(2, '0')
    print("#I", dd, mm, year, days)
    retval = "{}.{}.{}".format(dd, mm, year)
    return retval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip())
    result = dayOfProgrammer(year)
    fptr.write(result + '\n')
    fptr.close()

