class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        
        # Note: "move abs(N) right if N>0
        #   and move abs(N) left if N<0
        #   and don't move if N==0"
        # is exactly the same as
        # "move N right, preserving sign"
        raw_indexes = [
            (i + N)
            for i, N in enumerate(nums)
        ]
        print(f'{raw_indexes=}')

        indexes = [
            i % len(nums)
            for i in raw_indexes
        ]
        print(f'{indexes=}')

        answers = [
            nums[i]
            for i in indexes
        ]

        return answers

# NOTE: Acceptance Rate 61.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 61 ms Beats 49.33%
# NOTE: Memory 19.34 MB Beats 34.53%
