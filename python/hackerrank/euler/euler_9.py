#!/bin/python3

# import sys

def euler_9(N):
    print("#N", N)
    answers = [-1]
    A_min = 1
    A_max = N // 3 + 1
    for A in range(A_min, A_max+1):
        AA = A * A
        print("#A", A, AA)
        print("#  N//2:", N // 2)
        print("#  N//2 - A:", N // 2 - A)
        print("#  N - A:", N - A)
        if (N - A) == 0:
            print("# for low N, N==A")
            continue
        B = N * (N // 2 - A) // (N - A)
        if B <= A:
            print("#B  ", B, "<A")
            continue
        BB = B * B
        print("#B  ", B, BB)
        C = N - A - B
        CC = C * C
        print("#C    ", C, CC)
        match = AA+BB == CC
        print("#?      ", AA+BB, CC, match)
        if not match:
            print("#X      FAIL")
            continue
        ABC = A * B * C
        print("#+      ", ABC)
        answers.append(ABC)
    return max(answers)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_9(n))

