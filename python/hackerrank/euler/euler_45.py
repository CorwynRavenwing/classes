
def sqrt(X):
    return int(X ** 0.5)

def triangle(N):
    return N * (N+1) // 2

def is_triangle(N):
    trial = sqrt(2 * N)
    T = triangle(trial)
    return T == N

def pent(n):
    P = n * (3 * n - 1) // 2
    return P

def is_pent(P):
    trial = sqrt(P * 2 / 3)
    Pn = pent(trial)
    Pn1 = pent(trial+1)
    # print("#ip()", P, trial, Pn, P == Pn, Pn1, P == Pn1)
    return P == Pn or P == Pn1

def hexagon(N):
    return N * (2 * N - 1)

def is_hexagon(H):
    trial = sqrt(H / 2)
    Hn = hexagon(trial)
    Hn1 = hexagon(trial+1)
    # print("#ih()", H, trial, Hn, H == Hn, Hn1, H == Hn1)
    return Hn == H or H == Hn1

def euler_45(N, a, b):
    if (a, b) == (3, 5):
        for n in range(1, N):
            P = pent(n)
            if P > N:
                break
            if is_triangle(P):
                print(P)
    elif (a, b) == (5, 6):
        for n in range(1, N):
            H = hexagon(n)
            if H > N:
                break
            if is_pent(H):
                print(H)

(N, a, b) = map(int, input().strip().split(' '))
euler_45(N, a, b)

