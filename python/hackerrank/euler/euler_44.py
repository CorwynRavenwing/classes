

# highest_n = 0
# highest_pent_n = 0
# known_pents = []

def pent(n):
    # global known_pents
    P = n * (3 * n - 1) // 2
    # if P not in known_pents:
    #     # print(f"#pent({n}) = {P}")
    #     known_pents.append(P)
    return P

def is_pent(P):
    trial = int((P * 2 / 3) ** 0.5)
    Pn = pent(trial)
    Pn1 = pent(trial+1)
    # print("#ip()", P, trial, Pn, P == Pn, Pn1, P == Pn1)
    return P == Pn or P == Pn1

# def is_pent_2(P):
#     global highest_n, highest_pent_n, known_pents
#     while highest_pent_n < P:
#         highest_n += 1
#         highest_pent_n = pent(highest_n)
#     answer = P in known_pents
#     # print(f"#is_pent({P}) = {answer}")
#     return answer

def euler_44(N, K):
    # print(f"#euler_44({N}, {K})")
    for n in range(K, N+1):
        if n in [0, K]:
            continue
        # print(f"#{n=} {K=}")
        Pn = pent(n)
        Pnk = pent(n - K)
        # print(f"#{Pn=} +/- {Pnk=}")
        if is_pent(Pn + Pnk):
            # print("#FOUND(+)", n, Pn)
            print(Pn)
        elif is_pent(Pn - Pnk):
            # print("#FOUND(-)", n, Pn)
            print(Pn)

(N, K) = map(int, input().strip().split(' '))
euler_44(N, K)

