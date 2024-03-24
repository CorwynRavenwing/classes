
# L: List[int]
# return int
def list_to_int(L):
    return int(''.join(map(str, L)))

# X: int
# return List[int]
def int_to_list(X):
    return list(map(int, list(str(X))))

def min_number_with_length(X, N):
    # ignoring N for now
    L = [1] * X
    return list_to_int(L)
    # e.g. 4 -> 1111

def max_number_with_length(X, N):
    L = [N] * X
    return list_to_int(L)
    # e.g. 4 -> 9999

def int_len(X):
    return len(str(X))

def min_product_length(a_len, b_len, N):
    # ignoring N for now
    A = min_number_with_length(a_len, 1)
    B = min_number_with_length(b_len, 1)
    C = A * B
    return int_len(C)

def max_product_length(a_len, b_len, N):
    A = max_number_with_length(a_len, N)
    B = max_number_with_length(b_len, N)
    C = A * B
    return int_len(C)

def calculate_digits_in_product(N):
    product_len_dict = {}
    for a_len in range(1, N):
        for b_len in range(a_len, N):
            c_len = N - a_len - b_len
            if c_len <= 0:
                # print("#C <= 0", c_len)
                break
            min_c_len = min_product_length(a_len, b_len, N)
            max_c_len = max_product_length(a_len, b_len, N)
            if min_c_len <= c_len <= max_c_len:
                # print("#C OK", min_c_len, c_len, max_c_len)
                product_len_dict[
                    (a_len, b_len)
                ] = c_len
            # else:
            #     print("#C BAD", min_c_len, c_len, max_c_len)
    # print("#PL", product_len_dict)
    return product_len_dict

def invalid_digits(L, ok_digits):
    bad = set(L) - set(ok_digits)
    # print(f"{set(L)} - {set(ok_digits)} = {bad}")
    return len(bad) > 0

def repeated_digits(L):
    # print(f"{L} {set(L)}")
    return len(L) != len(set(L))

def euler_32(N):
    product_len_dict = calculate_digits_in_product(N)
    ok_digits = tuple(range(1, N+1))
    successes = set()
    # print("#OK.A", ok_digits)
    for key, value in product_len_dict.items():
        a_len, b_len = key
        c_len = value
        min_A = min_number_with_length(a_len, 1)
        max_A = max_number_with_length(a_len, N)
        min_B = min_number_with_length(b_len, 1)
        max_B = max_number_with_length(b_len, N)
        for A in range(min_A, max_A+1):
            aL = int_to_list(A)
            if invalid_digits(aL, ok_digits):
                continue
            if repeated_digits(aL):
                continue
            ok_for_B = [
                x
                for x in ok_digits
                if x not in aL
            ]
            # print("#OK.B", ok_for_B)
            for B in range(min_B, max_B+1):
                if B < A:
                    # print(f"{B} < {A}")
                    continue
                bL = int_to_list(B)
                if invalid_digits(bL, ok_for_B):
                    continue
                if repeated_digits(bL):
                    continue
                C = A * B
                # print("#AxB", A, B, C)
                cL = int_to_list(C)
                if len(cL) < c_len:
                    # print(f"#C {len(cL)} < {c_len}: continue")
                    continue
                if len(cL) > c_len:
                    # print(f"#C {len(cL)} > {c_len}: break")
                    break
                ok_for_C = [
                    x
                    for x in ok_for_B
                    if x not in bL
                ]
                # print("#OK.C", ok_for_C)
                if invalid_digits(cL, ok_for_C):
                    continue
                if repeated_digits(cL):
                    continue
                # print(f"#SUCCESS!  {A}x{B}={C}")
                successes.add(C)
    # print("#successes", successes)
    return sum(successes)

N = int(input().strip())
print(euler_32(N))

