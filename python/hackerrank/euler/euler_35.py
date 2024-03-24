
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

# L: List[int]
# return int
def list_to_int(L):
    return int(''.join(map(str, L)))

# X: int
# return List[int]
def int_to_list(X):
    return list(map(int, list(str(X))))

def rotate_list(L):
    return L[1:] + L[:1]

def rotate_int(X):
    XL = int_to_list(X)
    YL = rotate_list(XL)
    Y = list_to_int(YL)
    # print(f"#R {X} -> {Y}")
    return Y

def all_rotations_prime(X):
    if not is_prime(X):
        return False
    Y = X
    while True:
        Y = rotate_int(Y)
        if Y == X:
            break
        if not is_prime(Y):
            return False
    return True

def euler_35(N):
    retval = []
    for X in range(N):
        if all_rotations_prime(X):
            retval.append(X)
    # print(f"#{retval=}")
    return sum(retval) if len(retval) else 0

N = int(input().strip())
print(euler_35(N))

