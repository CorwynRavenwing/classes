
def digits_of(x):
    return tuple(str(x))

def is_palindrome(x):
    digits_of_x = digits_of(x)
    L = len(digits_of_x)
    for i in range(L // 2):
        # even lengths: checks all digits
        # odd lengths: checks all but the center digit
        if digits_of_x[i] != digits_of_x[L-i-1]:
            return False
    return True

def int_to_str(
    n,
    b,
    symbols='0123456789abcdefghijklmnopqrstuvwxyz',
):
    try:
        return (
            (
                int_to_str(n // b, b) if n >= b else ""
            ) + (
                symbols[n % b]
            )
        )
    except IndexError:
        raise ValueError(
            "Not enough symbols for this number and base"
        )
            
def euler_36(N, K):
    retval = []
    for C in range(1, N):
        if not is_palindrome(C):
            continue
        base_K = int_to_str(C, K)
        # print(f"#{C} -> {base_K} (b{K})")
        if not is_palindrome(base_K):
            continue
        # print(f"#FOUND {C} palindrome in both bases")
        retval.append(C)
    # print(f"{retval=}")
    return sum(retval) if len(retval) else 0

(N, K) = map(int, input().strip().split(' '))
print(euler_36(N, K))

