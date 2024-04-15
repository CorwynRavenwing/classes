
def sqrt_int(X):
    return int(X ** 0.5)

def digits_lowest_form(X):
    # print(f"#DLF: BEFORE {X}")
    Xtemp = list(X)
    if Xtemp[1:]:
        while max(Xtemp[1:]) > 9:
            for i, val in enumerate(Xtemp):
                if i == 0:
                    continue
                if val <= 9:
                    continue
                transfer = val // 10
                Xtemp[i-1] += transfer
                Xtemp[i] -= transfer * 10
        while min(Xtemp[1:]) < 0:
            for i, val in enumerate(Xtemp):
                if i == 0:
                    continue
                if val >= 0:
                    continue
                transfer = abs(val // 10)
                Xtemp[i-1] -= transfer
                Xtemp[i] += transfer * 10

    X = tuple(Xtemp)
    # print(f"#DLF: AFTER  {X}")
    return X

# print(f"#{digits_lowest_form((0, 0, 0, 12345))=}")
# print(f"#{digits_lowest_form((10, -1, -2, -3))=}")

# usage: ds(5, 3) == (0, 0, 0, 5) == 0.005 == 5e-3
def digits_scientific(X, E):
    initial_zeros = [0] * E
    number = [X]
    return digits_lowest_form(initial_zeros + number)

def add_digits(X, Y):
    # print("#add_digits()")
    # print(f"#  {X=}")
    # print(f"#  {Y=}")
    LX = len(X)
    LY = len(Y)
    Xtemp = list(X) + [0] * (LY - LX)
    Ytemp = list(Y) + [0] * (LX - LY)
    zipped = zip(Xtemp, Ytemp)
    Ztemp = tuple(map(sum, zipped))
    Z = digits_lowest_form(Ztemp)
    # print(f"#  {Z=}")
    return Z

def subtract_digits(X, Y):
    negativeY = tuple([
        - digit
        for digit in Y
    ])
    # do not call digits_lowest_form here
    return add_digits(X, negativeY)

def digits_times_int(X, INT):
    Z = tuple([
        digit * INT
        for digit in X
    ])
    return digits_lowest_form(Z)

def digits_shift_times_10(X):
    # print(f"#DSx10: BEFORE {X}")
    Xtemp = list(X)
    INT = Xtemp.pop(0)
    TENTHS = Xtemp.pop(0) if Xtemp else 0
    NEW_INT = INT * 10 + TENTHS
    Ztemp = tuple([NEW_INT] + Xtemp)
    Z = digits_lowest_form(Ztemp)
    # print(f"#DSx10: AFTER  {Z}")
    return Z

def sqrt_digits(X, length):
    INT = sqrt_int(X)
    retval = [INT]
    if INT * INT == X:
        return tuple(retval)
    remainder = tuple([X - INT])
    while len(retval) <= length:
        remainder = digits_shift_times_10(remainder)
        print("# " + "-" * 60)
        print(f"# RET={retval}")
        print(f"# REM={remainder}")
        accumulator = (0,)
        square_frac = ()
        prev_comparitor = ()
        comparitor = ()
        for index in range(1, 11):
            # retval_times_2 = digits_times_int(retval, 2)
            # accumulator = add_digits(accumulator, retval_times_2)
            accumulator = digits_times_int(retval, 2 * index)
            # print(f"#   I={index} A={accumulator}")
            square = index * index
            square_frac = digits_scientific(square, len(retval))
            # print(f"#   SQ={square} F={square_frac}")
            prev_comparitor = comparitor
            # print(f"#   PREV={prev_comparitor}")
            comparitor = add_digits(accumulator, square_frac)
            # print(f"#   I={index} COMP={comparitor}")
            # print("#" + "-" * 20)
            if comparitor > remainder:
                # print("# TOO HIGH, USE PREVIOUS")
                print(f"# {prev_comparitor[:5]} < {remainder[:5]} < {comparitor[:5]}")
                retval.append(index - 1)
                remainder = subtract_digits(remainder, prev_comparitor)
                print(f"# new RET={retval}")
                print(f"# new REM={remainder}")
                break
    return digits_lowest_form(retval)

def sqrt_sum(X, P):
    digits = sqrt_digits(X, P+10)
    if len(digits) == 1:
        print(f"#{X} is a perfect square: {digits[0]}")
        return 0
    digits = digits[:P]   # cut off at P digits
    print(f"#{X} {P} {digits}")
    return sum(digits)

# print(sqrt_sum(2, 10))
# print(sqrt_sum(4, 10))

def euler_80(N, P):
    answers = [
        sqrt_sum(i, P)
        for i in range(N + 1)
    ]
    return sum(answers)

N = int(input().strip())
P = int(input().strip())
print(euler_80(N, P))

