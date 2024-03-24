
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

def divisors_of(X):
    # print(f"#divisors_of({X})")
    retval = set()
    for i in range(1, X+1):
        if i * i > X:
            break
        if X % i == 0:
            j = X // i
            # print(f"#  found divisors {i}, {j}")
            retval.add(i)
            retval.add(j)
    return tuple(retval)

def proper_divisors_of(X):
    d = divisors_of(X)
    # print("#d", d)
    pd = list(d)
    # print("#pd", pd)
    if X in d:
        pd.remove(X)
        # print("#pd", pd)
    # else:
    #     print("### X not in its own divisors", X, d)
    return tuple(pd)

@with_cache
def abundant(X):
    S = sum(proper_divisors_of(X))
    return S > X

def euler_23(N):
    for X in range(1, N//2 + 2):
        if not abundant(X):
            # print("#X", X)
            continue
        Y = N - X
        if abundant(Y):
            # print("#X", X, Y)
            return "YES"
    return "NO"

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_23(N))

