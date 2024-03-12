#!/bin/python3

# import math
import os
# import random
# import re
# import sys

def purge(s1, s2):
    s1 = ''.join([
        e
        for e in s1
        if e in s2
    ])
    s2 = ''.join([
        e
        for e in s2
        if e in s1
    ])
    return (s1, s2)

def with_cache(fn, debug = False):
    cache_miss_value = 'cache miss'
    cache_data = {}
    attempts = 0
    cache_misses = 0
    
    def inner(x):
        nonlocal attempts, cache_misses
        attempts +=1
        retval = cache_data.get(x, cache_miss_value)
        if retval is cache_miss_value:
            cache_misses += 1
            retval = fn(x)
            if debug:
                miss_fraction = cache_misses / attempts
                miss_percent = round(100 * miss_fraction, 2)
                print(
                    "#cache miss {} -> {}"
                    .format(x, retval)
                )
                if cache_misses % 1000 == 0:
                    print(
                        "#    miss {}% ({}/{})"
                        .format(
                            miss_percent,
                            cache_misses,
                            attempts
                        )
                    )
            cache_data[x] = retval
        return retval
     
    return inner

# global variables
S1 = None
S2 = None
L1 = None
L2 = None
accept_first = False
cache_scores = True

def scan_to_next_match(location):
    (c1, i2) = location
    global S2
    try:
        i2 = S2.index(c1, i2)
        c2 = S2[i2]
        assert(c1 == c2)
    except ValueError:
        return None
    return i2

scan_to_next_match = with_cache(scan_to_next_match, False)
# cache has 3% miss rate: keep this

def get_children(P):
    global S1, S2
    global L1, L2
    global accept_first
    (i1, i2) = P
    (j1, j2) = (i1 + 1, i2 + 1)
    if j1 >= L1 or j2 >= L2:
        # string S1 or S2 ran out
        return [None, None]
    skip = (j1, i2)   # keep second character the same
    c1 = S1[j1]
    param = (c1, j2)
    j2 = scan_to_next_match(param)
    accept = (
        (j1, j2)
        if j2 is not None
        else None
    )
    return [accept, skip] if accept_first else [skip, accept]

# get_children = with_cache(get_children, False)
# cache has 50% miss rate (!!!): don't bother doing it
# much faster (9s -> 7s for test 4) without the cache

def get_score_uncached(P):
    # one known answer:
    if P is None:
        return -1
    return None

score_cache = {}
score_cache_attempt = 0
score_cache_miss = 0
def get_score(P):
    # one known answer:
    if P is None:
        return -1

    global score_cache, score_cache_attempt, score_cache_miss
    score = score_cache.get(P, None)

    score_cache_attempt += 1
    if score is None:
        score_cache_miss += 1
        if score_cache_miss % 1000 == 0:
            miss_fraction = score_cache_miss / score_cache_attempt
            miss_percent = round(100 * miss_fraction, 2)
            print(
                "#SCORE cache *MISS*",
                "{}%".format(miss_percent),
                P,
                score,
            )
    # else:
    #     print("#SCORE cache  HIT  ", P, score)

    # don't prime the cache, just return it 
    return score

def set_score(P, score):
    global score_cache
    score_cache[P] = score
    # prime the cache, return passed-in score
    return score

def max_possible_score(P):
    global L1, L2
    (i1, i2) = P
    remain_1 = max(0, L1 - i1)
    remain_2 = max(0, L2 - i2)
    score = min(remain_1, remain_2)
    # print("#    MAX", score, (remain_1, remain_2))
    return score

