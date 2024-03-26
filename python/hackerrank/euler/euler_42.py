
def triangle(N):
    return N * (N+1) // 2

def sqrt(X):
    return int(X ** 0.5)

def euler_42(N):
    trial = sqrt(2 * N)
    T = triangle(trial)
    print(f"#{N=} {trial=} {T=} {T == N}")
    if T == N:
        return trial
    return -1

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_42(N))

