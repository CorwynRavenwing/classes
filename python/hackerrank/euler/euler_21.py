
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
def D(X):
    pd = proper_divisors_of(X)
    return sum(pd)

def amicable(X):
    DX = D(X)
    DDX = D(DX)
    retval = (X == DDX) and (X != DX)
    # if retval:
    #     print("#A():", X, DX, DDX, retval)
    return retval

def euler_21(N):
    A = [
        X
        for X in range(1, N)
        if amicable(X)
    ]
    print("#A", A)
    return sum(A)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_21(N))

