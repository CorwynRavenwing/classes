class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        @cache
        def magic(i: int) -> int:
            iPlus1 = i + 1
            Or = i | iPlus1     # "|": bitwise or operator
            print(f'{i}|{iPlus1} = {Or}')
            return Or

        def find_magic(N: int) -> int:
            for i in range(N + 1):
                answer = magic(i)
                if answer == N:
                    return i
            return -1
        
        answer = [
            find_magic(N)
            for N in nums
        ]
        
        return answer

# NOTE: Acceptance Rate 74.7% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 346 ms Beats 5.15%
# NOTE: Memory 19.59 MB Beats 15.44%
