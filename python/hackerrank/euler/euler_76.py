
def with_cache(fn):
    cache_data = {}

    def inner(x):
        if x in cache_data:
            R = cache_data[x]
            # print("#cache hit", x, R)
        else:
            R = fn(x)
            cache_data[x] = R
            # print("#cache miss", x, R)
        return R
    return inner

def sum_count_easy(T):
    (N, maxval) = T
    if N in [0, 1]:
        # print("# -> 1")
        return 1
    if maxval in [0, 1]:
        # print("# -> 1")
        return 1
    return None

@with_cache
def sum_count_hard(T):
    problem_set = [T]
    mod = 10 ** 9 + 7
    retval = 0
    while problem_set:
        ones = [
            (a, b)
            for (a, b) in problem_set
            if a in [0, 1] or b in [0, 1]
        ]
        if ones:
            retval += len(ones)
            retval %= mod
            problem_set = [
                T
                for T in problem_set
                if T not in ones
            ]
            print(f"# {len(problem_set)} <- {ones}")
        if not problem_set:
            continue
        T = problem_set.pop()
        (N, maxval) = T
        # ans = sum_count_easy(T)
        # if ans is not None:
        #     retval += ans
        #     retval %= mod
        #     continue
        max_this = N // maxval
        possibles = [
            (N - (count * maxval), maxval - 1)
            for count in range(0, max_this + 1)
        ]
        problem_set.extend(possibles)
        print(f"# {len(problem_set)} -> {possibles}")
    return retval

def sum_count(N, maxval):
    # print(f"sum_count({N}, {maxval})")
    if maxval > N:
        maxval = N
    T = (N, maxval)
    ans = sum_count_easy(T)
    if ans is not None:
        return ans
    return sum_count_hard(T)

def euler_76(N):
    # print(f"#{mod=}")
    return sum_count(N, N-1)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_76(N))

