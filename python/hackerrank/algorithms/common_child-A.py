#!/bin/python3

# import math
import os
# import random
# import re
# import sys

# STR s1
# STR s2
# return INT

def purge(L1, L2):
    L1 = [
        e
        for e in L1
        if e in L2
    ]
    L2 = [
        e
        for e in L2
        if e in L1
    ]
    return (L1, L2)

def skipPast(List, Elem):
    if Elem not in List:
        return []
    List = List[:]  # copy List
    # skip everything prior to Elem, plus Elem itself:
    while List.pop(0) != Elem:
        pass
    return List

def join(S):
    return ''.join(S)

def display(S):
    S = join(S)
    M = 5
    leeway = 3
    L = len(S)
    return (
        S[:M]+'...(+'+str(L-M)+')'
        if L > M+leeway
        else S
    )

def commonChild(s1, s2):
    L1 = list(s1)
    L2 = list(s2)
    # print("#L1", display(L1))
    # print("#L2", display(L2))
    (L1, L2) = purge(L1, L2)
    # print("#L1", display(L1))
    # print("#L2", display(L2))
    if L1 == L2:
        return len(L1)
    size_L = min(len(L1), len(L2))
    P = (0, size_L, join(L1), join(L2))
    possibles = [P]
    done = []
    max_A = None
    while len(possibles) > 0:
        # P = possibles.pop()   # last-in first-out
        # P = max(possibles)      # max first
        # possibles = [e for e in possibles if e != P]  # pop that one
        possibles.sort()
        P = possibles.pop()     # get highest
        (S, size_L, L1, L2) = P
        if P in done:
            print("\t\t#DONE ALREADY?!?")
            continue
        done.append(P)
        (T1, T2) = purge(L1, L2)
        print("#Loop",
            [len(possibles), len(done)],
            max_A,
            (S + size_L),
            [S, size_L],
            display(T1), display(T2)
        )

        # test 000: neither S+T1 nor S+T2 are larger than max_A
        if max_A is not None:
            E1 = S + len(T1)
            E2 = S + len(L2)
            E = min(E1, E2)
            if E < max_A:
                print("\t\t#SHORT", max_A, [E1, E2])
                # don't do any tests
                continue

        # test 00: L1 and L2 are the same
        if T1 == T2:
            print("\t\t#EQ", S, len(T1))
            A = S + len(T1)
            max_A = A if max_A is None else max(A, max_A)
            # don't do any tests
            continue

        # needed for all following tests:
        M1 = T1.pop(0)
        M2 = T2.pop(0)
        SP1 = skipPast(T1, M2)   # yes, the 1's and 2's are ...
        SP2 = skipPast(T2, M1)   # ... reversed on the M's here

        # test 0: L1[0] and L2[0] are the same:
        if M1 == M2:
            print("\t\t#NEXT", M1, M2)
            P = (S+1, size_L-1, T1, T2)
            if P not in possibles and P not in done:
                possibles.append(P)
                print("\t\t#P0", M1, [display(T1), display(T2)])
            # else:
                # print("\t\t#dup0")
            # don't do other tests
            continue

        # test 1: accept L1[0]
        (A1, A2) = purge(T1, SP2)

        # test 2: accept L2[0]
        (B1, B2) = purge(SP1, T2)

        # test 3: reject both
        (C1, C2) = purge(T1, T2)

        new_P = [
            (S+1, A1, A2),   # test 1
            (S+1, B1, B2),   # test 2
            (S,   C1, C2),   # test 3
        ]

        for i, P in enumerate(new_P):
            (A, B, C) = P
            size_L = min(len(B), len(C))
            P = (A, size_L, B, C)
            if P not in possibles and P not in done:
                possibles.append(P)
                M = (
                    M1 if i==0
                    else M2 if i==1
                    else ' ' if i==2
                    else '?'
                )
                print("\t\t#P"+str(i+1), [M], size_L)
                # print("\t\t#P"+str(i+1), [M], [display(B), display(C)])

    print("#Poss", possibles)
    print("#A", max_A)
    return max_A

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

