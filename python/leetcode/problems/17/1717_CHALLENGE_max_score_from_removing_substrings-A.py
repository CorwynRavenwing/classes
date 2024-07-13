class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def getScore_noCache(s: str) -> int:
            nonlocal x, y
            
            def found(X: str) -> bool:
                # easier to read in the if.. and while.. below
                nonlocal s
                return X in s

            # neither
            if not found('ab') and not found('ba'):
                return 0
            
            # both
            if found('ab') and found('ba'):
                return max([
                    x + getScore(s.replace('ab', '', 1)),
                    y + getScore(s.replace('ba', '', 1)),
                ])
            
            # only AB
            if found('ab') and not found('ba'):
                answer = 0
                while found('ab') and not found('ba'):
                    answer += x
                    s = s.replace('ab', '', 1)
                return answer + getScore(s)

            # only BA
            if not found('ab') and found('ba'):
                answer = 0
                while not found('ab') and found('ba'):
                    answer += y
                    s = s.replace('ba', '', 1)
                return answer + getScore(s)
            
        cache = {}
        def getScore(s: str) -> int:
            if s not in cache:
                cache[s] = getScore_noCache(s)
                print(f'getScore({s}) -> {cache[s]}')
            # else:
            #     print(f'getScore({s}) -> cache hit')
            return cache[s]
        
        only_ab = ''.join([
            C if C in 'ab' else 'X'
            for C in s
        ])
        # print(f'{only_ab=}')

        substrings = only_ab.split('X')
        # print(f'{substrings=}')

        return sum([
            getScore(SS)
            for SS in substrings
        ])
# NOTE: works and I'm proud of it, but Memory Limit Exceeded for large inputs
