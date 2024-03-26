
# does not return '1' among the factors
def primeFactors(n):
    # print("#pF()", n)
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            # print("#F", i)
            factors.append(i)
            n //= i
        i += 1
        if i > n:
            break
    return factors

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
def count_prime_factors(n):
    retval = len(set(primeFactors(n)))
    # print(f"#cpf({n}) -> {retval}")
    return retval

def euler_47(N, K):
    for n in range(N+1):
        if count_prime_factors(n) != K:
            continue
        print(f"#{n=} YES")
        fail = False
        for i in range(n+1, n+K):
            if count_prime_factors(i) != K:
                fail = True
                print(f"#  {i=} NO")
                break
            else:
                print(f"#  {i=} YES")
        if not fail:
            print(n)

(N, K) = map(int, input().strip().split(' '))
euler_47(N, K)

