
def euler_81(matrix):
    sums = []
    prior_row = []
    for row_num, row in enumerate(matrix):
        new_row = []
        print(f"#{row=}")
        for col_num, val in enumerate(row):
            print(f"#{row_num=} {col_num=} {val=}")
            priors = []
            if (row_num, col_num) == (0, 0):
                priors.append(0)
            if row_num != 0:
                priors.append(prior_row[col_num])
            if col_num != 0:
                priors.append(new_row[col_num - 1])
            print(f"#    {priors=}")
            new_value = val + min(priors)
            print(f"#    -> {new_value}")
            new_row.append(new_value)
        print(f"#sums={new_row}")
        sums.append(new_row)
        prior_row = new_row
    return sums[-1][-1]

N = int(input().strip())
matrix = [
    list(map(int, input().strip().split(' ')))
    for _ in range(N)
]
print(euler_81(matrix))

