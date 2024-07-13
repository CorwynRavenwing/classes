class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def getScore_noCache(s: str) -> int:
            nonlocal x, y
            
            def found(test: str) -> bool:
                # easier to read in the if.. and while.. below
                nonlocal s
                return test in s

            # neither
            if not found('ab') and not found('ba'):
                return 0

            answer = 0
            while found('ab') or found('ba'):
                if x >= y:
                    # all possible AB if it's more expensive
                    while found('ab'):
                        answer += x
                        s = s.replace('ab', '', 1)
                    # then BA if any
                    if found('ba'):
                        answer += y
                        s = s.replace('ba', '', 1)
                else:
                    # all possible BA if it's more expensive
                    while found('ba'):
                        answer += y
                        s = s.replace('ba', '', 1)
                    # then AB if any
                    if found('ab'):
                        answer += x
                        s = s.replace('ab', '', 1)
            return answer

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
# NOTE: recursion was not necessary; cache is redundant but harmless
