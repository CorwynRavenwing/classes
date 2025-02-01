class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        parity = [
            N % 2
            for N in nums
        ]
        # print(f'{parity=}')

        pairs = tuple(pairwise(parity))
        # print(f'{pairs=}')

        sums = tuple(map(sum, pairs))
        # print(f'{sums=}')

        translate = (1, 0, 1)
        problems = tuple([
            translate[S]
            for S in sums
        ])
        # print(f'{problems=}')

        problemSums = (0,) + tuple(accumulate(problems))
        # print(f'{problemSums=}')

        # always_true = (
        #     True if len(sums) == 0
        #     else
        #     False if 0 in sums
        #     else
        #     False if 2 in sums
        #     else
        #     True
        # )
        # always_false = (
        #     False if always_true
        #     else
        #     False if 1 in sums
        #     else
        #     True 
        # )
        # print(f'{always_true =}')
        # print(f'{always_false=}')

        def doQuery(Q: List[int]) -> int:
            print(f'{Q=}')
            (fromI, toI) = Q
            # if fromI == toI:
            #     # only testing parity of 1 number against itself
            #     return True
            # if always_false:
            #     return False
            # if always_true:
            #     return True
            issues = problemSums[toI] - problemSums[fromI]
            print(f'  {issues=}')
            return (issues == 0)

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Runtime 254 ms Beats 5.01%
# NOTE: Memory 55.36 MB Beats 5.04%
