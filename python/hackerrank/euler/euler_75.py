
def possible_triangles(P):
    retval = []
    for A in range(1, 1 + P // 3):
        # A^2 + B^2 = C^2
        # C = P - (A+B)
        # C^2 = (P-(A+B))^2
        # C^2 = P^2 - 2P(A+B) + (A+B)^2
        # C^2 = P^2 - 2PA - 2PB + A^2 + 2AB + B^2
        # 2PB - 2AB = P^2 - 2PA
        # 2B(P - A) = P^2 - 2PA
        # B = P(P/2 - A)/(P - A)
        if (P - A) == 0:
            continue
        B = P * (P//2 - A)//(P - A)
        if B < A:
            continue
        C = P - (A+B)
        if A * A + B * B == C * C:
            retval.append((A, B, C))
    return retval

def triangle_count(P):
    return len(possible_triangles(P))

def euler_75(N):
    one_solution = [
        P
        for P in range(1, N+1)
        if triangle_count(P) == 1
    ]
    return len(one_solution)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_75(N))

