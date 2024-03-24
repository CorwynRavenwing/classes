
# L: List[int]
# return int
def list_to_int(L):
    return int(''.join(map(str, L)))

# X: int
# return List[int]
def int_to_list(X):
    return list(map(int, list(str(X))))

# F1: Tuple[int, int]
# F2: same
# return bool
def fractions_equivalent(F1, F2):
    (num1, den1) = F1
    (num2, den2) = F2

    return num1 * den2 == num2 * den1

# in: list
# out: list
# cancels one digit
def all_possible_cancels(possibles):
    retval = []
    for fracL in possibles:
        (numL, denL) = fracL
        for i, d in enumerate(numL):
            if d == 0:
                continue
            if d not in denL:
                continue
            num_without_d = numL[:]
            pop_d = num_without_d.pop(i)
            assert pop_d == d
            for j, e in enumerate(denL):
                if d != e:
                    continue
                den_without_e = denL[:]
                pop_e = den_without_e.pop(j)
                assert pop_e == e
                newL = (num_without_d, den_without_e)
                if newL not in retval:
                    retval.append(newL)
    return retval

# in: one
# out: list
# cancels K digits
def all_possible_cancelled_fractions(fracL, K):
    possibles = [fracL]
    # print(f"{possibles=}")
    for i in range(K):
        possibles = all_possible_cancels(possibles)
        # print(f"{possibles=}")
    return possibles

def euler_33(N, K):
    retval = []
    min_N_digit = 10 ** (N - 1)   # 4 -> 1000
    max_N_digit = (10 ** N) - 1   # 4 -> 9999
    for num in range(min_N_digit, max_N_digit + 1):
        numL = int_to_list(num)
        for den in range(num + 1, max_N_digit + 1):
            denL = int_to_list(den)
            frac = (num, den)
            fracL = (numL, denL)
            APCF = all_possible_cancelled_fractions(fracL, K)
            # print(f"{APCF=}")
            for possL in APCF:
                (nL, dL) = possL
                (n, d) = list_to_int(nL), list_to_int(dL)
                poss = (n, d)

                if not fractions_equivalent(frac, poss):
                    continue
                # print(f"FOUND: {frac}, {poss}")
                retval.append(frac)
    # print(f"{retval=}")
    grouped = zip(*retval)
    summed = map(sum, grouped)
    return ' '.join(map(str, summed))

(N, K) = tuple(map(int, input().strip().split(' ')))
print(euler_33(N, K))

