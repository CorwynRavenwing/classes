
def euler_67(grid):
    sum_dict = {}
    print(f"# [] -> {sum_dict}")
    for row in grid:
        new_sum_dict = {}
        for i, v in enumerate(row):
            UL = sum_dict.get(i-1, 0)
            UR = sum_dict.get(i, 0)
            new_sum_dict[i] = v + max(UL, UR)
        sum_dict = new_sum_dict
        print(f"# {row} -> {sum_dict}")
    return max(sum_dict.values())

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    grid = [
        list(map(int, input().strip().split(' ')))
        for i in range(N)
    ]
    print(euler_67(grid))

