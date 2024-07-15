class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        cache = {}
        def NOS(n: int, k: int, depth=0) -> int:
            # in this version, n = distance instead
            # of fenceposts. i.e. +--+--+--+ == 3 not 4.
            margin = '  ' * depth
            pair = (n, k)
            if pair not in cache:
                print(f'{margin}NOS({n},{k}): ...')
                if k == 0:
                    answer = 1
                    print(f'{margin}  0 : {answer}')
                elif k == n:
                    answer = 1
                    print(f'{margin}  = : {answer}')
                elif k > n:
                    answer = 0
                    print(f'{margin}  > : {answer}')
                else:
                    print(f'{margin}  ?')
                    answer = 0
                    print(f'{margin}  ? {0}: (skip) {(n - 1, k)}')
                    # try skipping first segment, squeeze everything in afterwards
                    answer += NOS(n - 1, k, depth + 1)
                    for i in range(1, n):
                        print(f'{margin}  ? {i}: {i}*{(n - i, k - 1)}')
                        first1 = i  # segment MUST touch endpoint: (__X, _XX, XXX)
                        others = NOS(n - i, k - 1, depth + 1)
                        answer += first1 * others
                        print(f'{margin}  {answer} += {first1} * {others}')
                cache[pair] = answer
                print(f'{margin}NOS({n},{k}): {answer}')
            else:
                print(f'{margin}NOS({n},{k}): cache hit {cache[pair]}')
            return cache[pair]

        return NOS(n - 1, k)
# NOTE: this doesn't work, so I'm starting over, but didn't want to lose this version
