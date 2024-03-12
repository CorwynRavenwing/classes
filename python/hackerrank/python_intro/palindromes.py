def positive(i):
    return i > 0

def palindromic(i):
    if not positive(i):
        return False
    s = str(i)
    l = list(s)
    rl = l
    rl.reverse()
    rs = ''.join(rl)
    ri = int(rs)
    # print("P:", i, s, rs, ri, (i == ri))
    return i == ri

n = int(input())
items = tuple(map(int, input().split()))
positives = tuple(map(positive, items))
palindromes = tuple(map(palindromic, items))

print(all(positives) and any(palindromes))

