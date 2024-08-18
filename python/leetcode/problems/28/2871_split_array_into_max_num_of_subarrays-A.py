class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:

        AND = lambda x, y: x & y

        # brute force method:
        queue = {(0, 0, ())}   # sum of zero prior groups == zero; this group is empty
        for N in nums:
            # print(f'{queue=}')
            newQ = set()
            for (priorGroupCount, priorSum, priorGroup) in queue:
                # A) add N to the prior group
                newQ.add(
                    (priorGroupCount, priorSum, priorGroup + (N,))
                )
                if priorGroup:
                    # B) close prior group; put N in new group
                    groupSum = reduce(AND, priorGroup)
                    # print(f'  AND({priorGroup}) -> {groupSum}')
                    newQ.add(
                        (priorGroupCount + 1, priorSum + groupSum, (N,))
                    )
            queue = newQ
        # print(f'{queue=}')
        # close all groups
        answers = [
            (priorGroupCount + 1, priorSum + reduce(AND, priorGroup))
            for (priorGroupCount, priorSum, priorGroup) in queue
        ]
        # print(f'{answers=}')
        minSum = min([
            total
            for (groups, total) in answers
        ])
        print(f'{minSum=}')
        maxGroups = max([
            groups
            for (groups, total) in answers
            if total == minSum
        ])
        print(f'{maxGroups=}')
        return maxGroups

# NOTE: Brute force method.  TLE for large inputs.
