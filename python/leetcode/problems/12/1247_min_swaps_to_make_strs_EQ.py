class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

# VERSION 1:

        JOIN2 = lambda x: x[0] + x[1]
        pairs = tuple(map(JOIN2, zip(s1, s2)))
        counts = Counter(pairs)
        print(f'{counts=}')
        del counts['xx']
        del counts['yy']
        answer = 0
            
        if counts['xy'] >= 2:
            print(f'{counts=}')
            xy_pairs = counts['xy'] // 2
            print(f'  Use {xy_pairs=}')
            answer += xy_pairs
            counts['xy'] -= (2 * xy_pairs)
            if not counts['xy']:
                del counts['xy']

        if counts['yx'] >= 2:
            print(f'{counts=}')
            yx_pairs = counts['yx'] // 2
            print(f'  Use {yx_pairs=}')
            answer += yx_pairs
            counts['yx'] -= (2 * yx_pairs)
            if not counts['yx']:
                del counts['yx']

        if counts['xy'] and counts['yx']:
            print(f'{counts=}')
            print(f'  Use one of each')
            answer += 2
            counts['xy'] -= 1
            if not counts['xy']:
                del counts['xy']
            counts['yx'] -= 1
            if not counts['yx']:
                del counts['yx']

        if counts['xy'] or counts['yx']:
            print(f'{counts=}')
            print(f'  IMPOSSIBLE')
            return -1

        return answer

# VERSION 3:

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        JOIN2 = lambda x: x[0] + x[1]
        pairs = tuple(map(JOIN2, zip(s1, s2)))
        counts = Counter(pairs)
        print(f'{counts=}')
        answer = 0

        xy = counts['xy']
        yx = counts['yx']

        if xy >= 2:
            print(f'{counts=}')
            xy_pairs = xy // 2
            print(f'  Use {xy_pairs=}')
            answer += xy_pairs
            xy -= (2 * xy_pairs)

        if yx >= 2:
            print(f'{counts=}')
            yx_pairs = yx // 2
            print(f'  Use {yx_pairs=}')
            answer += yx_pairs
            yx -= (2 * yx_pairs)

        if xy and yx:
            print(f'{counts=}')
            print(f'  Use one of each')
            answer += 2
            xy -= 1
            yx -= 1

        if xy or yx:
            print(f'{counts=}')
            print(f'  IMPOSSIBLE')
            return -1

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: original (counts['xy'] version):
# NOTE: Runtime 3 ms Beats 7.41%
# NOTE: Memory 16.94 MB Beats 12.38%
# NOTE: second (xy version with "del")
# NOTE: (throws an error when variables are re-used)
# NOTE: third (xy version)
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.95 MB Beats 12.38%
# NOTE: Hugely faster, infinitessimally more memory
