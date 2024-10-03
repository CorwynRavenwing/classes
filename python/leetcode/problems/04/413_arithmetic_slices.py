class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        diffGroups = [
            (B - A, 1)
            for (A, B) in pairwise(nums)
        ]
        # print(f'{diffGroups=}')
        for i in range(1, len(diffGroups)):
            (prevAnswer, prevCount) = diffGroups[i - 1]
            (thisAnswer, thisCount) = diffGroups[i]
            if prevAnswer != thisAnswer:
                continue
            diffGroups[i - 1] = None
            diffGroups[i] = (thisAnswer, prevCount + thisCount)
        while None in diffGroups:
            diffGroups.remove(None)
        print(f'{diffGroups=}')
        
        diffs = [
            count - 1
            for (answer, count) in diffGroups
            if count >= 2
        ]
        print(f'{diffs=}')

        answers = [
            D * (D + 1) // 2    # triangle number
            for D in diffs
        ]
        print(f'{answers=}')

        return sum(answers)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 47 ms Beats 12.50%
# NOTE: Memory 17.25 MB Beats 6.65%
