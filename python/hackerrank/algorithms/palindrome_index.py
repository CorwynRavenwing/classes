#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def isPalindrome(s):
    # print("#iP()", s)
    L = len(s)
    for i in range(L // 2):
        # print("#?", i, L-i-1, L)
        c = s[i]
        r = s[L-i-1]
        # print("C/R", c, r)
        if c != r:
            return False
    return True

# STRING s
# return INTEGER
def palindromeIndex(s):
    print("#pI()", s)
    if isPalindrome(s):
        # print("#OK")
        return -1
    L = len(s)
    for i in range(L):
        j = L-i-1
        c = s[i]
        r = s[j]
        print("#ij", i, j, c, r)
        if c != r:
            test = s[i+1:j+1]
            print("#T", test)
            if isPalindrome(test):
                return i
            # else
            test = s[i:j]
            print("#T", test)
            if isPalindrome(test):
                return j
            else:
                return -1
        # check = s[:i] + s[i+1:]
        # # print("#CK", i, check)
        # if isPalindrome(check):
            # return i
    # print("#NO")
    return -1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

