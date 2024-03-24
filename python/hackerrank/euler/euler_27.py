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

def make_euler_prime_fn(A, B):
    def inner(X):
        return (X * X) + (A * X) + B
    return inner

def count_euler_primes(A, B):
    # print(f"#Euler({A}, {B})")
    X = 0
    fn = make_euler_prime_fn(A, B)
    while True:
        F = fn(X)
        if not is_prime(F):
            return X
        X += 1
        # print(f"#  Prime #{X}: {F}")
    pass

def euler_27(N):
    retval = (None, None)
    max_EP = 0
    # shortcut:
    # n^2 + A*n + B
    # at n=0, this = B
    # therefore B must be prime.
    for B in range(1, N+1):
        if not is_prime(B):
            continue
        for absA in range(1, N+1):
            for A in [absA, -absA]:
                EP = count_euler_primes(A, B)
                # print("#A,B,EP", (A, B), EP)
                if max_EP < EP:
                    max_EP = EP
                    retval = (A, B)
                    # print("#MAX+", retval, max_EP)
    return ' '.join(map(str, retval))

N = int(input().strip())
print(euler_27(N))

