# Enter your code here. Read input from STDIN. Print output to STDOUT

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

# test tc0 speeds with/without cache:
#  no,  no: 0.028s
# yes,  no: 0.031s
#  no, yes: 0.030s
# yes, yes: 0.029s

@with_cache
def collatz_next(N):
    if N % 2 == 0:
        return N // 2
    else:
        return 3 * N + 1

@with_cache
def collatz_chain_length(N):
    if N == 1:
        return 1
    CN = collatz_next(N)
    return 1 + collatz_chain_length(CN)

def euler_14(N):
    CCL = [
        (i, collatz_chain_length(i))
        for i in range(1, N+1)
    ]
    print("#CCL", CCL)
    lengths = [
        L
        for (i, L) in CCL
    ]
    print("#lengths", lengths)
    maxlen = max(lengths)
    print("#maxlen", maxlen)
    maxes = [
        i
        for (i, L) in CCL
        if L == maxlen
    ]
    print("#maxes", maxes)
    return max(maxes)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_14(N))

