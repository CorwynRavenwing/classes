
def euler_62(N, K):
    sets = {}
    for c in range(N):
        c3 = c ** 3
        digits = list(str(c3))
        digits.sort()
        key = ''.join(map(str, digits))
        # print(f"#{c} {c3} {key}")
        sets.setdefault(key, [])
        sets[key].append(c3)
    length_K = {
        key: sets[key]
        for key in sets
        if len(sets[key]) == K
    }
    # print("#length_K:", length_K)
    answer = [
        min(length_K[key])
        for key in length_K
    ]
    return answer

(N, K) = map(int, input().strip().split(' '))
print('\n'.join(map(str, euler_62(N, K))))

