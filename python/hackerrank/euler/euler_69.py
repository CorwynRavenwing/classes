
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

# does not return '1' among the factors
@with_cache
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

def relatively_prime(A, B):
    A_factors = set(primeFactors(A))
    B_factors = set(primeFactors(B))
    return A_factors.isdisjoint(B_factors)

def rp_below(n):
    return [
        i
        for i in range(1, n)
        if relatively_prime(i, n)
    ]

# print(f"#TEST {rp_below(10)=}")

def phi(n):
    return len(rp_below(n))

def n_over_phi(n):
    # print(f"# {n} / {phi(n)}")
    return n / phi(n)

def euler_69(N):
    tuples = [
        (n_over_phi(n), n)
        for n in range(2, N)
    ]
    tuples.sort(reverse=True)
    print(f"#{tuples=}")
    maximum = tuples[0][0]
    answers = [
        b
        for (a, b) in tuples
        if a == maximum
    ]
    print(f"#{answers=}")
    return min(answers)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_69(N))

