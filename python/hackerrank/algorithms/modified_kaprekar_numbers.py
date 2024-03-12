#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

def isKaprekarNumber(n):
    # print("#iKN()", type(n), n)
    Sn = str(n)
    # print("#Sn", type(Sn), Sn)
    d = len(Sn)
    # print("#d", type(d), d)
    n2 = n ** 2
    # print("#n2", type(n2), n2)
    Sn2 = str(n2)
    # print("#Sn2", type(Sn2), Sn2)
    pos = len(Sn2) - d
    Sa = Sn2[:pos]
    Sb = Sn2[pos:]
    a = int(Sa) if Sa != '' else 0
    b = int(Sb) if Sb != '' else 0
    checksum = a + b
    # print("#Ck", Sa, Sb, a, b, checksum)
    return (checksum == n)

def kaprekarNumbers(p, q):
    kaprekars = [
        n
        for n in range(p, q+1)
        if isKaprekarNumber(n)
    ]
    if len(kaprekars):
        print(" ".join(map(str, kaprekars)))
    else:
        print("INVALID RANGE")
    return

if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)

