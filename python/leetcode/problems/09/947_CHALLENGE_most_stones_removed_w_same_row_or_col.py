class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        stones = tuple(map(tuple, stones))  # make each pair a tuple

        stonesByX = {}
        stonesByY = {}
        for S in stones:
            (X, Y) = S
            stonesByX.setdefault(X, set())
            stonesByY.setdefault(Y, set())
            stonesByX[X].add(S)
            stonesByY[Y].add(S)
        # print(f'{stonesByX=}')
        # print(f'{stonesByY=}')

        adjacent = {}
        for S in stones:
            (X, Y) = S
            adjacent[S] = (stonesByX[X] | stonesByY[Y]) - {S}
        # print(f'{adjacent=}')

        seen = set()
        groups = []
        # thisGroup = set()
        for S in stones:
            print(f'{S=}')
            if S in seen:
                print(f'  (seen)')
                continue
            else:
                seen.add(S)
            queue = {S}
            thisGroup = {S}
            while queue:
                Q = queue.pop()
                print(f'  {Q=}')
                for A in adjacent[Q]:
                    print(f'    {A=}')
                    if A in seen:
                        print(f'      (seen)')
                        continue
                    else:
                        seen.add(A)
                    thisGroup.add(A)
                    queue.add(A)
            print(f'  {thisGroup=}')
            groups.append(thisGroup)
            thisGroup = None
        print(f'{groups=}')

        return sum([
            len(G) - 1
            for G in groups
        ])

# NOTE: Accepted on first Submit
# NOTE: Runtime 220 ms Beats 27.42%
# NOTE: Memory 18.46 MB Beats 12.44%
