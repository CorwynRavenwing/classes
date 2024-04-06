
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
def factorial(N):
    retval = N
    for i in range(1, N):
        retval *= i
        # print("#I", i, retval)
    return retval

@with_cache
def factorial_sum(C):
    digits = map(int, list(str(C)))
    F = [
        factorial(d)
        for d in digits
    ]
    retval = sum(F)
    # print(f"#FS({C}) -> {F} -> {retval}")
    return retval

def euler_74(N, L):
    loop_lengths = {}
    for C in range(1, N):
        FS = C
        loop = []
        while FS not in loop:
            loop.append(FS)
            FS = factorial_sum(FS)
        # if C in [24, 42, 104, 114, 140, 141]:
        #     print(f"#{C=} {len(loop)}:{loop} {[FS]}")
        LL = len(loop)
        loop_lengths.setdefault(LL, [])
        loop_lengths[LL].append(C)
    retval = loop_lengths.get(L, [-1])
    # print(f"#loop_lengths[{L}]={retval}")
    return retval

T = int(input().strip())
for _ in range(T):
    (N, L) = map(int, input().strip().split(' '))
    print(' '.join(map(str, euler_74(N, L))))

