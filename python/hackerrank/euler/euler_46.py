
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

def sqrt(X):
    return int(X ** 0.5)

def euler_46(N):
    R = sqrt(N)
    count = 0
    for X in range(R+1):
        S = X * X
        P = N - 2 * S
        isP = is_prime(P)
        print(f"#{N=} {R=} {S=} {P=} {isP=}")
        if isP:
            count += 1
    return count

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_46(N))

