
def sum_power(L, N):
    Y = sum([
        d ** N
        for d in L
    ])
    return Y

def num_to_digits(X):
    return tuple(map(int,list(str(X))))

def sum_digits_power(X, N):
    digits = num_to_digits(X)
    Y = sum_power(digits, N)
    return Y

def count_digits(X):
    digits = num_to_digits(X)
    return len(digits)

def check(X, N):
    Y = sum_digits_power(X, N)
    return X == Y

def euler_30(N):
    retval = 0
    size = 1
    looping = True
    while looping:
        size += 1   # 1-digit answers aren't allowed
        print("#SIZE", size)
        digit_values = {}
        for d in range(10):
            sp = d ** N
            if count_digits(sp) > size:
                # print(f"#D {d} {sp} TOO BIG")
                # because, if 7^3 is too big, 8^3 will be too
                break
            # print(f"#D {d} {sp}")
            digit_values[(d,)] = sp
        # print(f"#{digit_values=}")
        fragments = {(): 0}
        # print(f"#{fragments=}")
        for i in range(1, size + 1):
            new_fragments = {}
            for L, total in fragments.items():
                max_L = max(L) if len(L) else 0
                # print(f"#{L=} {max_L=}")
                for D, value in digit_values.items():
                    if D[0] < max_L:
                        # print(f"#skip {D}")
                        continue
                    new_L = L + D
                    new_total = total + value
                    if count_digits(new_total) > size:
                        # print(f"#{new_L}{new_total} TOO BIG")
                        continue
                    new_fragments[new_L] = new_total
                # next digit_values
            # next fragments
            fragments = new_fragments
            # print(f"#{fragments=}")
            attempts = 0
            for L, total in fragments.items():
                D = num_to_digits(total)
                if len(D) != size:
                    # print(f"#{L=} {total} TOO SHORT")
                    continue
                M = tuple(sorted(D))
                attempts += 1
                if L != M:
                    # print(f"#{L=} {M=} DIFFERENT")
                    continue
                if check(total, N):
                    print(f"#FOUND {total} {L}")
                    retval += total
            # next fragments
            # print(f"#{attempts=}")
            if attempts == 0:
                # all X-digit numbers have sums that are
                # too short or too long
                looping = False
                break
        # next size
    # next looping
    print("#Loop exited")
    return retval

N = int(input().strip())
print(euler_30(N))

