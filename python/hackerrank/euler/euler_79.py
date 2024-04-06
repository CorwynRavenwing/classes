
def euler_79(codes):
    prerequisites = {}
    # all_letters = set()
    for code in codes:
        for i, C in enumerate(code):
            prerequisites.setdefault(C, [])
            prerequisites[C].extend(code[:i])
    retval = []
    P = prerequisites.copy()
    while P:
        print(f"#{retval=} {P=}")
        impossible = [
            C
            for C, perq in P.items()
            for P in perq
            if P not in retval
        ]
        # print(f"#{impossible=}")
        possible = [
            C
            for C in P
            if C not in impossible
        ]
        print(f"#{possible=}")
        if not possible:
            return "SMTH WRONG"
        take = min(possible)
        retval.append(take)
        P.pop(take)
    # check that prerequisites were not violated:
    for C, perq in prerequisites.items():
        C_index = retval.index(C)
        P_indexes = [
            retval.index(P)
            for P in perq
        ]
        print(f"#{C_index=} {P_indexes=}")
        failures = [
            index
            for index in P_indexes
            if index > C_index
        ]
        print(f"#{failures=}")
        if failures:
            return "SMTH WRONG"
    return ''.join(retval)

T = int(input().strip())
codes = [
    input().strip()
    for _ in range(T)
]
print(euler_79(codes))

