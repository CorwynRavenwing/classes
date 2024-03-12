#!/bin/python3

# import math
import os
# import random
# import re
# import sys
from collections import Counter

# global variable
S = ''

# STR s
def initialize(s):
    # This function is called once before all queries.
    global S
    S = s
    return

def factorial_mod_divided(N, mod, X, other_div_factors):
    # print("#F_M_D()", N, mod, X, other_div_factors)
    # defined as (N! / X! / other_div_factors) % mod
    answer = 1
    # print("#A 23", answer)
    for fi, fact in enumerate(other_div_factors):
        if fact is None:
            continue
        if (answer % fact == 0):
            answer //= fact
            other_div_factors[fi] = None
            # print("#A 27", answer)
    answer %= mod
    # print("#A 29", answer)
    for i in range(X+1, N+1):   # X+1 .. N  === N! / X!
        # print("#I", i)
        answer *= i
        # print("#A 32", answer)
        for fi, fact in enumerate(other_div_factors):
            if fact is None:
                continue
            if (answer % fact == 0):
                answer //= fact
                other_div_factors[fi] = None
                # print("#A 36", answer)
        if (other_div_factors == []):
            answer %= mod
        # print("#A 38", answer)
        for fi, fact in enumerate(other_div_factors):
            if fact is None:
                continue
            if (answer % fact == 0):
                answer //= fact
                other_div_factors[fi] = None
        # print("#A 42", answer, other_div_factors)
        other_div_factors = [
            f
            for f in other_div_factors
            if f is not None
        ]
    if (other_div_factors != []):
        # print("#ERROR: duplicates left over", other_div_factors)
        for fi, fact in enumerate(other_div_factors):
            if fact is None:
                continue
            answer /= fact
            other_div_factors[fi] = None
        # print("#A 46", answer)
    answer %= mod
    # print("#A 47", answer)
    return answer

# INT L
# INT R
# return INT
def answerQuery(L, R):
    # shortcut 1: a "maximum-length palindrome" is composed of
    # *all available pairs* of characters,
    # plus *any one* single character if one exists.
    
    # shortcut 2: the "count of M.L.P." ===
    # "permutations of one half of each pair" [aabbccccdddddd -> perm(abccddd)]
    # times "count of non-paired letters"
    # [all non-paired letters are different, or else they would be paired]
    
    # shortcut 3: "permutations of group ignoring duplicates"
    # === "perm(group) / perm(duplicates)"
    # [perm(abccddd) = perm(7) / perm(2)perm(3)]
    
    # shortcut 4: "permutations(N)" === N factorial
    
    # shortcut 5: "(A * B) mod C" === "((A mod C) * (B mod C)) mod C"
    # which will make huge factorials much easier
    
    mod = 1000000007
    SS = S[L-1:R]   # 1-indexed and inclusive
    # print("#SS", SS)
    chars = Counter(SS)
    singles = []
    pairs = Counter()
    for c, count in chars.items():
        if count % 2 == 1:
            singles.append(c)
            count -= 1
        if count > 0:
            pairs[c] = count // 2
    # print("#Singles", singles)
    # print("#Pairs", pairs)
    pairs_count = sum([
        count
        for count in pairs.values()
    ])
    # print("#Pairs Count", pairs_count)
    if pairs_count > 0:
        max_dups = max(pairs.values())
        # print("#Max Dups", max_dups)
        max_dup_element = [
            e
            for e, count in pairs.items()
            if count == max_dups
        ]
        # print("#Max Dup Element", max_dup_element)
        if max_dup_element != []:
            first_matching_dup = max_dup_element[0]
            # print("#First Matching Dup", first_matching_dup)
            other_div_factors = []
            # print("### PI", pairs.items())
            for e, count in pairs.items():
                # print("###   C", count)
                for fact in range(2, count+1):
                    # print("###      F", fact)
                    if e != first_matching_dup:
                        # print("###        E diff", e)
                        if fact > 1:
                            # print("###           F>1", fact)
                            other_div_factors.append(fact)
            #other_div_factors = [
            #    fact
            #    for e, count in pairs.items()
            #    for fact in range(2, count)
            #    if e != first_matching_dup
            #    if fact > 1
            #]
        else:
            other_div_factors = []
        # print("#Other Div Factors", other_div_factors)
        permute_pairs = factorial_mod_divided(
            pairs_count,
            mod,
            max_dups,
            other_div_factors
        )
        if permute_pairs == 0:
            print("non-zero pairs found zero permutations")
            permute_pairs = 1
    else:
        permute_pairs = 1
    singles_count = len(singles)
    if singles_count == 0:
        singles_count = 1
    answer = singles_count * permute_pairs
    answer %= mod
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    initialize(s)
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        L = int(first_multiple_input[0])
        R = int(first_multiple_input[1])
        result = answerQuery(L, R)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()

