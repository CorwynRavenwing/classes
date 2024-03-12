#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def numberInWords(i):
    match i:
        case 1: return "one"
        case 2: return "two"
        case 3: return "three"
        case 4: return "four"
        case 5: return "five"
        case 6: return "six"
        case 7: return "seven"
        case 8: return "eight"
        case 9: return "nine"
        case 10: return "ten"

        case 11: return "eleven"
        case 12: return "twelve"
        case 13: return "thirteen"
        case 14: return "fourteen"
        case 15: return "fifteen"
        case 16: return "sixteen"
        case 17: return "seventeen"
        case 18: return "eighteen"
        case 19: return "nineteen"
        
        case 20: return "twenty"
        
        # legal input range is [1 .. 29]
        case _:
            return ' '.join([
                numberInWords(20),    # "twenty"
                numberInWords(i-20),  # "three"
            ])
    return "unknown"

def timeInWords(h, m):
    nexthour = h+1
    if nexthour == 13:
        nexthour = 1
    if m == 0:
        return numberInWords(h)+" o' clock"
    if m == 1:
        return "one minute past "+numberInWords(h)
    if m == 15:
        return "quarter past "+numberInWords(h)
    if m == 30:
        return "half past "+numberInWords(h)
    if m == 45:
        return "quarter to "+numberInWords(nexthour)
    # if m == 59:
    #     return "one minute of "+numberInWords(nexthour)
    if m < 30:
        return numberInWords(m)+" minutes past "+numberInWords(h)
    else:
        return numberInWords(60-m)+" minutes to "+numberInWords(nexthour)
    return "unreachable"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    fptr.write(result + '\n')
    fptr.close()

