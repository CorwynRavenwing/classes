class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:

        MAX_TYPE_1 = 2

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
            # print(f'Q={len(queues)} ${costSoFar} {len(Q)}')
            if costSoFar >= bestAnswer:
                print(f'  NO: ${costSoFar} >= {bestAnswer}')
                del queues[costSoFar]
                continue
            if not Q:
                print(f'  Queue empty at ${costSoFar}')
                del queues[costSoFar]
                continue
            indexes = Q.pop()   # order is now irrelevant
            # print(f'  {costSoFar}: {indexes[:5]}...')

            if not indexes:
                bestAnswer = min(bestAnswer, costSoFar)
                continue

            if indexes in seen:
                # print(f'    seen')
                continue
            else:
                seen.add(indexes)
            
            # if we ever use the 1-cost operation, we use it several times:
            # 1000100101    original
            # 0100100101    1
            # 0010100101    2
            # 0001100101    3
            # 0000000101    4: first and second are gone at cost Y = (index2 - index1)
            # but we only use this method if it is cheaper than the x-cost operation

            # first pass: the 1-cost operation, on each adjacent pair, if possible
            found = 0
            for first, second in pairwise(indexes):
                # print(f'  1-op: try {first},{second}')
                y = second - first
                if y >= x:
                    # print(f'    NO: too far apart ({y=})')
                    continue

                new1 = [
                    flip(indexes, first, second)
                ]
                new1 = [
                    N
                    for N in new1
                    if N not in seen
                ]
                if not new1:
                    continue
                # print(f'      +{y}: 1')
                costY = costSoFar + y
                queues.setdefault(costY, set())
                for N in new1:
                    queues[costY].add(N)
                    found += 1
                if found >= MAX_TYPE_1:
                    break
            
            # second pass: the X-cost operation, if no 1-cost ops were found
            if found:
                continue
            # else:
            #     # print(f'    No 1-cost found: using X-cost instead')
            first = indexes[0]
            second = indexes[1]
            new2 = [
                flip(indexes, first, second)
            ]
            new2 = [
                N
                for N in new2
                if N not in seen
            ]

            if not new2:
                continue
            # print(f'      +{x}: {len(new2)}')
            costX = costSoFar + x
            queues.setdefault(costX, set())
            for N in new2:
                queues[costX].add(N)

        return bestAnswer

# NOTE: *STILL* Time Limit Exceeded, but only for huge inputs.
