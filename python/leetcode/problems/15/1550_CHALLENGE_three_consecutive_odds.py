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

