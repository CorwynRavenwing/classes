class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        numSet = set(nums)
        seen = set()
        answer = -1
        for N in sorted(numSet):
            print(f'{N=}')
            if N in seen:
                print(f'  (seen)')
                continue
            else:
                seen.add(N)
            streak = 1
            Square = N * N
            while Square in numSet:
                print(f'  {Square=}')
                seen.add(Square)
                streak += 1
                answer = max(answer, streak)
                Square = Square * Square
        return answer
# NOTE: Runtime 708 ms Beats 35.96%
# NOTE: Memory 37.32 MB Beats 13.79%

# NOTE: re-ran for challenge:
# NOTE: Runtime 147 ms Beats 37.84%
# NOTE: Memory 38.87 MB Beats 8.33%
