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
        queues = {0: {indexes}}     # Dict[int,Set[List[int]]]
        seen = set()
        bestAnswer = float('inf')
        while queues:
            worstCost = max(queues)
            if worstCost >= bestAnswer:
                print(f'  Trash ${worstCost}')
                del queues[worstCost]
                continue
            costSoFar = min(queues)
            Q = queues[costSoFar]
            print(f'Q={len(queues)} ${costSoFar} {len(Q)}')
            if costSoFar >= bestAnswer:
                print(f'  NO: ${costSoFar} >= {bestAnswer}')
                del queues[costSoFar]
                continue
            if not Q:
                print(f'  Queue empty at ${costSoFar}')
                del queues[costSoFar]
                continue
            indexes = Q.pop()   # order is now irrelevant
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

            new1 = [
                flip(indexes, first, second)
            ]
            new2 = [
                flip(indexes, first, other)
                for other in others
            ]
            new1 = [
                N
                for N in new1
                if N not in seen
            ]
            new2 = [
                N
                for N in new2
                if N not in seen
            ]
            print(f'      +{Z}: 1')
            print(f'      +{x}: {len(new2)}')
            costZ = costSoFar + Z
            costX = costSoFar + x
            queues.setdefault(costZ, set())
            queues.setdefault(costX, set())
            for N in new1:
                queues[costZ].add(N)
            for N in new2:
                queues[costX].add(N)

        return bestAnswer

# NOTE: still a Time Limit Exceeded for very large inputs