# STR s1
# STR s2
# return INT
def commonChild(s1, s2):
    (s1, s2) = purge(s1, s2)
    global S1, S2
    global L1, L2
    global accept_first
    S1 = s1
    S2 = s2
    L1 = len(s1)  # no longer identical
    L2 = len(s2)  # after running purge()

    origin = (-1, -1)
    in_progress = [origin]
    inprog_scores = [[]]
    p_values_checked = 0

    while len(in_progress) > 0:
        assert(len(inprog_scores) > 0)
        p_values_checked += 1
        P = in_progress[-1]   # don't pop yet
        S = inprog_scores[-1]

        # # shouldn't need this check:
        # if P is None:
        #     max_score = -1
        #     # act like section 2

        children = get_children(P)
        SS = [
            S[0] if len(S) > 0 else '',
            S[1] if len(S) > 1 else '',
        ]
        max_possible = max_possible_score(P)
        if p_values_checked % 1 == 0:
            print("#IP {} {} ({},{}) {} [{},{}] {} {}".format(
                str(p_values_checked).rjust(6),
                str(len(in_progress)).rjust(4),
                str(P[0]).rjust(4),
                str(P[1]).rjust(4),
                str(max_possible).rjust(4),
                str(SS[0]).rjust(3),
                str(SS[1]).rjust(3),
                str(children[0]).center(12),
                str(children[1]).center(12),
            ))

        if children == [None, None]:
            # -> scores(children) == [-1, -1]
            # -> max([-1, -1+1]) == 0
            max_score = 0
            in_progress.pop()    # ignore retval
            inprog_scores.pop()  # ignore retval
            if len(inprog_scores) > 0:
                print("#MAX-", max_score)
                if cache_scores:
                    set_score(P, max_score)
                inprog_scores[-1].append(max_score)
                continue
            else:
                print("#RET-", max_score)
                print("# *** checked total", p_values_checked)
                return max_score

        # recalculate len(S) each time because it may change
        if (len(S) == 0):
            print("#   S", S, "len", len(S), "0")
            if cache_scores:
                print("#      BRANCH A cache_scores")
                max_score = get_score(P)
            else:
                max_score = None
            if max_score is not None:
                print("#      BRANCH A1 found cached score")
                max_score = get_score(P)
                in_progress.pop()    # ignore retval
                inprog_scores.pop()  # ignore retval
                if len(inprog_scores) > 0:
                    print("#MAX0", max_score)
                    inprog_scores[-1].append(max_score)
                    S = inprog_scores[-1]
                    # fall through
                    continue
                    # CAUSES THE PROBLEM
                else:
                    print("#RET0", max_score)
                    print("# *** checked total", p_values_checked)
                    return max_score
            elif children[0] is None:
                print("#      BRANCH B children.0 None")
                print("#    child[0] is None")
                max_score = -1
                inprog_scores[-1].append(max_score)
                S = inprog_scores[-1]
                # fall through
                # continue
                # THIS ONE IS OKAY
            else:
                print("#      BRANCH C else")
                print("#    child[0] append")
                in_progress.append(children[0])
                inprog_scores.append([])
                continue

        # recalculate len(S) each time because it may change
        if (len(S) == 1):
            print("#   S", S, "len", len(S), "1")
            if children[1] is None:
                print("#    child[1] is None")
                max_score = -1
                inprog_scores[-1].append(max_score)
                S = inprog_scores[-1]
                # fall through
                # continue
                # THIS ONE IS OKAY TOO
            # elif S[0] > max_possible:
            #     print("#    *** MPS < other", max_possible, S[0])
            #     max_score = -1
            #     inprog_scores[-1].append(max_score)
            #     S = inprog_scores[-1]
            #     # fall through
            #     continue
            else:
                print("#    child[1] append")
                in_progress.append(children[1])
                inprog_scores.append([])
                continue

        # recalculate len(S) each time because it may change
        if (len(S) == 2):
            print("#   S", S, "len", len(S), "2")
            adds = [1, 0] if accept_first else [0, 1]
            max_score = max([
                S[0] + adds[0],
                S[1] + adds[1],
            ])
            in_progress.pop()    # ignore retval
            inprog_scores.pop()  # ignore retval
            if len(inprog_scores) > 0:
                print("#MAX1", max_score)
                if cache_scores:
                    set_score(P, max_score)
                inprog_scores[-1].append(max_score)
                continue
            else:
                print("#RET1", max_score)
                print("# *** checked total", p_values_checked)
                return max_score

    assert("Prior loop returns" == "but never terminates")
    return None

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

