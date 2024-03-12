N, M = tuple(map(int, input().split()))

B = '.|.'
lines = []
L = (N-1) // 2  # N is odd, therefore L is an int
for i in range(L):
    copies = 2*i + 1    
    block = B * copies
    line = block.center(M, '-')
    print(line)
    lines.append(line)

print("WELCOME".center(M, '-'))

while len(lines):
    print(lines.pop())

