class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        
        def NullSafeMax(A, B):
            return (
                None if (A is None) and (B is None)
                else A if (B is None)
                else B if (A is None)
                else max(A, B)
            )
        
        parityAtIndex = [N % 2 for N in nums]
        maxParityScoreBefore = []
        # referenced as MPSB[parity][index]
        maxParityScoreBefore = [[None, None]] * len(nums)
        # print(f'DEBUG: {maxParityScoreBefore=}')

        # maxParityScoreBefore[0] = [0, 0]
        parity = parityAtIndex[0]
        maxParityScoreBefore[0][parity] = nums[0]    # get first value for free
        # print(f'{0}: ({parity}) {maxParityScoreBefore[0]}')
        for i in range(1, len(nums)):
            SB = maxParityScoreBefore[i - 1]
            parity = parityAtIndex[i]
            other_parity = (1 - parity)
            # print(f'DEBUG: {SB=} {parity=} {other_parity=}')
            # print(f'DEBUG: {maxParityScoreBefore[i]=}')
            thing1 = (
                nums[i] + SB[parity]
                if SB[parity] is not None
                else None
            )
            thing2 = (
                nums[i] + SB[other_parity] - x
                if SB[other_parity] is not None
                else None
            )
            maxParityScoreBefore[i][parity] = NullSafeMax(thing1,thing2)
            maxParityScoreBefore[i][other_parity] = SB[other_parity]
            # print(f'{i}: ({parity}) {maxParityScoreBefore[i]}')

        (A, B) = maxParityScoreBefore[-1]
        return NullSafeMax(A, B)
# NOTE: Runtime 861 ms Beats 63.73%
# NOTE: Memory 31.64 MB Beats 61.14%
