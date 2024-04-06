
from typing import List

def with_cache(fn):
    cache_data = {}

    def inner(x):
        if x in cache_data:
            R = cache_data[x]
            print("#cache hit", x, R)
        else:
            R = fn(x)
            cache_data[x] = R
            print("#cache miss", x, R)
        return R
    return inner

primes: List[int] = []

@with_cache
def hard(T):
    (N, P) = T
    print(f"#hard({N},{P})")
    max_this_prime = N // P
    prime_index = primes.index(P)
    next_prime = (
        primes[prime_index + 1]
        if prime_index + 1 < len(primes)
        else None
    )
    possible = [
        easy(N - (P * this_prime), next_prime)
        for this_prime in range(max_this_prime + 1)
    ]
    return sum(possible)

def easy(N, P):
    print(f"#easy({N},{P})")
    if N == 0:
        return 1
    if P == 1:
        return 1
    if P is None:
        return 0
    return hard(
        (N, P)
    )
    pass

@with_cache
def is_prime(X):
    # print(f"#is_prime({X})")
    if X < 2:
        # print("#  No")
        return False
    for i in range(2, X+1):
        if i * i > X:
            break
        if X % i == 0:
            # print(f"#  found divisor {i}")
            return False
    # print("#  Yes")
    return True

def all_primes_below(N):
    return [
        P
        for P in range(N)
        if is_prime(P)
    ]

def euler_77(N):
    global primes
    primes = tuple(reversed(all_primes_below(N + 1)))
    print(f"#{primes=}")
    return easy(N, primes[0])

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_77(N))

