class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        EO = [
            (
                'E'
                if A % 2 == 0
                else 'O'
            )
            for A in arr
        ]
        print(f'{EO=}')
        eoStr = ''.join(EO)
        print(f'{eoStr=}')
        return 'OOO' in eoStr

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 18.13 MB Beats 18.18%
# NOTE: I didn't snapshot this one before, so it's been sped up greatly
