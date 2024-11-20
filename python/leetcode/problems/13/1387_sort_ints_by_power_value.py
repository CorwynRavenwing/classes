class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @cache
        def Collatz(x: int) -> int:
            print(f'Collatz({x})')
            if x == 1:
                return 0
            if x % 2 == 0:
                new_x = x // 2
            else:
                new_x = 3 * x + 1
            return 1 + Collatz(new_x)
        
        answers = [
            (Collatz(N), N)
            for N in range(lo, hi + 1)
        ]
        answers.sort()
        print(f'{answers=}')

        answer_pair = answers[k - 1]  # "Nth" is 1-basis
        (collatz_power, N) = answer_pair
        return N

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 235 ms Beats 45.48%
# NOTE: Memory 24.66 MB Beats 26.35%
