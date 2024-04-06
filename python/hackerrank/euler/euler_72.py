
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

# def euler_72(N):
#     fractions = [
#         (x, y)
#         for y in range(1, N+1)
#         for x in range(1, y)
#         if relatively_prime(x, y)
#     ]
#     # fractions.sort(key=lambda T: T[0]/T[1])
#     # print(f"{fractions=}")
#     return len(fractions)
def euler_72(N):
    answer = 0
    for y in range(1, N+1):
        for x in range(1, y):
            if relatively_prime(x, y):
                answer += 1
    return answer


T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_72(N))

