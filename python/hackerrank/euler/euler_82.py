
def euler_82(matrix):
    sums = []
    prior_row = []
    swap_matrix = list(zip(*matrix))
    for row_num, row in enumerate(swap_matrix):
        new_row = []
        print(f"#{row=}")
        for col_num, val in enumerate(row):
            print(f"#{row_num=} {col_num=} {val=}")
            priors = []
            if row_num == 0:
                priors.append(0)
            if row_num != 0:
                priors.append(prior_row[col_num])
            print(f"#    {priors=}")
            new_value = val + min(priors)
            print(f"#    -> {new_value}")
            new_row.append(new_value)
        for col_num, val in enumerate(row):
            print(f"#  {col_num=}")
            tries = [new_row[col_num]]
            if col_num != 0:
                tries.append(val + new_row[col_num - 1])
            if col_num + 1 != len(new_row):
                tries.append(val + new_row[col_num + 1])
            print(f"#  {tries=}")
            new_row[col_num] = min(tries)
        print(f"#sums={new_row}")
        sums.append(new_row)
        prior_row = new_row
    return min(sums[-1])

N = int(input().strip())
matrix = [
    list(map(int, input().strip().split(' ')))
    for _ in range(N)
]
print(euler_82(matrix))

