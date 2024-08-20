class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:

        # since all our operations have to do with flipping bits,
        # we can Without Loss Of Generality merge the two numbers
        # into a collection of *differences* and then work towards
        # *eliminating* them.
        print(f'{s1=}\n{s2=}')
        diffs = tuple([
            (1 if (A != B) else 0)
            for (A, B) in zip(s1, s2)
        ])
        # print(f'{diffs=}')
        totalDiffs = sum(diffs)
        if totalDiffs % 2 != 0:
            print(f'NO: {totalDiffs=} is odd')
            return -1
        
        @cache
        def flip(indexes: List[int], index1: int, index2: int) -> List[int]:
            for i in [index1, index2]:
                if i in indexes:
                    indexes = tuple([index for index in indexes if index != i])
                else:
                    indexes = indexes + (i,)
            
            return tuple(sorted(indexes))
        
        @cache
        def costToClearDiffs(indexes: List[int]) -> int:
            print(f'costToClearDiffs{indexes}')
            if not indexes:
                return 0
            first = indexes[0]
            second = indexes[1]     # count is even --> GT 0 means at least 2
            others = indexes[2:]

            # if we ever use the 1-cost operation, we use it several times:
            # 1000100101    original
            # 0100100101    1
            # 0010100101    2
            # 0001100101    3
            # 0000000101    4: first and second are gone at cost Y
            y = second - first
            # then we use either this method, or the x-cost operation,
            # whichever is cheaper

            return min(
                [
                    (
                        min(x, y)
                    ) + costToClearDiffs(flip(indexes, first, second))
                ] + [
                    x + costToClearDiffs(flip(indexes, first, other))
                    for other in others
                ]
            )

        indexes = tuple([index for index, value in enumerate(diffs) if value == 1])
        return costToClearDiffs(indexes)

# NOTE: Time Limit Exceeded for large inputs
