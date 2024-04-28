#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def tuplify(s):
    return tuple(map(tuple, s))

allowed_range = range(1, 9+1)

def flattenSquare(S):
    return S[0] + S[1] + S[2]

def differenceFromCorrectRange(s):
    single_line = sorted(flattenSquare(s))
    number_dict = {}
    for d in allowed_range:
        number_dict[d] = -1   # expect 1 each
    for d in single_line:
        number_dict[d] += 1   # will already exist
    number_dict = {
        k: v
        for k, v in number_dict.items()
        if v != 0
    }
    number_dict['total'] = sum(single_line) - 3*15
    return number_dict
    
def differenceFromMagicSquare(s):
    row = tuple(
        sum(r) - 15
        for r in s
    )
    # print("#ROW", row)
    s_prime = list(zip(*s))
    # print("#S'", s_prime)
    col = tuple(
        sum(c) - 15
        for c in s_prime
    )
    # print("#COL", col)
    diag = (
        s[0][0] + s[1][1] + s[2][2] - 15,
        s[0][2] + s[1][1] + s[2][0] - 15,
    )
    # print("#DIAG", diag)
    range_diff = tuple(differenceFromCorrectRange(s).values())
    return (row, col, diag, range_diff)

def scoreMagicSquare(s):
    errors = differenceFromMagicSquare(s)
    scores = [
        abs(val)
        for group in errors
        for val in group
    ]
    # print(f"#{list(scores)}")
    return sum(scores)

def mutatedTuple(T, col, delta):
    mT = (
        (val + delta) if col == j else val
        for j, val in enumerate(T)
    )
    mT = (
        new_val if new_val in allowed_range else None
        for new_val in mT
    )
    mT = tuple(mT)
    return (
        mT
        if None not in mT
        else None
    )

def mutatedSquare(S, row, col, delta):
    mS = (
        mutatedTuple(T, col, delta) if row == i else T
        for i, T in enumerate(S)
    )
    mS = tuple(mS)
    return (
        mS
        if None not in mS
        else None
    )

def allNeighborSquares(S):
    neighbors = (
        mutatedSquare(S, row, col, delta)
        for row in range(3)
        for col in range(3)
        for delta in [-1, 1]
    )
    neighbors = (
        new_val
        for new_val in neighbors
        if new_val is not None
    )
    return tuple(neighbors)

def costOfMagicSquareChange(s1, s2):
    L1 = flattenSquare(s1)
    L2 = flattenSquare(s2)

    Z = tuple(zip(L1, L2))
    # print(f"#{Z=}")
    deltas = tuple(
        abs(a - b)
        for (a, b) in Z
    )
    print(f"#{deltas}")
    return sum(deltas)

annealing = 5

def formingMagicSquare(s):
    s = tuplify(s)
    print("#s", s)
    number_dict = differenceFromCorrectRange(s)
    print("#ND", number_dict)
    errors = differenceFromMagicSquare(s)
    print("#MAGIC_DIFF", errors)
    score = scoreMagicSquare(s)
    print("#SCORE", score)
    if score == 0:
        return 0
    cost = 0
    cost_records = {
        s: cost
    }
    best_score = score
    no_worse_than = best_score + annealing
    squares_at_this_cost = [(score, s)]
    while squares_at_this_cost:
        print(f"#SQ={len(squares_at_this_cost)}")
        squares_at_next_cost = []
        for square_record in squares_at_this_cost:
            # print(f"#{cost=} NWT={no_worse_than} {square_record}")
            (old_score, old_s) = square_record
            neighbors = allNeighborSquares(old_s)
            # print(f"### {cost=} NWT={no_worse_than}", end=" ")
            for new_s in neighbors:
                if new_s in cost_records:
                    # print(f"#  {new_s} SEEN BEFORE: {cost_records[new_s]}")
                    continue
                cost_records[new_s] = cost+1
                new_score = scoreMagicSquare(new_s)
                # print(f"#  {new_s} score {new_score}")
                if new_score > no_worse_than:
                    # print(f"[{new_score}]", end=" ")
                    continue
                if new_score < best_score:
                    best_score = new_score
                    no_worse_than = best_score + annealing
                # print(f"{new_score}", end=" ")
                squares_at_next_cost.append((new_score, new_s))
                if new_score == 0:
                    # MAGIC SQUARE!
                    print(f"# MAGIC {new_s} score={new_score}")
                    actual_cost = costOfMagicSquareChange(s, new_s)
                    print(f"# COST {cost+1} {actual_cost}")
                    assert cost+1 == actual_cost
                    return cost+1
            # print("")
        cost += 1
        squares_at_this_cost = squares_at_next_cost
    print("#reached the end of the program.  this shouldn't happen")
    return None

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

