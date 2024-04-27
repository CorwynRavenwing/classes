#!/bin/python3

# import math
import os
# import random
# import re
# import sys

cached_values = {}

def cache_set(query, answer):
    global cached_values
    cached_values[query] = answer
    print(f"#  cache set '{query}' -> '{answer}'")
    pass

def cache_get(query, default = None):
    global cached_values
    answer = cached_values.get(query, default)
    return answer

def with_cache(fn):
    def inner(query):
        answer = cache_get(query)
        if answer is None:
            print(f"#  cache miss '{query}'")
            answer = fn(query)
            cache_set(query, answer)
        else:
            print(f"#  cache hit '{query}' -> '{answer}'")
        return answer
    return inner

mod = 10 ** 9 + 7

def factorial(N):
    if not N:
        return 1
    retval = N
    for i in range(1, N):
        retval *= i
        # print("#I", i, retval)
    return retval

# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY x as parameter.
def solve(x):
    N = len(x)
    print(f"#{N=} {x=}")
    allowed_values = tuple([
        val + 1
        for val in range(N)
        if (val + 1) not in x
    ])
    print(f"#{allowed_values=}")
    attempt = tuple(
        allowed_values if val == 0 else (val,)
        for val in x
    )
    print(f"#{attempt=}")
    possibilities = [attempt]
    print(f"#{possibilities=}")

    line_numbers = 0
    while possibilities:
        print(f"#{len(possibilities)=}")
        attempt = possibilities.pop()
        print(f"#  {attempt=}")
        answer = cache_get(attempt, None)
        if answer is not None:
            line_numbers += answer
            line_numbers %= mod
            continue
        if not attempt:
            print("#    EMPTY")
            cache_set(attempt, 0)
            continue
        n = len(attempt)
        first = attempt[0]
        rest = attempt[1:]
        if len(first) == 1:
            x0 = first[0]
            line = (x0 - 1) * factorial(n - 1)
            line %= mod
            if N == n:
                line += 1
            line_numbers += line
            line_numbers %= mod
            print(f"#    {N=} {n=} ({x0}-1)*({n}-1)! = {line} {line_numbers=}")
            new_attempt = tuple(
                tuple(
                    (
                        Xn - 1
                        if Xn > x0
                        else Xn
                    )
                    for Xn in group
                    if Xn != x0
                )
                for group in rest
            )
            print(f"#    -> {new_attempt}")
            new_answer = cache_get(new_attempt)
            if new_answer is None:
                possibilities.append(new_attempt)
            else:
                cache_set(attempt, line + new_answer)
            continue
        new_possibilities = []
        new_total = 0
        for x0 in first:
            new_attempt = ((x0,),) + tuple(
                tuple(
                    Xn
                    for Xn in group
                    if Xn != x0
                )
                for group in rest
            )
            print(f"#    -> {new_attempt}")
            new_answer = cache_get(new_attempt)
            new_total = (
                new_total + new_answer
                if None not in [new_total, new_answer]
                else None
            )
            new_possibilities.append(new_attempt)
        if new_total is None:
            possibilities.extend(new_possibilities)
        else:
            cache_set(attempt, line + new_total)
    print(f"#{possibilities=}")
    print("#  -> should be empty")
    return line_numbers % mod

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = solve(a)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

