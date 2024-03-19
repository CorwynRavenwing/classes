# Enter your code here. Read input from STDIN. Print output to STDOUT

def divisors_of(X):
    # print(f"#divisors_of({X})")
    retval = set()
    for i in range(1, X+1):
        if i * i > X:
            # print(f"#  {i}^2 ({i*i}) > {X}")
            break
        if X % i == 0:
            j = X // i
            # print(f"#  found divisors {i}, {j}")
            retval.add(i)
            retval.add(j)
    return tuple(retval)

def euler_12(N):
    TN = 0
    i = 0
    while True:
        i += 1
        TN += i
        # print("#I, TN", i, TN)
        div = divisors_of(TN)
        # print("#div", div)
        if len(div) > N:
            return TN
    
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_12(N))

