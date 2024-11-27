class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        # VAL = lambda C: alphabet.index(C) + 1
        VAL = lambda C: alphabet.index(C)

        # @cache
        # def DP(n: int, k: int) -> str:
        #     # print(f'DP({n},{k})')
        #     if k < 0:
        #         return None
        #     if n == 0:
        #         if k == 0:
        #             return ''
        #         else:
        #             return None
            
        #     if k == n * 26:
        #         subset = 'z'
        #     else:
        #         subset = alphabet
             
        #     for letter in subset:
        #         # print(f'DP({n},{k}): "{letter}"')
        #         V = VAL(letter)
        #         rest = DP(n - 1, k - V)
        #         if rest is not None:
        #             # print(f'DP({n},{k}): "{letter+rest}"')
        #             return letter + rest
            
        #     return None
        
        # return DP(n, k)

        k -= n  # make letters zero-based instead

        (Zs, OtherChar) = divmod(k, 25)
        As = n - Zs - 1
        print(f'{As=} {OtherChar} {Zs=}')

        if As == -1:
            return ('z' * Zs)

        return ('a' * As) + alphabet[OtherChar] + ('z' * Zs)

# NOTE: Accepted on second Run (edge case of all Z's)
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 89.14%
# NOTE: Memory 18.37 MB Beats 47.92%
