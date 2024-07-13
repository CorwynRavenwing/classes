class Solution:
    def numWays(self, s: str) -> int:

        mod = 10 ** 9 + 7

        counts = Counter(s)
        ones = counts['1']
        zeros = counts['0']
        if counts['1'] == 0:
            print(f'Special case: no ones, {zeros=}')
            # special case, all zeros, needing split into 3 non-empty parts
            # if zeros were e.g. 7, the answer would be 15 = Triangle(5),
            # computed as (5)(6)/2.  In terms of the 7, this equals:
            answer = (zeros - 1) * (zeros - 2) // 2
            return answer % mod
            # in the case of s = '', zeros will also be 0,
            # and this will spuriously return (-1)(-2)/2 = (2/2) = 1,
            # but I think that value of s is forbidden.
        
        if ones % 3 != 0:
            print(f'Failure case: {ones=} not divisible by 3')
            return 0
        
        fraction = ones // 3
        s = s.replace('1','A', fraction)
        s = s.replace('1','B', fraction)
        s = s.replace('B','!', 1)
        s = s.replace('1','C', fraction)
        if '1' in s:
            raise Exception(f'Logic error: {3} * {fraction} != {ones}')
        # print(f'{s=}')
        prior = 'do this until we dont change anymore'
        while prior != s:
            prior = s
            s = s.replace('0A', 'A')
            s = s.replace('AA', 'A')
            s = s.replace('0B', 'B')
            s = s.replace('BB', 'B')
            s = s.replace('!B', '!')
            s = s.replace('C0', 'C')
            s = s.replace('CC', 'C')
            # print(f'{s=}')
        parts = s.split('!')
        numbers = tuple(map(len, parts))
        print(f'{numbers}')
        (A, B) = numbers
        answer = (A * B)
        return answer % mod

