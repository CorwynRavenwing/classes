#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

mod = 10 ** 9 + 7

def factorial_divide(N, M1, M2):
    # print(f"# factorial_divide({N}, {M1}, {M2})")
    retval = 1
    Min, Max = min(M1, M2), max(M1, M2)
    for i in range(Max+1, N+1):
        retval *= i
        print("#I*", i, retval)
    for i in range(1, Min+1):
        assert retval % i == 0
        retval //= i
        print("#I/", i, retval)
    # print(f"#  -> {retval}")
    return retval % mod

def factorial(N):
    if not N:
        return 1
    retval = N
    for i in range(1, N):
        retval *= i
        # print("#I", i, retval)
    return retval

def n_pick_k(N, K):
    # N pick K === (N!) / (K!)(N-K)!
    if N < K:
        return 0
    answer = factorial_divide(N, K, N-K)
    return answer

# STR s
# return INT
def shortPalindrome(s):
    # answers = []
    retval = 0
    S_counts = Counter(s)
    for letter, count in S_counts.items():
        # print(f"#Total of {count} letter '{letter}'")
        D_count = n_pick_k(count, 4)
        retval += D_count
        # print(f"#  ({D_count=}) {letter} {retval=}")
    if len(S_counts) > 1:
        for A in range(len(s)):
            Sa = s[A]
            # print(f"#{A=} {Sa}")
            for B in range(A+1, len(s)):
                Sb = s[B]
                if Sb == Sa:
                    continue
                # print(f"#{A=} {Sa} {B=} {Sb}")
                minC = B+1
                while minC:
                    C = s.find(Sb, minC)
                    if C == -1:
                        # print(f"#{A=} {Sa} {B=} {Sb} {C=} NO")
                        minC = 0
                        continue
                    Sc = s[C]
                    # print(f"#{A=} {Sa} {B=} {Sb} {C=} {Sc}")
                    minD = C+1
                    D_section = s[minD:]
                    D_section_counts = Counter(D_section)
                    D_count = D_section_counts[Sa]
                    Sd = Sa
                    retval += D_count
                    # print(f"#{A=} {Sa} {B=} {Sb} {C=} {Sc} ({D_count=}) {Sd} {retval=}")
                    minC = C + 1
    # print(f"#{answers=}")
    # return len(answers)
    return retval % mod

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = shortPalindrome(s)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

