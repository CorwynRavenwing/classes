class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:

        def coprime(d1: str, d2: str) -> bool:
            pair = (
                d1+d2
                if d1 < d2
                else
                d2+d1
            )
            return pair not in (
                '22', '24', '26', '28',   # constraint: won't be a zero
                '33', '36', '39',
                '44', '46', '48',
                '55',
                '66', '68', '69',
                '77', '88', '99',
            )
        
        def firstDigit(num: int) -> str:
            return str(num)[0]

        def lastDigit(num: int) -> str:
            return str(num)[-1]
        
        def beautiful(n1: int, n2: int) -> bool:
            return coprime(
                firstDigit(n1),
                lastDigit(n2)
            )
        
        beautiful_pairs = [
            (Ni, Nj)
            for i, Ni in enumerate(nums)
            for j, Nj in enumerate(nums)
            if i < j and beautiful(Ni, Nj)
        ]
        print(f'{beautiful_pairs=}')
        return len(beautiful_pairs)

