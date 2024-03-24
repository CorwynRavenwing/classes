
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
def fibonacci(X):
    if X <= 2:
        return 1
    return fibonacci(X - 1) + fibonacci(X - 2)

def euler_25(N):
    F = 0
    i = 0
    while len(str(F)) < N:
        i += 1
        F = fibonacci(i)
    F0 = fibonacci(i-1)
    F1 = fibonacci(i)
    L0 = len(str(F0))
    L1 = len(str(F1))
    OK = (L0 < N) and (L1 == N)
    print(f"#check: {N} {i} {L0} {L1} {OK}")
    if not OK:
        assert False
    return i

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_25(N))

