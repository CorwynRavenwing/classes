# Enter your code here. Read input from STDIN. Print output to STDOUT

def euler_13(L):
    # L: List[str] where str are 50-digit numbers
    # print("#L", L)
    groups = tuple(zip(*L))
    # print("#groups", groups)
    sums = [
        sum(map(int, G))
        for G in groups
    ]
    # print("#sums", sums)
    while max(sums) >= 10:
        if sums[0] >= 10:
            sums = [0] + sums
            # print("#sums", sums)
        for i in range(len(sums) - 1):
            if sums[i+1] >= 10:
                T1 = (sums[i], sums[i+1])
                sums[i] += 1
                sums[i+1] -= 10
                T2 = (sums[i], sums[i+1])
                # print("#I  ", i, T1, T2)
        # print("#sums", sums)
    answer = sums[:10]
    # print("#answer", answer)
    return ''.join(map(str, answer))

N = int(input().strip())
L = [
    input().strip()
    for _ in range(N)
]
print(euler_13(L))

