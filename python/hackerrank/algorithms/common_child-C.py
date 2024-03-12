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

def cache_decorate(fn, cache_miss_value = None, debug = False):
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

# need cache_miss_val = False b/c None is a legit answer
CMV = False
DBG = True
scan_to_next_match = cache_decorate(scan_to_next_match, CMV, DBG)
# cache has 3% miss rate: keep this

def get_children(P):
    global S1, S2
    global L1, L2
    (i1, i2) = P
    (j1, j2) = (i1 + 1, i2 + 1)
    if j1 >= L1 or j2 >= L2:
        # string S1 or S2 ran out
        return [None, None]
    skip_letter = (j1, i2)   # keep second character the same
    c1 = S1[j1]
    param = (c1, j2)
    j2 = scan_to_next_match(param)
    accept_letter = (
        (j1, j2)
        if j2 is not None
        else None
    )
    return [skip_letter, accept_letter]

# get_children = cache_decorate(get_children, None, False)
# cache has 50% miss rate (!!!): don't bother
# much faster (9s -> 7s for test tc4) without the cache

score_cache = {}
def get_score(P):
    # one known answer:
    if P is None:
        return -1

    global score_cache
    score = score_cache.get(P, None)

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
    S1 = s1
    S2 = s2
    L1 = len(s1)  # no longer identical
    L2 = len(s2)  # after running purge()

    origin = (-1, -1)
    in_progress = [origin]

    while len(in_progress) > 0:
        P = in_progress[-1]   # don't pop yet
        # print("#IP", [len(in_progress)], P)
        score = get_score(P)
        if score is not None:
            # print("#found score {} for P {}".format(score, P))
            # found score, don't need to work this one
            in_progress.pop()  # ignore retval
            continue
        
        children = get_children(P)
        # print("#\tCH", children)
        scores = [
            get_score(c)
            for c in children
        ]
        scores = [
            (
                s + i
                if s is not None
                else None
            )
            for i, s in enumerate(scores)
        ]
        # print("#\tSC0", scores)
        # ### for some reason this is SLOWER:
        # for index, other_index in [(0, 1), (1, 0)]:
        #     if scores[index] is None:
        #         other_score = scores[other_index]
        #         if other_score is not None:
        #             # one real score and one None
        #             this_child = children[index]
        #             mps = max_possible_score(this_child)
        #             if mps < other_score:
        #                 # print("#MPS < other", mps, other_score)
        #                 scores[index] = -1
        #                 # could set it to mps instead
        #                 # print("#\tSC1", scores)

        # repeat question b/c scores might have changed
        if None not in scores:
            max_score = max(scores)
            # print("#setting score for P to", max_score)
            set_score(P, max_score)
            in_progress.pop()  # ignore retval
            continue

        # print("#in progress append")
        for c in children:
            in_progress.append(c)
        # print("#IP is now:", in_progress)
    
    answer = get_score(origin)
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()

