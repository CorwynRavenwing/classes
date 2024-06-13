class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        mod = 10 ** 9 + 7

        arr.sort()
        Factors = {}

        for i, N in enumerate(arr):
            print(f'factors: {N}')
            Factors[N] = []
            for F in arr[:i]:
                if N % F == 0:
                    # F divides N
                    Q = N // F
                    if Q in arr:
                        quotient = (F, Q)
                        print(f'  {N}: {quotient}')
                        Factors[N].append(quotient)
                    else:
                        print(f'  {N}: {F} -> invalid {Q}')
        print(f'{Factors=}')

        TreesRootedAt = {}
        for N in arr:
            print(f'trees: {N}:')
            TreesRootedAt[N] = 1    # can always do [N]
            print(f'  -> {TreesRootedAt[N]}')
            for quotient in Factors[N]:
                (F, Q) = quotient
                treesF = TreesRootedAt[F]
                treesQ = TreesRootedAt[Q]
                TreesRootedAt[N] += treesF * treesQ
                print(f'  -> {TreesRootedAt[N]} ({quotient})')
                TreesRootedAt[N] %= mod
                print(f'  -> {TreesRootedAt[N]} (%)')
        print(f'{TreesRootedAt=}')
        answer = sum([
            count
            for root, count in TreesRootedAt.items()
        ])
        answer %= mod
        return answer

