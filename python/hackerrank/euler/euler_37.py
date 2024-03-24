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
    if X is None:
        # print("#  No")
        return False
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

def list_to_int(L):
    return int(''.join(map(str, L))) if len(L) else None

def int_to_list(X):
    return list(map(int, list(str(X))))

def truncate_int_L(X):
    XL = int_to_list(X)
    YL = XL[1:]
    Y = list_to_int(YL)
    return Y

def truncate_int_R(X):
    XL = int_to_list(X)
    YL = XL[:-1]
    Y = list_to_int(YL)
    return Y

def characters_legal(X):
    XL = int_to_list(X)
    X0 = XL.pop(0)
    if X0 not in [2, 3, 5, 7]:
        return False
    XN = XL.pop(-1)
    if XN not in [3, 7]:
        return False
    for x in XL:
        if x not in [1, 3, 7, 9]:
            return False
    return True

def all_truncations_prime(X):
    if not characters_legal(X):
        # print(f"#NO: CHARS {X=}")
        return False
    if not is_prime(X):
        # print(f"#NO: {X=}")
        return False
    Y = X
    # print(f"#CHECK: {X=}")
    while Y is not None:
        Y = truncate_int_L(Y)
        if Y is None:
            continue
        if not is_prime(Y):
            # print(f"#NO: {Y=}")
            return False
    Z = X
    while Z is not None:
        Z = truncate_int_R(Z)
        if Z is None:
            continue
        if not is_prime(Z):
            # print(f"#NO: {Z=}")
            return False
    # print(f"#YES: {X=}")
    return True

def euler_37(N):
    retval = []
    # 10 because we are ignoring single digit numbers
    for X in range(10, N):
        if all_truncations_prime(X):
            print("#FOUND", X)
            retval.append(X)
    print(f"#{retval=}")
    return sum(retval) if len(retval) else 0

N = int(input().strip())
print(euler_37(N))

