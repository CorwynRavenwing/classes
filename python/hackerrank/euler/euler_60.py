
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

def all_primes_below(N):
    return [
        P
        for P in range(N)
        if is_prime(P)
    ]

def concat_int(A, B):
    return int(str(A)+str(B))
    
def euler_60(N, K):
    APBN = all_primes_below(N)
    # print(f"#{N=} {APBN=}")
    pairs = []
    for P1 in APBN:
        for P2 in APBN:
            if P2 < P1:
                continue
            T1 = concat_int(P1, P2)
            T2 = concat_int(P2, P1)
            Q1 = is_prime(T1)
            Q2 = is_prime(T2)
            # print(f"{P1} {P2} {T1} {T2} {Q1} {Q2}")
            if Q1 and Q2:
                pairs.append((P1, P2))
                # if P1 != P2:
                #     pairs.append((P2, P1))
    pairs.sort()
    # print(f"#{pairs=}")
    groups = {}
    groups[2] = pairs
    for i in range(3, K+1):
        prior_group = groups[i - 1]
        groups[i] = []
        for PG in prior_group:
            first_num = PG[0]
            pairs_with_group = [
                b
                for (a, b) in pairs
                if a == first_num
            ]
            # print(f"#PWG {PG} {first_num} {pairs_with_group}")
            for num in PG:
                pairs_with_group = [
                    PWG
                    for PWG in pairs_with_group
                    if (num, PWG) in pairs
                    # or (PWG, num) in pairs
                ]
                # print(f"#PWG {PG}+{num} {pairs_with_group}")
            # print(f"#PWG {PG} (done) {pairs_with_group}")
            for PWG in pairs_with_group:
                groups[i].append(list(PG) + [PWG])
                # print("#YES", PG, PWG)
    # print(f"{groups}")
    answers = [
        sum(G)
        for G in groups[K]
    ]
    answers.sort()
    return map(str, answers)

(N, K) = map(int, input().strip().split(' '))
print('\n'.join(euler_60(N, K)))

