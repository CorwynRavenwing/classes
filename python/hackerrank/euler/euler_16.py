# Enter your code here. Read input from STDIN. Print output to STDOUT

def euler_16(N):
    print("#N", N)
    power = 2 ** N
    print("#power", power)
    digits = list(str(power))
    print("#digits", digits)
    return sum(map(int, digits))

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_16(N))

