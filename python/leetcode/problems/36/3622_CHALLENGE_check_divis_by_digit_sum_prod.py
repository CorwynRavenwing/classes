class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        digits = tuple(map(int, str(n)))
        print(f'{digits=}')

        digisum = sum(digits)
        digiprod = math.prod(digits)
        print(f'{digisum=} {digiprod=}')
        answer = (n % (digisum + digiprod)) == 0

        return answer

# NOTE: Acceptance Rate 70.6% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (polarity reversed)
# NOTE: Runtime 3 ms Beats 8.74%
# NOTE: Memory 19.37 MB Beats 23.77%
