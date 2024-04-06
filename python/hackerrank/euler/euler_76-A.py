
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

@with_cache
def sum_count_hard(T):
    (N, maxval) = T
    max_this = N // maxval
    possibles = [
        sum_count(N - (count * maxval), maxval - 1)
        for count in reversed(range(0, max_this + 1))
    ]
    # print(f"# -> {possibles}")
    mod = 10 ** 9 + 7
    return sum(possibles) % mod

def sum_count(N, maxval):
    # print(f"sum_count({N}, {maxval})")
    if N in [0, 1]:
        # print("# -> 1")
        return 1
    if maxval in [0, 1]:
        # print("# -> 1")
        return 1
    if maxval > N:
        maxval = N
    T = (N, maxval)
    return sum_count_hard(T)

def euler_76(N):
    # print(f"#{mod=}")
    return sum_count(N, N-1)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_76(N))

