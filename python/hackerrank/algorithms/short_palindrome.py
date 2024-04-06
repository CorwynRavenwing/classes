#!/bin/python3

# import math
import os
# import random
# import re
# import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    # answers = []
    retval = 0
    for A in range(len(s)):
        Sa = s[A]
        print(f"#{A=} {Sa}")
        for B in range(A+1, len(s)):
            Sb = s[B]
            print(f"#  {B=} {Sb}")
            minC = B+1
            while minC:
                C = s.find(Sb, minC)
                if C == -1:
                    print(f"#    {C=} NO")
                    minC = 0
                    continue
                Sc = s[C]
                print(f"#    {C=} {Sc}")
                minD = C+1
                while minD:
                    D = s.find(Sa, minD)
                    if D == -1:
                        print(f"#      {D=} NO")
                        minD = 0
                        continue
                    Sd = s[D]
                    print(f"#      {D=} {Sd}")
                    # answers.append(
                    #     ((A, B, C, D), (Sa, Sb, Sc, Sd))
                    # )
                    retval += 1
                    minD = D + 1
                minC = C + 1
    # print(f"#{answers=}")
    # return len(answers)
    return retval

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = shortPalindrome(s)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

