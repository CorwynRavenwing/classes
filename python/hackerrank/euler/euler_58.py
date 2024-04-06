
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

def euler_58(N):
    X = 1
    side_length = 1
    distance = 0
    numbers = 0
    primes = 0
    print(f"#start {X=}")
    numbers += 1
    if is_prime(X):
        primes += 1
    while True:
        side_length += 2
        distance += 2
        for i in range(4):
            X += distance
            print(f"#loop {distance=} {i=} {X=}")
            numbers += 1
            if is_prime(X):
                primes += 1
        ratio = 100 * primes / numbers
        print(f"#  {ratio=}")
        if ratio < N:
            break
    return side_length

N = int(input().strip())
print(euler_58(N))

