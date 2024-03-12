#!/bin/python3

# import sys

def euler_2(n):
    answer = 0
    (fPrev, f) = (1, 2)
    while f <= n:
        if f % 2 == 0:
            answer += f
            # print("#add f", f, answer)
        fNext = fPrev + f
        (fPrev, f) = (f, fNext)
    return answer

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_2(n))

