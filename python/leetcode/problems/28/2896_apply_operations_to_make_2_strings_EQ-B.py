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
        
        indexes = tuple([index for index, value in enumerate(diffs) if value == 1])
        queue = [(0, indexes)]
        seen = set()
        bestAnswer = float('inf')
        while queue:
            print(f'L={len(queue)}')
            # queue.sort()      # maintaining sorted order with bisect.insort()
            (costSoFar, indexes) = queue.pop(0)
            if costSoFar >= bestAnswer:
                continue
            print(f'  {costSoFar}: {indexes}')

            if not indexes:
                bestAnswer = min(bestAnswer, costSoFar)
                continue

            if indexes in seen:
                print(f'    seen')
                continue
            else:
                seen.add(indexes)
            
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
            Z = min(x, y)

            new = [
                (costSoFar + Z, flip(indexes, first, second))
            ] + [
                (costSoFar + x, flip(indexes, first, other))
                for other in others
            ]
            print(f'      +{Z}: 1')
            print(f'      +{x}: {len(new)-1}')
            for N in new:
                if N in seen:
                    print(f'      SKIP {N}')
                    continue
                else:
                    # print(f'      +{N}')
                    bisect.insort(queue, N)

        return bestAnswer

# NOTE: much faster, but still Time Limit Exceeded for huge inputs
