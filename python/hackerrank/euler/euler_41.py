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
    # print(f"#  PRIME {X}")
    return True

def is_pandigital_list(digits):
    length = len(digits)
    target = list(range(1, length+1))
    return set(digits) == set(target)

def is_pandigital(X):
    digits = list(map(int, str(X)))
    return is_pandigital_list(digits)

# test
# print(f"#{is_prime(4231)=}")
# print(f"#{is_pandigital(4231)=}")

def list_to_int(digits):
    return int(
        ''.join(
            map(str, digits)
        )
    )

def increment_pandigital(digits):
    length = len(digits)
    # target = list(range(1, length+1))
    # print("#IP()", length, digits)
    digits[-1] += 1
    # print("#IP++", digits)
    while digits[-1] in digits[:-1]:
        # last digit is found in all-but-last-digit substring
        digits[-1] += 1
        # print("#IP A", length, digits)
    while 10 > digits[-1] > length:
        # last digit outside of 1..n range but not >= 10
        digits[-1] += 1
        # could probably just jump to "10" here
        # print("#IP B", length, digits)
    while max(digits) > length:
        # any digit outside of 1..n range b/c of recent increments
        M = max(digits)
        I = digits.index(M)
        while 10 > digits[I] > length:
            # digit I is outside of 1..n range but not >= 10
            digits[I] += 1
            # print("#IP C", length, digits)
            # could probably just jump to "10" here
            digits[I+1:] = [0] * len(digits[I+1:])
            # print("#IP D", length, digits)
        if digits[I] >= 10:
            if I == 0:
                # first, add a new leftmost digit if necessary
                digits = [0] + digits
                # print("#IP E", length, digits)
                length = len(digits)
                # or maybe just add 1?
                if length >= 10:
                    return None
                continue
            digits[I-1] += 1
            digits[I] -= 10
            # print("#IP F", length, digits)
            digits[I+1:] = [0] * len(digits[I+1:])
            # print("#IP G", length, digits)
            while digits[I-1] in digits[:I-1]:
                # (I-1)th digit is found in left-of-that substring
                digits[I-1] += 1
                # print("#IP G+", length, digits)
        while 0 in digits:
            target = list(range(1, length+1))
            # print("#IP H", length, digits)
            I = digits.index(0)
            # print(f"#{I=}")
            # print(f"#{target=}")
            # print(f"#{digits[:I]=}")
            available = [
                d
                for d in target
                if d not in digits[:I]
            ]
            # maybe set(target) - set(digits[:I]) ?
            # print("#available", available)
            digits[I] = min(available)
            # print("#IP I", length, digits)
    if not is_pandigital_list(digits):
        print("#ERROR", digits)
    assert is_pandigital_list(digits)
    # print("#IP->", length, digits)
    return digits

def euler_41(N):
    largest = -1
    digits = [0]
    X = list_to_int(digits)
    while X <= N:
        if is_pandigital(X) and is_prime(X):
            largest = max(largest, X)
            # print("#FOUND", X)
        digits = increment_pandigital(digits)
        if digits is None:
            break
        X = list_to_int(digits)
    return largest

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_41(N))

