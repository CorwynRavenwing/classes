# Enter your code here. Read input from STDIN. Print output to STDOUT

def euler_15(N, M):
    Mod = 10 ** 9 + 7
    print("#Mod", Mod)
    Row = [1] * (N+1)
    for _ in range(M):
        print("#Row", _, Row)
        total = 0
        NextRow = []
        for i, value in enumerate(Row):
            total += value
            total %= Mod
            NextRow.append(total)
        Row = NextRow
    print("#Row", M, Row)
    return Row[-1]

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split(' '))
    print(euler_15(N, M))

