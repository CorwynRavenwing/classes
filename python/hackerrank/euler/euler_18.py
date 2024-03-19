# Enter your code here. Read input from STDIN. Print output to STDOUT

def euler_18(grid):
    # print("#check", grid)
    priorSums = {}
    for Row in grid:
        # print("#  Row", Row)
        Sums = {}
        for i, value in enumerate(Row):
            UL = priorSums.get(i-1, 0)
            UR = priorSums.get(i, 0)
            # print("#Up", UL, UR)
            Sums[i] = value + max(UL, UR)
            # print("#Now", value, Sums[i])
        priorSums = Sums
        # newRow = Sums.values()
        # print("#  Row", Row, "->", list(newRow))
    # print("#Sums", Sums)
    return max(Sums.values())

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    grid = [
        list(map(int, input().strip().split(' ')))
        for i in range(N)
    ]
    print(euler_18(grid))

