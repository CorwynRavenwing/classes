def factorial(N):
    retval = N
    for i in range(1, N):
        retval *= i
        # print("#I", i, retval)
    return retval

def euler_20(N):
    F = factorial(N)
    digits = list(map(int, list(str(F))))
    # print("#digits", digits)
    return sum(digits)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_20(N))

