class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        # STRATEGY:
        # first, use fences rather than fenceposts:
        n -= 1
        # next, picture n=5 k=3:
        # ...A===B...C===D...E===F...
        #  a   b   c   d   e   f   g
        # sections b, d, f (count == k) have minimum size of one
        # sections a, c, e, g (count == k+1) have minimum size of zero
        # total sections S = 2k+1
        # but together they must add up to n.
        # so the additions must add up to A=(n - k) to account for the three 1's.
        # 1: the answer therefore is "S choose A with duplicates", S=(2k + 1), A=(n - k)
        # 2: see "Stars and Bars": "Y choose Z with duplicates" == "(Z + Y - 1) choose Z".
        # 3: "A choose B" == (A!)/(B!)(A-B)!

        # merge equations 1 and 2:
        # 4a: "((n-k) + (2n - 2k - 1) - 1) choose (n-k)"
        # 4: "(3n - 3k - 2) choose (n-k)"

        # merge equations 4 and 3:
        # 5a: ((3n - 3k - 2)!)/((n-k)!)((3n - 3k - 2)-(n-k))!
        # 5: (3n - 3k - 2)!/(n - k)!(2n - 2k - 2)!

        mod = 10 ** 9 + 7
        
        cache = {}
        def factorial(n: int) -> int:
            if n not in cache:
                # print(f'F({n}): cache miss ...')
                if n in [0, 1]:
                    answer = 1
                else:
                    answer = n * factorial(n - 1)
                cache[n] = answer
            #     print(f'F({n}): {answer}')
            # else:
            #     print(f'F({n}): cache hit {cache[n]}')
            return cache[n]

        # 3: "N choose K" == (N!)/(K!)(N-K)!
        def NchooseK(N: int, K: int) -> int:
            print(f'NcK({N},{K}):')
            A = factorial(N)
            # print(f'  {A=} = factorial({N})')
            B = factorial(K)
            # print(f'  {B=} = factorial({K})')
            C = factorial(N - K)
            # print(f'  {C=} = factorial({N}-{K}={N - K})')
            answer = (A // B) // C
            # print(f'  {answer} = {A}/({B}*{C})')
            return answer

        # 2: see "Stars and Bars": "N choose K with duplicates" == "(K + N - 1) choose K".
        def NchooseKwithDuplicates(N: int, K: int) -> int:
            print(f'NcKdup({N},{K}):')
            return NchooseK(K + N - 1, K)

        # 1: the answer therefore is "S choose A with duplicates", S=(2k + 1), A=(n - k)
        print(f'{n=} {k=} S={2*k+1} A={n-k}')
        answer = NchooseKwithDuplicates(2*k + 1, n-k)
        answer %= mod
        return answer
# NOTE: Runtime 51 ms; Beats 79.17%
# NOTE: Memory 28.61 MB; Beats 62.50%
