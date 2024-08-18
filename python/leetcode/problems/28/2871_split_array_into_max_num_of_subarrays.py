class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:

        AND = lambda x, y: x & y

        total = reduce(AND, nums)
        if total > 0:
            print(f'AND(nums)={total}: keep one single array')
            return 1

        print(f'AND(nums)={total}: split into as many 0 arrays as possible')
        
        # brute force method:
        queue = {(0, 0, ())}   # sum of zero prior groups == zero; this group is empty
        for N in nums:
            # print(f'{queue=}')
            newQ = set()
            for (priorGroupCount, priorSum, priorGroup) in queue:
                if priorGroup:
                    # B) close prior group; put N in new group
                    groupSum = reduce(AND, priorGroup)
                    if groupSum == 0:
                        # print(f'  AND({priorGroup}) -> {groupSum}')
                        newQ.add(
                            (priorGroupCount + 1, priorSum + groupSum, (N,))
                        )
                        continue    # and DO NOT perform step (A) below!
                # A) add N to the prior group
                newQ.add(
                    (priorGroupCount, priorSum, priorGroup + (N,))
                )
            queue = newQ
        # print(f'{queue=}')
        # close all groups
        answers = []
        for (priorGroupCount, priorSum, priorGroup) in queue:
            groupSum = reduce(AND, priorGroup)
            print(f'Check answer {priorGroupCount},{priorSum},{priorGroup}->{groupSum}')
            if groupSum == 0:
                print(f'  == 0: add one last group')
                answers.append(
                    (priorGroupCount + 1, priorSum + groupSum)
                )
            else:
                print(f'  != 0: merge with prior group')
                answers.append(
                    (priorGroupCount, AND(priorSum, groupSum))
                )
        print(f'{answers=}')
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

# NOTE: a much better algorithm which only has one path instead of N^2
# NOTE: Runtime 981 ms Beats 6.17%
# NOTE: Memory 27.46 MB Beats 58.02%
