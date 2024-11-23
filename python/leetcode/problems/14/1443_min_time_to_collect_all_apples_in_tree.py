class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adjacentTo = {}
        for i in range(n):
            adjacentTo.setdefault(i, set())
        for (fromI, toI) in edges:
            adjacentTo[fromI].add(toI)
            adjacentTo[toI].add(fromI)
        print(f'{adjacentTo=}')

        parentOf = {}
        childrenOf = {}
        for i in range(n):
            parentOf.setdefault(i, None)
            childrenOf.setdefault(i, set())
        parentOf[0] = -1
        queue = {0}
        while queue:
            P = queue.pop()
            assert parentOf[P] is not None
            for C in adjacentTo[P]:
                if C == parentOf[P]:
                    continue
                parentOf[C] = P
                childrenOf[P].add(C)
                queue.add(C)
        print(f'{parentOf=}')
        print(f'{childrenOf=}')

        def AppleDistance(node: int, uplink=0) -> int:
            print(f'AD({node}):')
            childDistances = [
                AppleDistance(child, 1)
                for child in childrenOf[node]
            ]
            print(f'AD({node}): {childDistances=}')
            childTotal = sum(childDistances)
            print(f'AD({node}): {childTotal=}')
            retval = (
                (childTotal + uplink)
                if childTotal
                else uplink
                if hasApple[node]
                else 0
            )
            print(f'AD({node}): {retval=}')
            return retval

        return 2 * AppleDistance(0)

# NOTE: Accepted on third Run (variable-name typos)
# NOTE: Accepted on second Submit (fencepost error)
# NOTE: Runtime 510 ms Beats 5.21%
# NOTE: Memory 116.97 MB Beats 5.04%
