
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

