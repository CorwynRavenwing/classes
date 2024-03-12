from collections import deque

def can_stack(cubes):
    while len(cubes) > 0:
        # print("C", tuple(cubes))
        # if len(cubes) % 1000 == 0:
            # print("L(C)", len(cubes))
        first = cubes[0]
        last = cubes[-1]
        big = max(cubes)
        # print("?", first, last, big)
        if big == first:
            # print("FIRST", first)
            ignore = dq.popleft()
            continue
        elif big == last:
            # print("LAST", last)
            ignore = dq.pop()
            continue
        else:
            # print("NO")
            return False
    # print("ZERO")
    return True
    
T = int(input())
# print("T", T)
for t in range(T):
    N = int(input())
    # print("N", N)
    dq = deque(map(int, input().split()))
    # print("dq", dq)
    if can_stack(dq):
        print("Yes")
    else:
        print("No")
# print("done")

