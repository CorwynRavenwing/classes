#!/bin/python3

# import sys

def sum_1_to_n(n):
    # either n or n+1 are even: integer division guaranteed
    return n * (n+1) // 2

def sum_divisible(n, d):
    print("#SAUNDD", n, d)
    m = n - 1
    mod = m % d
    print("#%0", m, mod)
    m2 = m - mod
    mod2 = m2 % d
    assert(mod2 == 0)
    q = m2 // d
    print("#%1", m2, mod2, "Q:", q)

    retval = sum_1_to_n(q) * d

    return retval

def euler_1(n):
    div3 = sum_divisible(n, 3)
    div5 = sum_divisible(n, 5)
    div15 = sum_divisible(n, 15)
    print("#3,5,15:", div3, div5, div15)
    retval = div3 + div5 - div15
    # subtract "15" because these will have been counted twice
    return retval

#     retval = 0
#     for i in range(1, n):
#         if i % 3 == 0 or i % 5 == 0:
#             retval += i
#     return retval

#     match = [
#         i
#         for i in range(1, n)
#         if i % 3 == 0 or i % 5 == 0
#     ]
#     return sum(match)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_1(n))

