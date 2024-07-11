class Solution:
    def maxDiff(self, num: int) -> int:

        numStr = str(num)
        possible = {numStr}
        digits = sorted(set(numStr))
        print(f'init: {numStr} ({digits})')
        for D in digits:
            for R in map(str, range(10)):
                newStr = numStr.replace(D, R)
                if newStr[0] == '0':
                    print(f'{D}->{R}: {newStr} (INVALID, leading 0)')
                else:
                    print(f'{D}->{R}: {newStr}')
                    possible.add(newStr)
        print(f'{possible=}')
        return int(max(possible)) - int(min(possible))
# NOTE: 35 ms; Beats 66.43%
